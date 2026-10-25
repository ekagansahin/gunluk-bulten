#!/usr/bin/env python3
"""
Faz 2 — Günlük ham bülten.

api_listesi.md'deki API'leri çeker; her kategoriyi ayrı Telegram mesajı olarak
gönderir. Görsel dönen API'ler (NASA, xkcd, köpek, tilki, ördek...) fotoğraf olarak gelir.
Bu fazda veri yorumlanmıyor; her API'den sadece okunabilir alanlar seçiliyor.

Kullanım:
    python3 bulten.py            # [x] olanlar
    python3 bulten.py --hepsi    # [ ] olanlar dahil (anahtar isteyenler hariç)
    python3 bulten.py --kuru     # Telegram'a göndermez, ekrana yazar
"""
import argparse
import datetime as dt
import html
import json
import re
import xml.etree.ElementTree as ET

import requests

from api_test import HAM, UA, dene, durum, env_oku, kaydet, liste_oku, tg

EMOJI = {"Finans": "💰", "Hava": "🌤️", "Akademik": "🎓", "Genel": "🌍", "Eğlence": "🎲"}
BUGUN = dt.date.today()


def J(b):
    return json.loads(b)


def kisalt(s, n=300):
    s = re.sub(r"\s+", " ", html.unescape(str(s or ""))).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def tr_saat(iso):
    """UTC ISO zamanı Türkiye saatine çevirir."""
    t = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return (t + dt.timedelta(hours=3)).strftime("%d.%m %H:%M")


# ============ Finans ============
def f_tcmb_kur(b):
    kok = ET.fromstring(b)
    s = [f"Bülten tarihi: {kok.get('Tarih')}"]
    for c in kok.findall("Currency"):
        if c.get("Kod") in ("USD", "EUR"):
            s.append(f"{c.get('Kod')} ({c.findtext('Unit')}): alış {c.findtext('ForexBuying')} · satış {c.findtext('ForexSelling')}")
    return s, []


def f_frankfurter(b):
    d = J(b)
    s = [f"1 {d['base']} = ({d['date']})"]
    s += [f"{k}: {d['rates'][k]}" for k in ("EUR", "GBP", "CHF", "JPY", "CNY", "TRY") if k in d["rates"]]
    return s, []


def f_truncgil(b):
    d = J(b)
    s = [f"Güncelleme: {d.get('Update_Date')}"]
    for k in ("USD", "EUR", "GBP", "gram-altin", "ceyrek-altin", "yarim-altin", "tam-altin",
              "cumhuriyet-altini", "ons", "gumus"):
        if k in d:
            v = d[k]
            s.append(f"{k}: alış {v.get('Alış')} · satış {v.get('Satış')} ({v.get('Değişim')})")
    return s, []


def f_coingecko(b):
    return [f"{c}: ${v['usd']:,} · ₺{v['try']:,} · 24s {v['usd_24h_change']:+.2f}%"
            for c, v in J(b).items()], []


def f_binance(b):
    d = J(b)
    return [f"{d['symbol']}: {float(d['lastPrice']):,.2f} ({float(d['priceChangePercent']):+.2f}%) "
            f"· gün içi {float(d['lowPrice']):,.0f}–{float(d['highPrice']):,.0f}"], []


YAHOO = {"XU100.IS": "BIST 100", "USDTRY=X": "USD/TRY", "EURTRY=X": "EUR/TRY",
         "GC=F": "Altın (ons, $)", "BZ=F": "Brent petrol ($)", "^GSPC": "S&P 500", "^IXIC": "Nasdaq"}


def f_yahoo(b):
    s = []
    for sembol, ad in YAHOO.items():
        try:
            if sembol == "XU100.IS":
                m = J(b)["chart"]["result"][0]["meta"]
            else:
                r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{sembol}",
                                 headers={"User-Agent": UA}, timeout=15)
                m = r.json()["chart"]["result"][0]["meta"]
            f, onceki = m["regularMarketPrice"], m.get("chartPreviousClose") or m.get("previousClose")
            deg = f" ({(f / onceki - 1) * 100:+.2f}%)" if onceki else ""
            s.append(f"{ad}: {f:,.2f}{deg}")
        except Exception as e:
            s.append(f"{ad}: alınamadı ({type(e).__name__})")
    return s, []


