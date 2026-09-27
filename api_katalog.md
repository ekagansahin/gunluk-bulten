# API Kataloğu — test sonuçları

Son test: 27.09.2026 20:03 · 34/39 API çalıştı

| Durum | Kimlik | Ad | Kategori | HTTP | Süre | Boyut | Tip |
|---|---|---|---|---|---|---|---|
| ✅ | `tcmb_kur` | TCMB günlük kurlar | 1. Finans | 200 | 0.1 sn | 8.9 KB | application/xml |
| ❌ | `tcmb_evds` | TCMB EVDS (tüm seriler) | 1. Finans | - | 0.0 sn | 0.0 KB | - |
| ✅ | `frankfurter` | Frankfurter (ECB kurları) | 1. Finans | 200 | 0.2 sn | 0.4 KB | application/json |
| ✅ | `truncgil` | Truncgil Finans (altın, döviz) | 1. Finans | 200 | 0.1 sn | 6.9 KB | application/json |
| ✅ | `coingecko` | CoinGecko | 1. Finans | 200 | 0.4 sn | 0.2 KB | application/json |
| ✅ | `binance` | Binance public | 1. Finans | 200 | 0.3 sn | 0.5 KB | application/json |
| ✅ | `yahoo` | Yahoo Finance (BIST100, Brent, S&P500) | 1. Finans | 200 | 0.3 sn | 37.4 KB | application/json |
| ❌ | `alphavantage` | Alpha Vantage | 1. Finans | - | 0.0 sn | 0.0 KB | - |
| ❌ | `finnhub` | Finnhub | 1. Finans | - | 0.0 sn | 0.0 KB | - |
| ✅ | `openmeteo` | Open-Meteo hava durumu | 2. Hava & Çevre | 200 | 0.2 sn | 0.9 KB | application/json |
| ✅ | `openmeteo_aq` | Open-Meteo hava kalitesi | 2. Hava & Çevre | 200 | 0.3 sn | 0.4 KB | application/json |
| ❌ | `openweather` | OpenWeatherMap | 2. Hava & Çevre | - | 0.0 sn | 0.0 KB | - |
| ✅ | `afad` | AFAD deprem | 2. Hava & Çevre | 200 | 0.1 sn | 0.0 KB | application/json |
| ✅ | `kandilli` | Kandilli (topluluk API'si) | 2. Hava & Çevre | 200 | 0.3 sn | 56.2 KB | application/json |
| ✅ | `usgs` | USGS dünya depremleri | 2. Hava & Çevre | 200 | 0.3 sn | 0.2 KB | application/json |
| ✅ | `tatil` | Nager.Date resmî tatiller | 2. Hava & Çevre | 200 | 0.2 sn | 2.6 KB | application/json |
| ✅ | `arxiv_rss` | arXiv RSS (kategori bazlı) | 3. Akademik | 200 | 0.2 sn | 0.9 KB | application/rss+xml |
| ✅ | `arxiv_api` | arXiv arama API'si | 3. Akademik | 200 | 0.5 sn | 23.0 KB | application/atom+xml |
| ✅ | `openalex` | OpenAlex (yeni yayınlar, konu araması) | 3. Akademik | 200 | 0.5 sn | 0.6 KB | application/json |
| ✅ | `crossref` | Crossref | 3. Akademik | 200 | 0.8 sn | 400.1 KB | application/json |
| ✅ | `hackernews` | Hacker News top 10 | 3. Akademik | 200 | 0.5 sn | 4.4 KB | application/json |
| ✅ | `github` | GitHub yeni ve popüler repolar | 3. Akademik | 200 | 0.9 sn | 171.0 KB | application/json |
| ✅ | `wiki_bugun` | Wikipedia "Bugün tarihte" (TR) | 4. Genel | 200 | 0.5 sn | 653.1 KB | application/json |
| ✅ | `nasa_apod` | NASA günün astronomi fotoğrafı | 4. Genel | 200 | 1.1 sn | 1.4 KB | application/json |
| ✅ | `uzay_haber` | Spaceflight News | 4. Genel | 200 | 0.6 sn | 2.4 KB | application/json |
| ✅ | `roket` | Yaklaşan roket fırlatmaları | 4. Genel | 200 | 1.3 sn | 48.3 KB | application/json |
| ✅ | `iss` | Uzaydaki insanlar | 4. Genel | 200 | 0.4 sn | 0.6 KB | application/json |
| ✅ | `xkcd` | xkcd son çizgi roman | 5. Eğlence | 200 | 0.3 sn | 0.4 KB | application/json |
| ✅ | `soz` | ZenQuotes günün sözü | 5. Eğlence | 200 | 0.4 sn | 0.3 KB | application/json |
| ✅ | `bilgi` | Günün gereksiz bilgisi | 5. Eğlence | 200 | 0.2 sn | 0.3 KB | application/json |
| ✅ | `saka` | JokeAPI | 5. Eğlence | 200 | 0.3 sn | 0.4 KB | application/json |
| ✅ | `satranc_lichess` | Lichess günün bulmacası | 5. Eğlence | 200 | 0.2 sn | 0.7 KB | application/json |
| ✅ | `satranc_chesscom` | Chess.com günün bulmacası | 5. Eğlence | 200 | 0.3 sn | 0.5 KB | application/json |
| ✅ | `epic` | Epic Games ücretsiz oyunlar | 5. Eğlence | 200 | 0.5 sn | 43.4 KB | application/json |
| ❌ | `tmdb` | TMDB trend filmler ve diziler | 5. Eğlence | - | 0.0 sn | 0.0 KB | - |
| ✅ | `kedi_bilgi` | Kedi bilgisi (catfact.ninja) | 5. Eğlence | 200 | 0.3 sn | 0.2 KB | application/json |
| ✅ | `kopek` | Rastgele köpek (random.dog) | 5. Eğlence | 200 | 0.7 sn | 0.1 KB | application/json |
| ✅ | `tilki` | Rastgele tilki (randomfox.ca) | 5. Eğlence | 200 | 0.8 sn | 0.1 KB | application/json |
| ✅ | `ordek` | Rastgele ördek (random-d.uk) | 5. Eğlence | 200 | 0.3 sn | 0.1 KB | application/json |

## ✅ tcmb_kur — TCMB günlük kurlar

- URL: `https://www.tcmb.gov.tr/kurlar/today.xml`
- Anahtar: yok
- Not: Resmî. XML formatında, hafta sonu bir önceki iş gününün verisi
- Ham yanıt: `ham/2026-09-27/tcmb_kur.xml`

```
<?xml version="1.0" encoding="UTF-8"?> <?xml-stylesheet type="text/xsl" href="isokur.xsl"?> <Tarih_Date Tarih="25.09.2026" Date="09/25/2026" Bulten_No="2026/181" > <Currency CrossOrder="0" Kod="USD" CurrencyCode="USD"> <Unit>1</Unit> <Isim>ABD DOLARI</Isim> <CurrencyName>US DOLLAR</CurrencyName> <ForexBuying>48.7901</ForexBuying> <ForexSelling>48.8780</ForexSelling> <BanknoteBuying>48.7560</Bankno
```

## ❌ tcmb_evds — TCMB EVDS (tüm seriler)

- URL: `https://evds2.tcmb.gov.tr`
- Anahtar: ücretsiz
- Not: Faiz, enflasyon, rezerv gibi seriler. Tarihsel veri için güçlü
- Hata: Anahtar gerekiyor; henüz eklenmedi, atlandı

## ✅ frankfurter — Frankfurter (ECB kurları)

- URL: `https://api.frankfurter.dev/v1/latest?from=USD`
- Anahtar: yok
- Not: Çapraz kurlar ve tarihsel veri
- Ham yanıt: `ham/2026-09-27/frankfurter.json`

```
anahtarlar: amount, base, date, rates
{"amount": 1.0, "base": "USD", "date": "2026-09-25", "rates": {"AUD": 1.4224, "BRL": 5.1821, "CAD": 1.4143, "CHF": 0.82829, "CNY": 6.7132, "CZK": 21.35, "DKK": 6.5557, "EUR": 0.87696, "GBP": 0.75458, "HKD": 7.844, "HUF": 320.34, "IDR": 17914, "ILS": 3.0338, "INR": 95.82, "ISK": 119.79, "JPY": 157.59, "KRW": 1355.05, "MXN": 17.6989, "MYR": 4.074, "N
```

## ✅ truncgil — Truncgil Finans (altın, döviz)

- URL: `https://finans.truncgil.com/today.json`
- Anahtar: yok
- Not: Resmî değil. Gram, çeyrek ve cumhuriyet altını
- Ham yanıt: `ham/2026-09-27/truncgil.json`

```
anahtarlar: Update_Date, USD, EUR, GBP, CHF, CAD, RUB, AED, AUD, DKK, SEK, NOK
{"Update_Date": "2026-09-27 23:00:03", "USD": {"Alış": "48,8471", "Tür": "Döviz", "Satış": "49,0139", "Değişim": "%0,12"}, "EUR": {"Alış": "55,3999", "Tür": "Döviz", "Satış": "56,1125", "Değişim": "%0,06"}, "GBP": {"Alış": "64,3746", "Tür": "Döviz", "Satış": "65,2519", "Değişim": "%0,15"}, "CHF": {"Alış": "58,9585", "Tür": "Döviz", "Satış": "59,188
```

## ✅ coingecko — CoinGecko

- URL: `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,try&include_24hr_change=true`
- Anahtar: yok
- Not: Kripto fiyatları ve 24 saatlik değişim
- Ham yanıt: `ham/2026-09-27/coingecko.json`

```
anahtarlar: bitcoin, ethereum
{"bitcoin": {"try": 4146910, "try_24h_change": 0.8531453566207563, "usd": 84730, "usd_24h_change": 0.8531453566207597}, "ethereum": {"try": 131750, "try_24h_change": 0.2997377245122334, "usd": 2691.94, "usd_24h_change": 0.299737724512244}}
```

## ✅ binance — Binance public

- URL: `https://api.binance.me/api/v3/ticker/24hr?symbol=BTCUSDT`
- Anahtar: yok
- Not: api.binance.com erişilemedi, .me alan adı çalışıyor. CoinGecko varken gereksiz olabilir
- Ham yanıt: `ham/2026-09-27/binance.json`

```
anahtarlar: symbol, priceChange, priceChangePercent, weightedAvgPrice, prevClosePrice, lastPrice, lastQty, bidPrice, bidQty, askPrice, askQty, openPrice
{"symbol": "BTCUSDT", "priceChange": "723.45000000", "priceChangePercent": "0.861", "weightedAvgPrice": "84615.38870641", "prevClosePrice": "84042.43000000", "lastPrice": "84765.87000000", "lastQty": "0.00146000", "bidPrice": "84765.87000000", "bidQty": "8.27239000", "askPrice": "84765.88000000", "askQty": "0.23391000", "openPrice": "84042.42000000
```

## ✅ yahoo — Yahoo Finance (BIST100, Brent, S&P500)

- URL: `https://query1.finance.yahoo.com/v8/finance/chart/XU100.IS`
- Anahtar: yok
- Not: Resmî değil. Semboller: XU100.IS, BZ=F, ^GSPC, USDTRY=X
- Ham yanıt: `ham/2026-09-27/yahoo.json`

```
anahtarlar: chart
{"chart": {"result": [{"meta": {"currency": "TRY", "symbol": "XU100.IS", "exchangeName": "IST", "fullExchangeName": "Istanbul", "instrumentType": "INDEX", "firstTradeDate": 867738600, "regularMarketTime": 1790349011, "hasPrePostMarketData": false, "gmtoffset": 10800, "timezone": "TRT", "exchangeTimezoneName": "Europe/Istanbul", "regularMarketPrice"
```

## ❌ alphavantage — Alpha Vantage

- URL: `https://www.alphavantage.co`
- Anahtar: ücretsiz
- Not: Günlük istek limiti düşük. Yahoo çalıştığı sürece yedek olarak kalabilir
- Hata: Anahtar gerekiyor; henüz eklenmedi, atlandı

## ❌ finnhub — Finnhub

- URL: `https://finnhub.io`
- Anahtar: ücretsiz
- Not: Hisse ve şirket haberleri
- Hata: Anahtar gerekiyor; henüz eklenmedi, atlandı

## ✅ openmeteo — Open-Meteo hava durumu

- URL: `https://api.open-meteo.com/v1/forecast?latitude=39.93&longitude=32.86&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,sunrise,sunset&timezone=Europe/Istanbul`
- Anahtar: yok
- Not: Ankara. Gün doğumu ve batımı da buradan geliyor
- Ham yanıt: `ham/2026-09-27/openmeteo.json`

```
anahtarlar: latitude, longitude, generationtime_ms, utc_offset_seconds, timezone, timezone_abbreviation, elevation, daily_units, daily
{"latitude": 39.9375, "longitude": 32.875, "generationtime_ms": 0.10609626770019531, "utc_offset_seconds": 10800, "timezone": "Europe/Istanbul", "timezone_abbreviation": "GMT+3", "elevation": 870.0, "daily_units": {"time": "iso8601", "temperature_2m_max": "°C", "temperature_2m_min": "°C", "precipitation_probability_max": "%", "sunrise": "iso8601", 
```

## ✅ openmeteo_aq — Open-Meteo hava kalitesi

- URL: `https://air-quality-api.open-meteo.com/v1/air-quality?latitude=39.93&longitude=32.86&current=pm10,pm2_5,european_aqi`
- Anahtar: yok
- Not: PM10, PM2.5, AQI
- Ham yanıt: `ham/2026-09-27/openmeteo_aq.json`

```
anahtarlar: latitude, longitude, generationtime_ms, utc_offset_seconds, timezone, timezone_abbreviation, elevation, current_units, current
{"latitude": 39.9, "longitude": 32.9, "generationtime_ms": 0.23829936981201172, "utc_offset_seconds": 0, "timezone": "GMT", "timezone_abbreviation": "GMT", "elevation": 870.0, "current_units": {"time": "iso8601", "interval": "seconds", "pm10": "μg/m³", "pm2_5": "μg/m³", "european_aqi": "EAQI"}, "current": {"time": "2026-09-27T20:00", "interval": 36
```

## ❌ openweather — OpenWeatherMap

- URL: `https://openweathermap.org/api`
- Anahtar: ücretsiz
- Not: Open-Meteo'ya yedek
- Hata: Anahtar gerekiyor; henüz eklenmedi, atlandı

## ✅ afad — AFAD deprem

- URL: `https://servisnet.afad.gov.tr/apigateway/deprem/apiv2/event/filter?start={dun}T00:00:00&end={bugun}T23:59:59&minmag=3`
- Anahtar: yok
- Not: Resmî. Adres servisnet alan adına yönlendiriyor
- Ham yanıt: `ham/2026-09-27/afad.json`

```
boş liste
```

## ✅ kandilli — Kandilli (topluluk API'si)

- URL: `https://api.orhanaydogdu.com.tr/deprem/kandilli/live`
- Anahtar: yok
- Not: Resmî değil. AFAD'ın yedeği olarak kullanılabilir
- Ham yanıt: `ham/2026-09-27/kandilli.json`

```
anahtarlar: status, httpStatus, desc, serverloadms, metadata, result
{"status": true, "httpStatus": 200, "desc": "", "serverloadms": 0, "metadata": {"date_starts": "2026-09-26 23:03:33", "date_ends": "2026-09-27 23:03:33", "count": 47}, "result": [{"earthquake_id": "oaOl1LxXNfowk", "provider": "kandilli", "title": "HAMZALAR-TEKMAN (ERZURUM)", "mag": 1.4, "depth": 7.6, "geojson": {"type": "Point", "coordinates": [41.
```

## ✅ usgs — USGS dünya depremleri

- URL: `https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=6&starttime={dun}`
- Anahtar: yok
- Not: Dünyada M6+ depremler
- Ham yanıt: `ham/2026-09-27/usgs.json`

```
anahtarlar: type, metadata, features
{"type": "FeatureCollection", "metadata": {"generated": 1790539414000, "url": "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=6&starttime=2026-09-26", "title": "USGS Earthquakes", "status": 200, "api": "2.7.0", "count": 0}, "features": []}
```

## ✅ tatil — Nager.Date resmî tatiller

- URL: `https://date.nager.at/api/v3/PublicHolidays/2026/TR`
- Anahtar: yok
- Not: "Yaklaşan tatil: X gün kaldı" satırı için
- Ham yanıt: `ham/2026-09-27/tatil.json`

```
liste[14], ilk öğe: {"date": "2026-01-01", "localName": "Yılbaşı", "name": "New Year's Day", "countryCode": "TR", "fixed": false, "global": true, "counties": null, "launchYear": null, "types": ["Public"]}
```

## ✅ arxiv_rss — arXiv RSS (kategori bazlı)

- URL: `https://rss.arxiv.org/rss/cs.RO`
- Anahtar: yok
- Not: Günlük yeni makaleler. Kategoriler: cs.RO, physics.app-ph, cond-mat.mtrl-sci
- Ham yanıt: `ham/2026-09-27/arxiv_rss.xml`

```
<?xml version='1.0' encoding='UTF-8'?> <rss xmlns:arxiv="http://arxiv.org/schemas/atom" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0"> <channel> <title>cs.RO updates on arXiv.org</title> <link>http://rss.arxiv.org/rss/cs.RO</link> <description>cs.RO updates on the arXiv.org e-print archive
```

## ✅ arxiv_api — arXiv arama API'si

- URL: `https://export.arxiv.org/api/query?search_query=all:%22wire%20arc%20additive%22`
- Anahtar: yok
- Not: Şu an 406 döndürüyor. Anahtar kelime araması için gerekli; test betiğinde tekrar deneyeceğiz
- Ham yanıt: `ham/2026-09-27/arxiv_api.xml`

```
<?xml version='1.0' encoding='UTF-8'?> <feed xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:arxiv="http://arxiv.org/schemas/atom" xmlns="http://www.w3.org/2005/Atom"> <id>https://arxiv.org/api/9m9k4Wv7AR/NIWvEkA8nx3m3BY4</id> <title>arXiv Query: search_query=all:"wire arc additive"&amp;id_list=&amp;start=0&amp;max_results=10</title> <updated>2026-09-27T20:03:35Z</updated> <link href
```

## ✅ openalex — OpenAlex (yeni yayınlar, konu araması)

- URL: `https://api.openalex.org/works?search=wire%20arc%20additive%20manufacturing&filter=from_publication_date:{dun}`
- Anahtar: yok
- Not: Dergi makaleleri dahil. arXiv aramasının alternatifi
- Ham yanıt: `ham/2026-09-27/openalex.json`

```
anahtarlar: meta, results, group_by
{"meta": {"count": 0, "db_response_time_ms": 102, "page": 1, "per_page": 25, "groups_count": null, "x_query": {"oql": "works where date >= (2026-09-26)\n  and full text has (wire arc additive manufacturing)", "oqo": {"get_rows": "works", "filter_rows": [{"column_id": "from_publication_date", "value": "2026-09-26"}, {"column_id": "fulltext.search", 
```

## ✅ crossref — Crossref

- URL: `https://api.crossref.org/works?query=additive+manufacturing&filter=from-pub-date:{dun}`
- Anahtar: yok
- Not: DOI metadata. OpenAlex ile büyük ölçüde örtüşüyor
- Ham yanıt: `ham/2026-09-27/crossref.json`

```
anahtarlar: status, message-type, message-version, message
{"status": "ok", "message-type": "work-list", "message-version": "1.0.0", "message": {"facets": {}, "total-results": 2010, "items": [{"indexed": {"date-parts": [[2026, 9, 23]], "date-time": "2026-09-23T10:03:09Z", "timestamp": 1790157789304, "version": "4.1.0"}, "reference-count": 34, "publisher": "Elsevier BV", "license": [{"start": {"date-parts":
```

## ✅ hackernews — Hacker News top 10

- URL: `https://hacker-news.firebaseio.com/v0/topstories.json`
- Anahtar: yok
- Not: Teknoloji gündemi
- Ham yanıt: `ham/2026-09-27/hackernews.json`

```
liste[500], ilk öğe: 49868830
```

## ✅ github — GitHub yeni ve popüler repolar

- URL: `https://api.github.com/search/repositories?q=topic:robotics+created:>{hafta}&sort=stars`
- Anahtar: yok
- Not: Anahtarsız kullanımda istek limiti düşük
- Ham yanıt: `ham/2026-09-27/github.json`

```
anahtarlar: total_count, incomplete_results, items
{"total_count": 325, "incomplete_results": false, "items": [{"id": 1380792716, "node_id": "R_kgDOUk05jA", "name": "Grounded-Action-Model", "full_name": "GehaoZhang6/Grounded-Action-Model", "private": false, "owner": {"login": "GehaoZhang6", "id": 143525327, "node_id": "U_kgDOCI4Fzw", "avatar_url": "https://avatars.githubusercontent.com/u/143525327?
```

## ✅ wiki_bugun — Wikipedia "Bugün tarihte" (TR)

- URL: `https://api.wikimedia.org/feed/v1/wikipedia/tr/onthisday/all/{AA}/{GG}`
- Anahtar: yok
- Not: Türkçe
- Ham yanıt: `ham/2026-09-27/wiki_bugun.json`

```
anahtarlar: selected, births, deaths, events, holidays
{"selected": [{"text": "İkinci Dağlık Karabağ Savaşı başladı.", "pages": [{"type": "standard", "title": "İkinci_Dağlık_Karabağ_Savaşı", "displaytitle": "<span lang=\"tr\" dir=\"ltr\"><span class=\"mw-page-title-main\">İkinci Dağlık Karabağ Savaşı</span></span>", "namespace": {"id": 0, "text": ""}, "wikibase_item": "Q99659280", "titles": {"canonical
```

## ✅ nasa_apod — NASA günün astronomi fotoğrafı

- URL: `https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}`
- Anahtar: .env: NASA_API_KEY
- Not: Kendi anahtarınla çalışıyor. Görsel Telegram'da fotoğraf olarak gönderilebilir
- Ham yanıt: `ham/2026-09-27/nasa_apod.json`

```
anahtarlar: date, explanation, hdurl, media_type, service_version, title, url
{"date": "2026-09-27", "explanation": "What does the Andromeda galaxy really look like? The featured image shows how our Milky Way Galaxy's closest major galactic neighbor really appears in a long exposure through Earth's busy skies and with a digital camera that introduces normal imperfections.  The picture is a stack of 223 images, each a 300 sec
```

## ✅ uzay_haber — Spaceflight News

- URL: `https://api.spaceflightnewsapi.net/v4/articles/?limit=3`
- Anahtar: yok
- Not: Uzay haberleri
- Ham yanıt: `ham/2026-09-27/uzay_haber.json`

```
anahtarlar: count, next, previous, results
{"count": 36225, "next": "https://api.spaceflightnewsapi.net/v4/articles/?limit=3&offset=3", "previous": null, "results": [{"id": 40112, "title": "Starship Flight 14: SpaceX Attempts Orbit", "authors": [{"name": "Ryan Weber", "socials": null}], "url": "https://www.nasaspaceflight.com/2026/09/starship-flight-14-orbit/", "image_url": "https://www.nas
```

## ✅ roket — Yaklaşan roket fırlatmaları

- URL: `https://ll.thespacedevs.com/2.3.0/launches/upcoming/?limit=3`
- Anahtar: yok
- Not: Anahtarsız kullanımda saatlik limit var, günde 1 çağrı yeterli
- Ham yanıt: `ham/2026-09-27/roket.json`

```
anahtarlar: count, next, previous, results
{"count": 367, "next": "https://ll.thespacedevs.com/2.3.0/launches/upcoming/?limit=3&offset=3", "previous": null, "results": [{"id": "7d1afb26-6f9c-429b-9ccf-29012fd1e519", "url": "https://ll.thespacedevs.com/2.3.0/launches/7d1afb26-6f9c-429b-9ccf-29012fd1e519/", "name": "Starship | Starlink Group 31-1 (Starship Flight 14)", "response_mode": "norma
```

## ✅ iss — Uzaydaki insanlar

- URL: `http://api.open-notify.org/astros.json`
- Anahtar: yok
- Not: Küçük bir bilgi satırı olarak
- Ham yanıt: `ham/2026-09-27/iss.json`

```
anahtarlar: people, number, message
{"people": [{"craft": "ISS", "name": "Oleg Kononenko"}, {"craft": "ISS", "name": "Nikolai Chub"}, {"craft": "ISS", "name": "Tracy Caldwell Dyson"}, {"craft": "ISS", "name": "Matthew Dominick"}, {"craft": "ISS", "name": "Michael Barratt"}, {"craft": "ISS", "name": "Jeanette Epps"}, {"craft": "ISS", "name": "Alexander Grebenkin"}, {"craft": "ISS", "n
```

## ✅ xkcd — xkcd son çizgi roman

- URL: `https://xkcd.com/info.0.json`
- Anahtar: yok
- Not: Yeni sayı çıktıysa gönderilir
- Ham yanıt: `ham/2026-09-27/xkcd.json`

```
anahtarlar: month, num, link, year, news, safe_title, transcript, alt, img, title, day
{"month": "9", "num": 3303, "link": "", "year": "2026", "news": "", "safe_title": "Slab Graveyard", "transcript": "", "alt": "It's ok if you want to close close your eyes for the slab graveyard, so you can still have fun riding the mantle plume back up afterward!", "img": "https://imgs.xkcd.com/comics/slab_graveyard.png", "title": "Slab Graveyard",
```

## ✅ soz — ZenQuotes günün sözü

- URL: `https://zenquotes.io/api/today`
- Anahtar: yok
- Not: İngilizce
- Ham yanıt: `ham/2026-09-27/soz.json`

```
liste[1], ilk öğe: {"q": "Don't let your learning lead to knowledge. Let your learning lead to action.", "a": "Jim Rohn", "i": "https://zenquotes.io/img/jim-rohn.jpg", "h": "<blockquote>&ldquo;Don&#039;t let your learning lead to knowledge. Let your learning lead to action.&rdquo; &mdash; <footer>Jim Rohn</footer></blockquote>", "date": "2026-09-27"}
```

## ✅ bilgi — Günün gereksiz bilgisi

- URL: `https://uselessfacts.jsph.pl/api/v2/facts/today`
- Anahtar: yok
- Not: İngilizce
- Ham yanıt: `ham/2026-09-27/bilgi.json`

```
anahtarlar: id, text, source, source_url, language, permalink
{"id": "549e6e907701e62e3231d5d51a879675", "text": "Your stomach needs to produce a new layer of mucus every two weeks or it would digest itself.", "source": "djtech.net", "source_url": "https://www.djtech.net/humor/shorty_useless_facts.htm", "language": "en", "permalink": "https://uselessfacts.jsph.pl/api/v2/facts/549e6e907701e62e3231d5d51a879675"
```

## ✅ saka — JokeAPI

- URL: `https://v2.jokeapi.dev/joke/Programming?safe-mode`
- Anahtar: yok
- Not: Programlama esprileri
- Ham yanıt: `ham/2026-09-27/saka.json`

```
anahtarlar: error, category, type, joke, flags, id, safe, lang
{"error": false, "category": "Programming", "type": "single", "joke": "Debugging: Removing the needles from the haystack.", "flags": {"nsfw": false, "religious": false, "political": false, "racist": false, "sexist": false, "explicit": false}, "id": 40, "safe": true, "lang": "en"}
```

## ✅ satranc_lichess — Lichess günün bulmacası

- URL: `https://lichess.org/api/puzzle/daily`
- Anahtar: yok
- Not: Bulmaca linki
- Ham yanıt: `ham/2026-09-27/satranc_lichess.json`

```
anahtarlar: game, puzzle
{"game": {"id": "2ih7Pi5Y", "perf": {"key": "blitz", "name": "Blitz"}, "rated": true, "players": [{"name": "DrSimon", "id": "drsimon", "color": "white", "rating": 1777}, {"name": "dmirschi", "id": "dmirschi", "color": "black", "rating": 1809}], "pgn": "e4 c5 Nf3 Nc6 d4 cxd4 Nxd4 Nf6 Nc3 e5 Ndb5 d6 Bg5 a6 Na3 b5 Nd5 Qa5+ Bd2 Qd8 Nxf6+ Qxf6 Be3 Qg6 f
```

## ✅ satranc_chesscom — Chess.com günün bulmacası

- URL: `https://api.chess.com/pub/puzzle`
- Anahtar: yok
- Not: Bulmaca görseli ve linki
- Ham yanıt: `ham/2026-09-27/satranc_chesscom.json`

```
anahtarlar: title, url, publish_time, fen, pgn, image
{"title": "Major Piece Trampoline", "url": "https://www.chess.com/daily/2026-09-27", "publish_time": 1790492400, "fen": "6rk/1p2n2p/P1N1pp2/3p1p1P/3P4/BQRBP3/1P5q/2R1K3 b - - 0 27", "pgn": "[White \"Daily Puzzle Inspiration\"]\n[Black \"Checkmatemaster7\"]\n[Result \"*\"]\n[FEN \"6rk/1p2n2p/P1N1pp2/3p1p1P/3P4/BQRBP3/1P5q/2R1K3 b - - 0 27\"]\n\n27..
```

## ✅ epic — Epic Games ücretsiz oyunlar

- URL: `https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=tr`
- Anahtar: yok
- Not: Resmî değil. Haftalık ücretsiz oyunlar
- Ham yanıt: `ham/2026-09-27/epic.json`

```
anahtarlar: data
{"data": {"Catalog": {"searchStore": {"elements": [{"title": "Them's Fightin' Herds", "id": "1f723b00df58467998c4984ca39915ad", "namespace": "a567c32599bf4d4fb609e424f3691b39", "description": "Them's Fightin' Herds", "effectiveDate": "2022-12-19T16:00:00.000Z", "offerType": "BASE_GAME", "expiryDate": null, "viewableDate": "2022-12-19T15:55:00.000Z"
```

## ❌ tmdb — TMDB trend filmler ve diziler

- URL: `https://api.themoviedb.org/3/trending/movie/day`
- Anahtar: ücretsiz
- Not: Türkçe başlıklar ve yeni Türk filmleri için filtre yapılabilir
- Hata: Anahtar gerekiyor; henüz eklenmedi, atlandı

## ✅ kedi_bilgi — Kedi bilgisi (catfact.ninja)

- URL: `https://catfact.ninja/fact`
- Anahtar: yok
- Not: İngilizce. Önerdiğin alexwohlbruck/cat-facts API'si (cat-fact.herokuapp.com) 503 veriyor; aynı işi bu yapıyor
- Ham yanıt: `ham/2026-09-27/kedi_bilgi.json`

```
anahtarlar: fact, length
{"fact": "Cats have individual preferences for scratching surfaces and angles. Some are horizontal scratchers while others exercise their claws vertically.", "length": 145}
```

## ✅ kopek — Rastgele köpek (random.dog)

- URL: `https://random.dog/woof.json`
- Anahtar: yok
- Not: Görsel veya video linki döner; Telegram'da fotoğraf olarak gönderilebilir
- Ham yanıt: `ham/2026-09-27/kopek.json`

```
anahtarlar: fileSizeBytes, url
{"fileSizeBytes": 67107, "url": "https://random.dog/e9c94b72-4f92-4d65-b43a-e6decf24976f.jpg"}
```

## ✅ tilki — Rastgele tilki (randomfox.ca)

- URL: `https://randomfox.ca/floof/`
- Anahtar: yok
- Not: Görsel linki
- Ham yanıt: `ham/2026-09-27/tilki.json`

```
anahtarlar: image, link
{"image": "https://randomfox.ca/images/55.jpg", "link": "https://randomfox.ca/?i=55"}
```

## ✅ ordek — Rastgele ördek (random-d.uk)

- URL: `https://random-d.uk/api/v2/random`
- Anahtar: yok
- Not: Görsel linki
- Ham yanıt: `ham/2026-09-27/ordek.json`

```
anahtarlar: message, url
{"message": "Powered by random-d.uk", "url": "http://random-d.uk/api/113.jpg"}
```
