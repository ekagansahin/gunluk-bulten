#!/usr/bin/env python3
"""
Faz 1 — API test betiği.

api_listesi.md dosyasında [x] ile işaretli API'leri tek tek dener,
ham yanıtları ham/<tarih>/ klasörüne kaydeder ve api_katalog.md raporunu yazar.

Kullanım:
    python3 api_test.py              # sadece [x] olanları dener
    python3 api_test.py --hepsi      # [ ] olanlar dahil hepsini dener
    python3 api_test.py --sadece afad,yahoo
    python3 api_test.py --telegram   # sonuç özetini Telegram'a da gönderir
"""
import argparse
import datetime as dt
import html
import json
import os
import re
import time
from pathlib import Path

import requests

KOK = Path(__file__).resolve().parent
LISTE = KOK / "api_listesi.md"
ENV = KOK / ".env"
HAM = KOK / "ham"
KATALOG = KOK / "api_katalog.md"
UA = "Mozilla/5.0 (compatible; api-bulten/0.1; kisisel kullanim)"
SATIR = re.compile(r"^- \[( |x|X)\]\s*(.+)$")


# ---------- .env ----------
def env_oku():
    # GitHub Actions'ta anahtarlar ortam değişkeni (Secrets) olarak gelir; yerelde .env dosyasından okunur
    d = {k: v for k, v in os.environ.items()
         if k.startswith("TELEGRAM_") or k.endswith("_API_KEY")}
    if ENV.exists():
        for s in ENV.read_text(encoding="utf-8").splitlines():
            s = s.strip()
            if s and not s.startswith("#") and "=" in s:
                k, v = s.split("=", 1)
                d[k.strip()] = v.strip().strip('"').strip("'")
    return d


def env_ekle(anahtar, deger):
    metin = ENV.read_text(encoding="utf-8") if ENV.exists() else ""
    if metin and not metin.endswith("\n"):
        metin += "\n"
    ENV.write_text(metin + f"{anahtar}={deger}\n", encoding="utf-8")


# ---------- liste ----------
def liste_oku(hepsi=False, sadece=None):
    apiler, kategori = [], ""
    for s in LISTE.read_text(encoding="utf-8").splitlines():
        if s.startswith("## "):
            kategori = s[3:].strip()
            continue
        m = SATIR.match(s.strip())
        if not m:
            continue
        p = [x.strip() for x in m.group(2).split(" | ")]
        if len(p) < 5:
            continue
        secili = m.group(1).lower() == "x"
        api = dict(id=p[0], ad=p[1], anahtar=p[2], url=p[4],
                   not_=p[5] if len(p) > 5 else "", kategori=kategori, secili=secili)
        if sadece:
            if api["id"] in sadece:
                apiler.append(api)
        elif secili or hepsi:
            apiler.append(api)
    return apiler


def yer_tut(url):
    b = dt.date.today()
    # {NASA_API_KEY} gibi büyük harfli yer tutucular .env'den doldurulur
    for k, v in env_oku().items():
        url = url.replace("{" + k + "}", v)
    return (url.replace("{bugun}", b.isoformat())
               .replace("{dun}", (b - dt.timedelta(days=1)).isoformat())
               .replace("{hafta}", (b - dt.timedelta(days=7)).isoformat())
               .replace("{AA}", f"{b.month:02d}")
               .replace("{GG}", f"{b.day:02d}"))


# ---------- istek ----------
def dene(api):
    url = yer_tut(api["url"])
    t0 = time.time()
    for deneme in range(2):  # geçici bağlantı hatalarına karşı 1 tekrar
        try:
            r = requests.get(url, headers={"User-Agent": UA, "Accept": "*/*"}, timeout=20)
            return dict(url=url, kod=r.status_code, sure=time.time() - t0,
                        tip=r.headers.get("Content-Type", "").split(";")[0],
                        govde=r.content, hata=None)
        except requests.RequestException as e:
            hata = f"{type(e).__name__}: {str(e)[:150]}"
            time.sleep(2)
    return dict(url=url, kod=None, sure=time.time() - t0, tip="", govde=b"", hata=hata)


def durum(s):
    if s["hata"] or s["kod"] is None:
        return "❌"
    if s["kod"] == 200 and len(s["govde"]) > 0:  # "[]" = çalışıyor ama bugün veri yok
        return "✅"
    return "⚠️"