# ============ Hava & Çevre ============
def f_openmeteo(b):
    d = J(b)["daily"]
    s = [f"☀️ Gün doğumu {d['sunrise'][0][-5:]} · batımı {d['sunset'][0][-5:]}"]
    for i in range(min(3, len(d["time"]))):
        gun = dt.date.fromisoformat(d["time"][i]).strftime("%d.%m")
        s.append(f"{gun}: {d['temperature_2m_min'][i]:.0f}–{d['temperature_2m_max'][i]:.0f}°C · yağış olasılığı %{d['precipitation_probability_max'][i]}")
    return s, []


def f_openmeteo_aq(b):
    c = J(b)["current"]
    return [f"PM10: {c['pm10']} µg/m³ · PM2.5: {c['pm2_5']} µg/m³ · Avrupa AQI: {c['european_aqi']}"], []


def f_afad(b):
    d = J(b)
    if not d:
        return ["Son 24 saatte M3+ deprem yok."], []
    d = sorted(d, key=lambda x: float(x["magnitude"]), reverse=True)
    return [f"{len(d)} deprem (M3+). En büyükler:"] + [
        f"M{x['magnitude']} · {x['location']} · {x['date'][5:16].replace('T', ' ')}" for x in d[:5]], []


def f_kandilli(b):
    r = J(b)["result"]
    buyuk = sorted(r, key=lambda x: x["mag"], reverse=True)[:5]
    return [f"Son 24 saatte {len(r)} deprem. En büyük 5:"] + [
        f"M{x['mag']} · {x['title']} · {x['date_time'][5:16]}" for x in buyuk], []


def f_usgs(b):
    f = J(b)["features"]
    if not f:
        return ["Dün bugün dünyada M6+ deprem yok."], []
    return [f"M{x['properties']['mag']} · {x['properties']['place']}" for x in f[:5]], []


def f_tatil(b):
    gelecek = [x for x in J(b) if dt.date.fromisoformat(x["date"]) >= BUGUN][:3]
    if not gelecek:
        return ["Bu yıl kalan resmî tatil yok."], []
    return [f"{x['localName']}: {dt.date.fromisoformat(x['date']):%d.%m.%Y} ({(dt.date.fromisoformat(x['date']) - BUGUN).days} gün kaldı)"
            for x in gelecek], []


# ============ Akademik ============
def f_arxiv_rss(b):
    kanal = ET.fromstring(b).find("channel")
    ogeler = kanal.findall("item") if kanal is not None else []
    if not ogeler:
        return ["Bugün yeni gönderim yok (arXiv hafta sonu yayın yapmıyor)."], []
    return [f"{len(ogeler)} yeni makale. İlk 5:"] + [
        f"• {kisalt(i.findtext('title'), 150)}\n  {i.findtext('link')}" for i in ogeler[:5]], []


def f_arxiv_api(b):
    ns = {"a": "http://www.w3.org/2005/Atom"}
    s = []
    for e in ET.fromstring(b).findall("a:entry", ns)[:5]:
        s.append(f"• {kisalt(e.findtext('a:title', namespaces=ns), 150)} ({e.findtext('a:published', namespaces=ns)[:10]})\n  {e.findtext('a:id', namespaces=ns)}")
    return s or ["Sonuç yok."], []


def f_openalex(b):
    d = J(b)
    s = [f"Son 7 günde {d['meta']['count']} yayın."]
    for w in d["results"][:5]:
        s.append(f"• {kisalt(w.get('display_name'), 150)} ({w.get('publication_date')})\n  {w.get('doi') or w.get('id')}")
    return s, []


def f_crossref(b):
    m = J(b)["message"]
    s = [f"Toplam {m['total-results']} kayıt. İlk 5:"]
    for w in m["items"][:5]:
        s.append(f"• {kisalt((w.get('title') or ['?'])[0], 150)} — {(w.get('container-title') or [''])[0]}\n  {w.get('URL')}")
    return s, []


def f_hackernews(b):
    s = []
    for i in J(b)[:5]:
        it = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json", timeout=15).json()
        s.append(f"• {it.get('title')} (▲{it.get('score')})\n  {it.get('url') or f'https://news.ycombinator.com/item?id={i}'}")
    return s, []


def f_github(b):
    return [f"• {r['full_name']} ★{r['stargazers_count']} — {kisalt(r.get('description'), 100)}\n  {r['html_url']}"
            for r in J(b)["items"][:5]], []


# ============ Genel ============
def f_wiki_bugun(b):
    d = J(b)
    return [f"{x.get('year', '')}: {kisalt(x['text'], 200)}" for x in d.get("selected", [])[:5]], []


