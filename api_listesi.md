# API Listesi — Günlük Bülten (Faz 1)

**Nasıl düzenlenir:** `[x]` = bültende olsun, `[ ]` = şimdilik olmasın. Satır silebilir, yeni satır ekleyebilirsin.
Satır formatını koru; test betiği bu dosyayı okuyacak:
`- [x] kimlik | Ad | Anahtar | Ön kontrol | Endpoint | Not`

Ön kontrol (27.09.2026, senin bilgisayarından): ✅ yanıt verdi · ⚠️ sorunlu · ❌ erişilemedi · — denenmedi (anahtar gerekiyor)
Anahtar: `yok` · `ücretsiz` (kayıt gerekir) · `DEMO` (anahtarsız da sınırlı çalışır)

---

## 1. Finans
- [x] tcmb_kur | TCMB günlük kurlar | yok | ✅ | https://www.tcmb.gov.tr/kurlar/today.xml | Resmî. XML formatında, hafta sonu bir önceki iş gününün verisi
- [ ] tcmb_evds | TCMB EVDS (tüm seriler) | ücretsiz | — | https://evds2.tcmb.gov.tr | Faiz, enflasyon, rezerv gibi seriler. Tarihsel veri için güçlü
- [ ] frankfurter | Frankfurter (ECB kurları) | yok | ✅ | https://api.frankfurter.dev/v1/latest?from=USD | Çapraz kurlar ve tarihsel veri
- [ ] truncgil | Truncgil Finans (altın, döviz) | yok | ✅ | https://finans.truncgil.com/today.json | Resmî değil. Gram, çeyrek ve cumhuriyet altını
- [ ] coingecko | CoinGecko | yok | ✅ | https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,try&include_24hr_change=true | Kripto fiyatları ve 24 saatlik değişim
- [x] binance | Binance public | yok | ⚠️ | https://api.binance.me/api/v3/ticker/24hr?symbol=BTCUSDT | api.binance.com erişilemedi, .me alan adı çalışıyor. CoinGecko varken gereksiz olabilir
- [ ] yahoo | Yahoo Finance (BIST100, Brent, S&P500) | yok | ✅ | https://query1.finance.yahoo.com/v8/finance/chart/XU100.IS | Resmî değil. Semboller: XU100.IS, BZ=F, ^GSPC, USDTRY=X
- [ ] alphavantage | Alpha Vantage | ücretsiz | — | https://www.alphavantage.co | Günlük istek limiti düşük. Yahoo çalıştığı sürece yedek olarak kalabilir
- [ ] finnhub | Finnhub | ücretsiz | — | https://finnhub.io | Hisse ve şirket haberleri

