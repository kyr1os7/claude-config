---
name: hikkoshi-calendar-app264
description: Trigger 【出発点・タイムスパーク】+nama tempat → Kintone App 264 (引越し・運転) → buat event Google Calendar dengan memo format tetap + estimasi rute mobil
metadata:
  node_type: memory
  type: reference
  originSessionId: 6120bb0a-dde0-4930-90d4-bd9ec4f26ea9
  modified: 2026-09-30T07:41:13.789Z
---

Trigger word: `hikkoshi` (prompt: kyr1os7/claude-config prompts/AUTO_hikkoshi_calendar.md). Arsip case nyata → private repo hikkoshi-cases/.

App 264 = jadwal 引越し/運転 (movingDate, 開始/終了, 現在住所, 新役所名/MAPリンク, 配属先名/MAPリンク, 担当名/担当連絡先, 新住所, ガス会社名/ガス会社_連絡先/ガス立ち会い予定/ガス保証金額, 運転担当).

Event: tanggal = movingDate, jam = 開始–終了 (JST), title `【引越し対応・運転】名前／法人名`, location = titik start.
TRIGGER (user kirim):
```
【出発点・タイムスパーク】
<nama tempat>   ← user ketik
<link google map> ← Claude carikan
```
+ link record App 264. Claude: cari alamat tempat itu (WebSearch, mis. share.timescar.jp), buat link Google Maps search (nama + alamat, URL-encoded), tulis 2 baris itu di bawah 【出発点・タイムスパーク】; location event = nama（alamat）.
Urutan rute: 出発点 → 現在住所 → 新役所 → 配属先(挨拶) → 新住所. Default berangkat 09:00, KECUALI user sebut jam lain (mis. "10:00 dari タイムズ") → pakai jam itu & geser semua jam; jam event Calendar tetap 開始–終了 Kintone.
Baris 【異動】 berisi: `車で約X分（約Ykm）｜HH:MM出発（滞在想定）→ HH:MM頃到着`. Asumsi dipakai (teks persis): `（現在住所 荷物積込み30分想定）`, `（役所手続き1時間30分想定）`, `（挨拶30分想定）`.
Field kosong → 未確認; nilai tidak diubah. KECUALI 現在情報: user minta selalu dilengkapi — 現在住所・MAPリンク = Google Maps search link (https://www.google.com/maps/search/?api=1&query=<alamat encoded>), 現在市役所 = cari via WebSearch (nama + 〒 + alamat resmi). Kintone tidak ikut diubah. Contoh pertama: record 1 (2026-10-01).
Paling bawah memo (setelah 【ガス情報】): `レオパレス部屋詳細PDF：<link download.do>` lalu `Kintoneレコード：https://funtoco.cybozu.com/k/264/show#record=ID`. Link PDF format `https://funtoco.cybozu.com/k/api/record/download.do/-/<file>.pdf?app=264&field=6154840&detectType=true&record=ID&row=..&id=..&hash=..&revision=..&.pdf` — hash/row/id tidak ada di REST API, jadi ambil dari UI record (browser) atau minta user.