def html_temizle(s):
    """science.nasa.gov metinleri HTML geliyor: etiketleri ve 'Explanation:' önekini atar."""
    s = html.unescape(re.sub(r"<[^>]+>", "", str(s or "")))
    return re.sub(r"^\s*Explanation:\s*", "", s).strip()


def f_nasa_apod(b):
    # science.nasa.gov/wp-json/wp/v2/apod-basic: liste döner; görsel hdurl'de, url makale sayfası
    d = J(b)
    d = d[0] if isinstance(d, list) else d
    sayfa = d.get("permalink") or d.get("url")
    s = [f"{d.get('title')} ({d.get('date')})", kisalt(html_temizle(d.get("explanation")), 400)]
    if d.get("media_type") != "image":  # video günü: hdurl kapak görseli, video linki basic_html içinde
        m = re.search(r'<(?:iframe|video|source)[^>]*\ssrc="([^"]+)"', d.get("basic_html") or "")
        video = m.group(1) if m else sayfa
        s.append(f"🎬 {'https:' + video if video.startswith('//') else video}")
    s.append(sayfa)
    gorsel = d.get("hdurl")
    if not gorsel:
        return s, []
    # yedek: HD dosya Telegram'ın 5 MB sınırını aşarsa 1280 px genişlikte küçültülmüş hali
    return s, [(gorsel, f"🔭 {d.get('title')}", gorsel.split("?")[0] + "?w=1280")]


def f_uzay_haber(b):
    return [f"• {x['title']} ({x['news_site']})\n  {x['url']}" for x in J(b)["results"]], []


def f_roket(b):
    return [f"• {x['name']} — {tr_saat(x['net'])} TSİ · {x['status']['name']} · {x['pad']['location']['name']}"
            for x in J(b)["results"]], []


def f_iss(b):
    d = J(b)
    return [f"{d['number']} kişi: " + ", ".join(p["name"] for p in d["people"]),
            "(Not: bu kaynağın verisi güncel olmayabilir)"], []


# ============ Eğlence ============
def f_xkcd(b):
    d = J(b)
    return [f"#{d['num']} {d['title']} ({d['day']}.{d['month']}.{d['year']})", kisalt(d["alt"])], \
           [(d["img"], f"xkcd #{d['num']}: {d['title']}", None)]


def f_soz(b):
    d = J(b)[0]
    return [f"“{d['q']}” — {d['a']}"], []


def f_bilgi(b):
    return [J(b)["text"]], []


def f_kedi_bilgi(b):
    return [J(b)["fact"]], []


def f_saka(b):
    d = J(b)
    return [d["joke"] if d.get("type") == "single" else f"{d['setup']}\n— {d['delivery']}"], []


def f_satranc_lichess(b):
    p = J(b)["puzzle"]
    return [f"Puan {p['rating']} · {', '.join(p['themes'][:4])}", f"https://lichess.org/training/{p['id']}"], []


def f_satranc_chesscom(b):
    d = J(b)
    return [d["title"], d["url"]], [(d["image"] + "&.png", f"♟️ {d['title']}", None)]


def f_epic(b):
    s, simdi, yakinda = [], [], []
    for g in J(b)["data"]["Catalog"]["searchStore"]["elements"]:
        p = g.get("promotions") or {}
        slug = (g.get("productSlug") or "").replace("/home", "") or \
               ((g.get("offerMappings") or [{}])[0].get("pageSlug") or "")
        link = f"https://store.epicgames.com/tr/p/{slug}" if slug else ""
        if p.get("promotionalOffers") and g["price"]["totalPrice"]["discountPrice"] == 0:
            simdi.append(f"• {g['title']}\n  {link}")
        elif p.get("upcomingPromotionalOffers"):
            yakinda.append(f"• {g['title']}")
    if simdi:
        s += ["Şu an ücretsiz:"] + simdi
    if yakinda:
        s += ["Yakında:"] + yakinda
    return s or ["Şu an ücretsiz oyun yok."], []


def f_kopek(b):
    u = J(b)["url"]
    return [], [(u, "🐶", None)]


def f_tilki(b):
    return [], [(J(b)["image"], "🦊", None)]


def f_ordek(b):
    return [], [(J(b)["url"].replace("http://", "https://"), "🦆", None)]


def genel_cikar(b):
    return [kisalt(b.decode("utf-8", "replace"), 400)], []