## 2. Hava & Çevre
- [x] openmeteo | Open-Meteo hava durumu (Ankara) | yok | ✅ | https://api.open-meteo.com/v1/forecast?latitude=39.93&longitude=32.86&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,sunrise,sunset&timezone=Europe/Istanbul | Ankara. Gün doğumu ve batımı da buradan geliyor
- [ ] openmeteo_aq | Open-Meteo hava kalitesi | yok | ✅ | https://air-quality-api.open-meteo.com/v1/air-quality?latitude=39.93&longitude=32.86&current=pm10,pm2_5,european_aqi | PM10, PM2.5, AQI
- [ ] openweather | OpenWeatherMap | ücretsiz | — | https://openweathermap.org/api | Open-Meteo'ya yedek
- [ ] afad | AFAD deprem | yok | ✅ | https://servisnet.afad.gov.tr/apigateway/deprem/apiv2/event/filter?start={dun}T00:00:00&end={bugun}T23:59:59&minmag=3 | Resmî. Adres servisnet alan adına yönlendiriyor
- [x] kandilli | Kandilli (topluluk API'si) | yok | ✅ | https://api.orhanaydogdu.com.tr/deprem/kandilli/live | Resmî değil. AFAD'ın yedeği olarak kullanılabilir
- [ ] usgs | USGS dünya depremleri | yok | ✅ | https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=6&starttime={dun} | Dünyada M6+ depremler
- [ ] tatil | Nager.Date resmî tatiller | yok | ✅ | https://date.nager.at/api/v3/PublicHolidays/2026/TR | "Yaklaşan tatil: X gün kaldı" satırı için

## 3. Akademik
- [x] arxiv_rss | arXiv RSS (kategori bazlı) | yok | ✅ | https://rss.arxiv.org/rss/cs.RO | Günlük yeni makaleler. Kategoriler: cs.RO, physics.app-ph, cond-mat.mtrl-sci
- [x] arxiv_api | arXiv arama API'si | yok | ✅ | https://export.arxiv.org/api/query?search_query=all:%22additive%20manufacturing%22&sortBy=submittedDate&sortOrder=descending&max_results=5 | İlk denemede 406 vermişti, sonra düzeldi. En yeni 5 makale
- [x] openalex | OpenAlex (yeni yayınlar, konu araması) | yok | ✅ | https://api.openalex.org/works?search=wire%20arc%20additive%20manufacturing&filter=from_publication_date:{hafta}&sort=publication_date:desc&per_page=5 | Dergi makaleleri dahil. arXiv aramasının alternatifi
- [x] crossref | Crossref | yok | ✅ | https://api.crossref.org/works?query=additive+manufacturing&filter=from-pub-date:{dun} | DOI metadata. OpenAlex ile büyük ölçüde örtüşüyor
- [ ] hackernews | Hacker News top 10 | yok | ✅ | https://hacker-news.firebaseio.com/v0/topstories.json | Teknoloji gündemi
- [ ] github | GitHub yeni ve popüler repolar | yok | ✅ | https://api.github.com/search/repositories?q=topic:robotics+created:>{hafta}&sort=stars | Anahtarsız kullanımda istek limiti düşük

## 4. Genel
- [x] wiki_bugun | Wikipedia "Bugün tarihte" (TR) | yok | ✅ | https://api.wikimedia.org/feed/v1/wikipedia/tr/onthisday/all/{AA}/{GG} | Türkçe
- [x] nasa_apod | NASA günün astronomi fotoğrafı | yok | ✅ | https://science.nasa.gov/wp-json/wp/v2/apod-basic?per_page=1 | Eski api.nasa.gov/planetary/apod Eylül 2026 sonundan beri 500 veriyor; APOD science.nasa.gov'a taşındı (25.10.2026). Anahtar gerekmiyor. Yanıt liste döner; görsel hdurl'de, url makale sayfası, metinler HTML
- [ ] uzay_haber | Spaceflight News | yok | ✅ | https://api.spaceflightnewsapi.net/v4/articles/?limit=3 | Uzay haberleri
- [ ] roket | Yaklaşan roket fırlatmaları | yok | ✅ | https://ll.thespacedevs.com/2.3.0/launches/upcoming/?limit=3 | Anahtarsız kullanımda saatlik limit var, günde 1 çağrı yeterli
- [ ] iss | Uzaydaki insanlar | yok | ✅ | http://api.open-notify.org/astros.json | Küçük bir bilgi satırı olarak

## 5. Eğlence
- [ ] xkcd | xkcd son çizgi roman | yok | ✅ | https://xkcd.com/info.0.json | Yeni sayı çıktıysa gönderilir
- [x] soz | ZenQuotes günün sözü | yok | ✅ | https://zenquotes.io/api/today | İngilizce
- [x] bilgi | Günün gereksiz bilgisi | yok | ✅ | https://uselessfacts.jsph.pl/api/v2/facts/today | İngilizce
- [ ] saka | JokeAPI | yok | ✅ | https://v2.jokeapi.dev/joke/Programming?safe-mode | Programlama esprileri
- [ ] satranc_lichess | Lichess günün bulmacası | yok | ✅ | https://lichess.org/api/puzzle/daily | Bulmaca linki
- [ ] satranc_chesscom | Chess.com günün bulmacası | yok | ✅ | https://api.chess.com/pub/puzzle | Bulmaca görseli ve linki
- [x] epic | Epic Games ücretsiz oyunlar | yok | ✅ | https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=tr | Resmî değil. Haftalık ücretsiz oyunlar
- [ ] tmdb | TMDB trend filmler ve diziler | ücretsiz | — | https://api.themoviedb.org/3/trending/movie/day | Türkçe başlıklar ve yeni Türk filmleri için filtre yapılabilir
- [ ] kedi_bilgi | Kedi bilgisi (catfact.ninja) | yok | ✅ | https://catfact.ninja/fact | İngilizce. Önerdiğin alexwohlbruck/cat-facts API'si (cat-fact.herokuapp.com) 503 veriyor; aynı işi bu yapıyor
- [x] kopek | Rastgele köpek (random.dog) | yok | ✅ | https://random.dog/woof.json | Görsel veya video linki döner; Telegram'da fotoğraf olarak gönderilebilir
- [x] tilki | Rastgele tilki (randomfox.ca) | yok | ✅ | https://randomfox.ca/floof/ | Görsel linki
- [x] ordek | Rastgele ördek (random-d.uk) | yok | ✅ | https://random-d.uk/api/v2/random | Görsel linki

---

## Elenenler (ön kontrolde çalışmadı)
- Bored API (boredapi.com): kapanmış
- Free Dictionary (dictionaryapi.dev): erişilemedi

## Sonraki fazlar (şimdi değil)
- **Haber:** RSS kaynakları + eski özet projen · GNews / NewsAPI (ücretsiz anahtar)
- **Patent:** EPO OPS (ücretsiz anahtar) · USPTO PatentsView (ücretsiz anahtar) · Google Patents (resmî API'si yok) · TÜRKPATENT (API'si yok, sayfa kazıma gerekir)

## Senin eklemek istediklerin
<!-- Buraya serbestçe yazabilirsin: "akaryakıt fiyatları", "X şehrinin havası", "Y konusundaki makaleler" gibi -->
