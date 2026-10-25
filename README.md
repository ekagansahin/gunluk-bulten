# Günlük API Bülteni

Kişisel kullanım için: seçili açık API'lerden veriyi her sabah çekip Telegram botuna gönderir.

| Dosya | Görev |
|---|---|
| `api_listesi.md` | API'ler ve seçimler (`[x]` = bültende) |
| `bulten.py` | Bülteni oluşturup kategori kategori Telegram'a gönderir (`--hepsi`, `--kuru`) |
| `api_test.py` | API'leri test eder, `api_katalog.md` raporunu yazar |
| `.github/workflows/bulten.yml` | Her gün 07:20 TSİ'de GitHub Actions ile çalıştırır |

Gerekli anahtarlar (yerelde `.env`, GitHub'da Settings → Secrets → Actions):
`TELEGRAM_TOKEN`, `TELEGRAM_CHAT_ID`

NASA APOD artık science.nasa.gov üzerinden anahtarsız çekiliyor; `NASA_API_KEY` gerekmiyor.
