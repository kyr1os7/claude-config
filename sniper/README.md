# Social Alpha Scanner

Cari memecoin dari **media sosial**, bukan dari halaman trending.

Premisnya: ada jeda waktu antara *"normie sudah meme-in sesuatu"* dan
*"crypto Twitter sudah men-trading-kannya"*. Jeda itu yang dicari bot ini.

## Pipeline

```
1. HARVEST      Grok + Live Search X → meme/slang/momen viral 1-24 jam terakhir
                di timeline NON-kripto
                                 ↓
2. FILTER       heat cukup tinggi? lintas >=2 komunitas?
                                 ↓
3. SATURATION   panggilan Grok kedua khusus term ini: apakah CT sudah
                menempelkan CA/ticker? kalau sudah ramai → buang
                                 ↓
4. VELOCITY     bandingkan dengan scan sebelumnya (SQLite).
                masih naik atau sudah datar? ← butuh >=2 observasi
                                 ↓
5. DISCOVERY    Dexscreener: sudah ada token dengan nama/ticker itu?
                umur, likuiditas, FDV, tekanan beli
                                 ↓
6. SAFETY       ⛔ BELUM DIPASANG — chain-specific, lihat di bawah
                                 ↓
7. SCORE        gap score 0-100 → alert Telegram
```

## Status

| Modul | Status |
|---|---|
| `core/grok.py` — Live Search X | ✅ |
| `core/scanner.py` — harvest + saturation | ✅ |
| `core/store.py` — velocity & dedup | ✅ |
| `core/discovery.py` — Dexscreener | ✅ chain-agnostic |
| `core/score.py` — gap score | ✅ |
| `core/notify.py` — Telegram | ✅ |
| `core/safety.py` — rug/honeypot | ⛔ stub |
| eksekusi trade (buy/sell) | ⛔ belum |

Sekarang bot ini **alert-only**: dia mengirim sinyal, tidak memegang uang.
Itu disengaja — jalankan mode ini dulu beberapa hari dan nilai kualitas
sinyalnya sebelum menyambungkan dompet.

## Adverse selection — baca ini sebelum lanjut

Saat kamu menemukan token yang cocok dengan meme viral, di banyak kasus
token itu dibuat oleh orang yang melihat meme yang sama. Sebagian dari
mereka adalah deployer serial yang menembak 50 term trending sekaligus dan
menunggu justru bot seperti ini yang membeli.

Artinya: "gap" yang kamu masuki sering kali **jebakan yang sengaja
dipasang**. Filter keamanan di langkah 6 bukan pelengkap — di strategi ini
justru di situ sebagian besar edge-nya berada. Bot tanpa langkah 6 akan
menemukan meme dengan benar dan tetap kehilangan uang.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env      # isi XAI_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
python run.py --once      # satu siklus, buat tes
python run.py             # loop sesuai config.yaml
```

Butuh API key berbayar dari https://console.x.ai (terpisah dari X Premium).
Nama model terbaru cek di https://docs.x.ai/docs/models — `config.yaml`
default ke `grok-4`.

## Tuning

Semua ambang ada di `config.yaml`. Yang paling menentukan:

- `max_crypto_saturation` (default 35) — gerbang utama. Turunkan agar lebih
  selektif, naikkan kalau alert terlalu jarang.
- `interval_minutes` (default 20) — jangan lebih dari 30; velocity butuh
  beberapa observasi sebelum meme-nya keburu basi.
- `max_pair_age_hours` (default 24) — token lebih tua dari ini bukan lagi gap.

## Biaya

Tiap siklus = 2 panggilan Grok dengan Live Search per kandidat yang lolos
filter awal. Live Search ditagih per sumber yang diambil, bukan hanya per
token. Interval 20 menit = 72 siklus/hari. Pantau tagihan di hari pertama
sebelum membiarkannya jalan terus.