def ozet(govde):
    metin = govde.decode("utf-8", errors="replace")
    try:
        veri = json.loads(metin)
    except ValueError:
        return re.sub(r"\s+", " ", metin)[:400]
    if isinstance(veri, list):
        if not veri:
            return "boş liste"
        return f"liste[{len(veri)}], ilk öğe: " + json.dumps(veri[0], ensure_ascii=False)[:350]
    if isinstance(veri, dict):
        return ("anahtarlar: " + ", ".join(map(str, list(veri)[:12])) + "\n"
                + json.dumps(veri, ensure_ascii=False)[:350])
    return str(veri)[:400]


def kaydet(api, s, klasor):
    if not s["govde"]:
        return None
    tip = s["tip"]
    uzanti = "json" if "json" in tip else "xml" if ("xml" in tip or "rss" in tip) else "txt"
    yol = klasor / f"{api['id']}.{uzanti}"
    yol.write_bytes(s["govde"])
    return yol.relative_to(KOK)


# ---------- rapor ----------
def katalog_yaz(sonuclar, zaman):
    ok = sum(1 for _, s in sonuclar if durum(s) == "✅")
    satirlar = [
        "# API Kataloğu — test sonuçları",
        "",
        f"Son test: {zaman:%d.%m.%Y %H:%M} · {ok}/{len(sonuclar)} API çalıştı",
        "",
        "| Durum | Kimlik | Ad | Kategori | HTTP | Süre | Boyut | Tip |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for api, s in sonuclar:
        satirlar.append(
            f"| {durum(s)} | `{api['id']}` | {api['ad']} | {api['kategori']} | "
            f"{s['kod'] or '-'} | {s['sure']:.1f} sn | {len(s['govde'])/1024:.1f} KB | {s['tip'] or '-'} |")
    satirlar.append("")
    for api, s in sonuclar:
        satirlar += [f"## {durum(s)} {api['id']} — {api['ad']}", "",
                     f"- URL: `{api['url']}`", f"- Anahtar: {api['anahtar']}"]
        if api["not_"]:
            satirlar.append(f"- Not: {api['not_']}")
        if s.get("dosya"):
            satirlar.append(f"- Ham yanıt: `{s['dosya']}`")
        if s["hata"]:
            satirlar.append(f"- Hata: {s['hata']}")
        elif s["govde"]:
            satirlar += ["", "```", ozet(s["govde"]), "```"]
        satirlar.append("")
    KATALOG.write_text("\n".join(satirlar), encoding="utf-8")


# ---------- telegram ----------
def tg(token, yontem, **params):
    try:
        r = requests.post(f"https://api.telegram.org/bot{token}/{yontem}", json=params, timeout=20)
        return r.json()
    except (requests.RequestException, ValueError) as e:
        return {"ok": False, "description": str(e)[:150]}


def telegram_gonder(sonuclar, zaman):
    env = env_oku()
    token = env.get("TELEGRAM_TOKEN")
    if not token:
        print("Telegram: .env içinde TELEGRAM_TOKEN yok.")
        return
    me = tg(token, "getMe")
    if not me.get("ok"):
        print("Telegram: token geçersiz görünüyor →", me.get("description"))
        return
    print(f"Telegram: bot bulundu → @{me['result']['username']}")

    chat_id = env.get("TELEGRAM_CHAT_ID")
    if not chat_id:
        guncel = tg(token, "getUpdates")
        for u in reversed(guncel.get("result", [])):
            msg = u.get("message") or u.get("edited_message")
            if msg:
                chat_id = str(msg["chat"]["id"])
                env_ekle("TELEGRAM_CHAT_ID", chat_id)
                print("Telegram: chat_id bulundu ve .env'e eklendi.")
                break
    if not chat_id:
        print(f"Telegram: chat_id bulunamadı. Telegram'da @{me['result']['username']} botuna "
              "bir mesaj gönderip betiği tekrar çalıştır.")
        return

    ok = sum(1 for _, s in sonuclar if durum(s) == "✅")
    metin = [f"🧪 API testi — {zaman:%d.%m.%Y %H:%M}", f"{ok}/{len(sonuclar)} API çalıştı", ""]
    kategori = None
    for api, s in sonuclar:
        if api["kategori"] != kategori:
            kategori = api["kategori"]
            metin.append(f"\n{kategori}")
        ek = f"HTTP {s['kod']}" if s["kod"] and s["kod"] != 200 else f"{s['sure']:.1f} sn"
        if s["hata"]:
            ek = s["hata"].split(":")[0]
        metin.append(f"{durum(s)} {api['id']} ({ek})")
    cevap = tg(token, "sendMessage", chat_id=chat_id, text="\n".join(metin)[:4000],
               disable_web_page_preview=True)
    print("Telegram: mesaj gönderildi." if cevap.get("ok") else f"Telegram hatası: {cevap.get('description')}")

    # NASA günün astronomi fotoğrafı
    for api, s in sonuclar:
        if api["id"] == "nasa_apod" and durum(s) == "✅":
            veri = json.loads(s["govde"])
            apod_gonder(token, chat_id, veri[0] if isinstance(veri, list) else veri)


def apod_temizle(s):
    """science.nasa.gov metinleri HTML geliyor: etiketleri ve 'Explanation:' önekini atar."""
    s = html.unescape(re.sub(r"<[^>]+>", "", str(s or "")))
    return re.sub(r"^\s*Explanation:\s*", "", s).strip()


def apod_gonder(token, chat_id, veri):
    # science.nasa.gov biçimi: görsel hdurl'de (video günlerinde kapak görseli), url makale sayfası
    baslik = f"🔭 NASA — Günün Astronomi Fotoğrafı\n{veri.get('title', '')} ({veri.get('date', '')})"
    if veri.get("copyright"):
        baslik += f"\n© {apod_temizle(veri['copyright'])}"
    if veri.get("media_type") != "image":
        baslik += "\n🎬 Bugün video var, linke bak"
    sayfa = veri.get("permalink") or veri.get("url", "")
    cevap = {"ok": False}
    gorsel = veri.get("hdurl")
    if gorsel:
        cevap = tg(token, "sendPhoto", chat_id=chat_id, photo=gorsel, caption=f"{baslik}\n{sayfa}"[:1024])
        if not cevap.get("ok"):  # HD dosya Telegram'ın 5 MB sınırını aşarsa küçültülmüş hali
            cevap = tg(token, "sendPhoto", chat_id=chat_id, photo=gorsel.split("?")[0] + "?w=1280",
                       caption=f"{baslik}\n{sayfa}"[:1024])
    if not cevap.get("ok"):
        cevap = tg(token, "sendMessage", chat_id=chat_id, text=f"{baslik}\n{sayfa}")
    if cevap.get("ok") and veri.get("explanation"):
        tg(token, "sendMessage", chat_id=chat_id, text=apod_temizle(veri["explanation"])[:4000])
    print("Telegram: APOD gönderildi." if cevap.get("ok") else f"Telegram APOD hatası: {cevap.get('description')}")


# ---------- ana ----------
def main():
    ap = argparse.ArgumentParser(description="api_listesi.md'deki API'leri test eder.")
    ap.add_argument("--hepsi", action="store_true", help="[ ] olanlar dahil hepsini dene")
    ap.add_argument("--sadece", help="virgülle ayrılmış kimlikler, ör. afad,yahoo")
    ap.add_argument("--telegram", action="store_true", help="özeti Telegram'a gönder")
    a = ap.parse_args()

    sadece = set(a.sadece.split(",")) if a.sadece else None
    apiler = liste_oku(a.hepsi, sadece)
    zaman = dt.datetime.now()
    klasor = HAM / zaman.strftime("%Y-%m-%d")
    klasor.mkdir(parents=True, exist_ok=True)

    sonuclar = []
    for api in apiler:
        eksik = re.findall(r"\{([A-Z_]+)\}", yer_tut(api["url"]))
        if eksik:
            s = dict(url=api["url"], kod=None, sure=0.0, tip="", govde=b"",
                     hata=f".env içinde eksik anahtar: {', '.join(eksik)}")
        elif api["anahtar"] == "ücretsiz":
            s = dict(url=api["url"], kod=None, sure=0.0, tip="", govde=b"",
                     hata="Anahtar gerekiyor; henüz eklenmedi, atlandı")
        else:
            s = dene(api)
            s["dosya"] = kaydet(api, s, klasor)
        sonuclar.append((api, s))
        print(f"{durum(s)} {api['id']:<18} {str(s['kod'] or '-'):>4}  {s['sure']:5.1f} sn  "
              f"{len(s['govde'])/1024:7.1f} KB  {s['hata'] or ''}")

    katalog_yaz(sonuclar, zaman)
    ok = sum(1 for _, s in sonuclar if durum(s) == "✅")
    print(f"\n{ok}/{len(sonuclar)} API çalıştı → {KATALOG.name}, ham yanıtlar → {klasor.relative_to(KOK)}/")

    if a.telegram:
        telegram_gonder(sonuclar, zaman)


if __name__ == "__main__":
    main()