# ============ gönderim ============
AYLAR = ("January", "February", "March", "April", "May", "June", "July", "August",
         "September", "October", "November", "December")


def ayrac(token, chat_id, metin, kuru):
    """Günün başına ve sonuna konan ayraç mesajı."""
    if kuru:
        print(metin)
    else:
        tg(token, "sendMessage", chat_id=chat_id, text=metin)


def parcala(metin, n=4000):
    parca, simdi = [], ""
    for satir in metin.split("\n"):
        if len(simdi) + len(satir) + 1 > n:
            parca.append(simdi)
            simdi = ""
        simdi += satir + "\n"
    return parca + [simdi] if simdi.strip() else parca


def medya_gonder(token, chat_id, url, baslik, yedek, kuru):
    if kuru:
        print(f"  [medya] {baslik} → {url}")
        return
    uz = url.lower().split("?")[0].rsplit(".", 1)[-1]  # science.nasa.gov görsel linklerinde ?w=... var
    yontem, alan = ("sendVideo", "video") if uz in ("mp4", "webm") else \
                   ("sendAnimation", "animation") if uz == "gif" else ("sendPhoto", "photo")
    c = tg(token, yontem, chat_id=chat_id, **{alan: url}, caption=baslik[:1024])
    if not c.get("ok") and yedek:
        c = tg(token, yontem, chat_id=chat_id, **{alan: yedek}, caption=baslik[:1024])
    if not c.get("ok"):
        tg(token, "sendMessage", chat_id=chat_id, text=f"{baslik}\n{url}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hepsi", action="store_true")
    ap.add_argument("--kuru", action="store_true", help="göndermeden ekrana yaz")
    a = ap.parse_args()

    env = env_oku()
    token, chat_id = env.get("TELEGRAM_TOKEN"), env.get("TELEGRAM_CHAT_ID")
    if not a.kuru and not (token and chat_id):
        raise SystemExit(".env içinde TELEGRAM_TOKEN ve TELEGRAM_CHAT_ID olmalı.")

    klasor = HAM / BUGUN.isoformat()
    klasor.mkdir(parents=True, exist_ok=True)

    kategoriler = {}
    for api in liste_oku(hepsi=a.hepsi):
        if api["anahtar"] == "ücretsiz":
            continue  # anahtarı olmayanları atla
        kategoriler.setdefault(api["kategori"], []).append(api)

    # gün başı: --------------------------25 October 2026----------------------
    ayrac(token, chat_id, f"{'-' * 26}{BUGUN.day} {AYLAR[BUGUN.month - 1]} {BUGUN.year}{'-' * 22}", a.kuru)

    for kategori, apiler in kategoriler.items():
        ad = re.sub(r"^\d+\.\s*", "", kategori)
        emoji = next((e for k, e in EMOJI.items() if ad.startswith(k)), "📌")
        bloklar, medya = [f"{emoji} {ad.replace('i', 'İ').replace('ı', 'I').upper()} — {BUGUN:%d.%m.%Y}"], []
        for api in apiler:
            s = dene(api)
            kaydet(api, s, klasor)
            if durum(s) != "✅":
                bloklar.append(f"\n▪️ {api['ad']}\n⚠️ alınamadı: {s['hata'] or 'HTTP ' + str(s['kod'])}")
                continue
            try:
                satirlar, gorseller = globals().get(f"f_{api['id']}", genel_cikar)(s["govde"])
            except Exception as e:
                satirlar, gorseller = [f"⚠️ veri işlenemedi: {type(e).__name__}: {e}"], []
            if satirlar:
                bloklar.append(f"\n▪️ {api['ad']}\n" + "\n".join(satirlar))
            medya += gorseller

        for parca in parcala("\n".join(bloklar)):
            if a.kuru:
                print(parca)
            else:
                c = tg(token, "sendMessage", chat_id=chat_id, text=parca, disable_web_page_preview=True)
                if not c.get("ok"):
                    print("Telegram hatası:", c.get("description"))
        for url, baslik, yedek in medya:
            medya_gonder(token, chat_id, url, baslik, yedek, a.kuru)
        print(f"{emoji} {ad}: {len(apiler)} API, {len(medya)} görsel" + (" (kuru)" if a.kuru else " gönderildi"))

    ayrac(token, chat_id, "-" * 19, a.kuru)  # gün sonu


if __name__ == "__main__":
    main()
