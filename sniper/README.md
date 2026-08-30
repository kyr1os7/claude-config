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
| `core/safety.py` — Solana rug check | ✅ |
| `core/paper.py` — paper trading + PnL | ✅ |
| eksekusi trade nyata (buy/sell) | ⛔ sengaja belum |

Bot ini **alert-only**: mengirim sinyal dan mencatat trade hipotetis, tidak
memegang uang. Jalankan begini dulu ~seminggu, lalu `python run.py --stats`.
Kalau win-rate-nya tidak meyakinkan di uang bohongan, dia juga tidak akan
meyakinkan di uang asli.

## Safety check (Solana)

Dua lapis, dan **fail-closed** — kalau pengecekan gagal, token ditolak:

1. **RPC Solana langsung** — `mintAuthority` dan `freezeAuthority` wajib sudah
   dilepas. Ini fakta on-chain yang otoritatif: kalau mint authority masih
   hidup, dev bisa mencetak suplai tak terbatas kapan saja.
2. **rugcheck.xyz** — LP terkunci ≥80%, holder terbesar ≤15%, top-10 ≤40%,
   plus risiko level danger. Alamat burn dan pool LP dikecualikan dari hitungan
   konsentrasi supaya tidak salah tuduh.

Token yang gagal ditandai `blacklist` dan tidak akan di-alert lagi.

## Paper trading

Setiap alert yang lolos safety membuka posisi hipotetis, lalu dilacak tiap
5 menit sampai kena take-profit (5x), stop-loss (-50%), atau time-stop (3 jam).

Biaya dimodelkan: slippage 3% di sisi masuk **dan** keluar, plus fee per sisi.
Jadi TP 5x tercatat sebagai 4.70x bersih, bukan 5.00x. Ini yang membuat angkanya
jujur — perhatikan bahwa screenshot bot yang beredar tidak memperhitungkan
satu pun dari ini.

```bash
python run.py --stats    # closed / win rate / kumulatif SOL / posisi terbuka
```

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
python verify.py          # WAJIB — lihat catatan di bawah
python run.py --once      # satu siklus, buat tes
python run.py             # loop
```

### Jalankan `verify.py` lebih dulu

Kode ini ditulis di lingkungan yang egress-nya diblokir, jadi bentuk respons
Dexscreener, rugcheck, dan xAI **belum pernah diuji terhadap endpoint asli**.
`verify.py` memeriksa bahwa setiap field yang diandalkan kode memang ada, dan
menyebutkan persis field mana yang hilang kalau ada API yang berubah. Kalau ada
yang merah, perbaiki itu dulu sebelum menjalankan bot.

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
