---
name: reference_cek_app50_workflow
description: '"cek" trigger — perubahan status app50 (作業者=Sandy) + tabel menyeluruh bola-di-Sandy (4 status ⭐)'
metadata: 
  type: reference
  node_type: memory
  originSessionId: bfe0579d-9f10-4c52-8acd-9200adddbab6
  modified: 2026-07-27T01:05:24.788Z
---

Trigger **`cek`** (atau `CEK`): cek perubahan ステータス di Kintone app50 (就労_ビザ管理) untuk record yang 作業者-nya berisi Sandy (sandy@funtoco.jp).

**Cara jalan:**
1. Ambil waktu JST sekarang + kemarin (window = status berubah hari ini ATAU kemarin).
2. `kintone-get-records` app 50, filter `dateRange` 更新日時 dari kemarin s/d besok (hasil sering >token limit → simpan ke file, filter pakai `jq` di file: `select(.["作業者"].value | any(.code=="sandy@funtoco.jp"))`).
3. Bedakan **perubahan status asli** vs **edit field biasa**: cek stempel Status Time Line (DATE field yg cocok dgn status), bukan cuma 更新日時. Contoh mapping: 申請中→`申請中`, ビザ申請待ち→`数字_ビザ申請待ち`, ビザ申請準備中→`ビザ申請準備中`, OP_企業書類作成中→`書類作成中`, OP_押印書類受取待ち→`数字_押印書類受取待ち`, OP_申請人サイン書類準備中→`数字_申請人サイン書類準備中`, 企業_書類確認待ち→`書類確認中`, 支援_申請人サイン待ち→`数字_本人サイン待ち`. Kalau stempel = window → confirmed; kalau lama → field edit (exclude).
4. Waspada **一括バッチ**: kadang seluruh app ke-update di jam yg sama (puluhan record) → itu bukan perubahan status individual.

**Field codes app50:** 名前=`fullName`, status=`ステータス` (STATUS), deadline=`ステータス期限` (DATETIME), 作業者=`作業者` (STATUS_ASSIGNEE), `更新日時` (UPDATED_TIME). Link record: `https://funtoco.cybozu.com/k/50/show#record=<VIID number>`.

**Format tabel (header full Jepang):** 名前 · 新ステータス · 変更日時（JST） · ステータス期限 · リンク. Sort by 変更日時 desc. Deadline DATETIME `T02:00:00Z`=11:00 JST, `T00:00:00Z`=09:00 JST.

**⭐ "Bola di Sandy"** (mulai 2026-07-08; 2026-10-21 +ビザ申請準備中; 2026-11-11 status Kintone berubah → sekarang 7 status, versi Tethys Atlas sudah diperbarui & di-deploy): kalau status SAAT INI salah satu dari ini, beri ⭐ (butuh aksi Sandy):
- 支援_更新案内・人材情報更新待ち
- 支援_申請人サイン待ち
- ビザ申請準備中
- 納付案内待ち (BARU, tombol 納付支払い案内済み)
- 支払い確認待ち (BARU, tombol 支払い確認済み; isi 納付日 di RAKUVISA dulu)
- 新在留カード受け取り案内待ち (= 本人案内待ち lama, di-rename; tombol 受け取り案内済み)
- 在留カード情報待ち

**Perubahan 2026-11-11** (kasus 認定申請以外 dgn tanggal申請 ≥ 2026/10/1): 申請中 →(許可確認済み)→ 納付通知待ち [otomatis/tunggu 入管, BUKAN bola Sandy] →(納付通知受領済み)→ 納付案内待ち →(納付支払い案内済み)→ 支払い確認待ち →(支払い確認済み)→ 新在留カード受け取り案内待ち →(受け取り案内済み)→ 在留カード情報待ち → 許可. Nama `本人案内待ち` sudah TIDAK ADA di Kintone: query yg memakainya error http_400 (opsi tidak ditemukan pada field ステータス). 3 status baru tak punya stempel Time Line (deteksi perubahan via 更新日時 + deadline). Cek daftar status terkini: `/k/v1/app/status.json?app=50`.

Status lain tetap dilaporkan tanpa ⭐ (bola di tim lain). Catatan: 新在留カード受け取り案内待ち & 納付案内待ち & 支払い確認待ち & 在留カード情報待ち & 支援_更新案内 TIDAK punya stempel Time Line → judgment "berubah dalam window" pakai kombinasi 更新日時 + deadline baru, tandai "要確認" kalau tak bisa dipastikan.

**Output tiap `cek` = 2 bagian** (mulai 2026-07-27):
1. Perubahan status di window (hari ini/kemarin), format tabel di atas.
2. **Tabel menyeluruh "BOLA DI SANDY"**: SEMUA record app50 dgn 作業者=Sandy di 4 status ⭐, tanpa batas waktu update. Query: `kintone-get-records` app50 `inValues` ステータス = [4 status ⭐] (STATUS bisa di-inValues), lalu jq filter assignee sandy, sort by ステータス期限 asc. Tandai 🔴 lewat 期限 / 🟡 hari ini-besok / 🟢 masih ada. Ini backlog akurat (ambil kondisi terkini, bukan tracking per-window).

**Bahasa**: narasi/penjelasan `cek` pakai Bahasa Indonesia; nama status, header tabel, & isi Kintone tetap Jepang.

Terkait: [[feedback_japan_timezone]] [[reference_kintone_apps]] [[feedback_bahasa_indonesia]]
- 2026-11-04 visastatus: tanda 🔴 lewat deadline / 🟡 hari ini-besok / 🟢 nanti / ⚪ tanpa deadline di depan nama tiap kartu (kintone_tool._visa_report, sesuai aturan lama cek app50). Backup kintone_tool.py.bak-pre-dot, restart Office ke-13.
