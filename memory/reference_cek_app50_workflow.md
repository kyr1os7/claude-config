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

**⭐ "Bola di Sandy"** (mulai 2026-07-08): kalau status SAAT INI salah satu dari 4 ini, beri ⭐ (butuh aksi Sandy):
- 支援_更新案内・人材情報更新待ち
- 支援_申請人サイン待ち
- 本人案内待ち
- 在留カード情報待ち

Status lain tetap dilaporkan tanpa ⭐ (bola di tim lain). Catatan: 本人案内待ち & 在留カード情報待ち & 支援_更新案内 TIDAK punya stempel Time Line → judgment "berubah dalam window" pakai kombinasi 更新日時 + deadline baru, tandai "要確認" kalau tak bisa dipastikan.

**Output tiap `cek` = 2 bagian** (mulai 2026-07-27):
1. Perubahan status di window (hari ini/kemarin), format tabel di atas.
2. **Tabel menyeluruh "BOLA DI SANDY"**: SEMUA record app50 dgn 作業者=Sandy di 4 status ⭐, tanpa batas waktu update. Query: `kintone-get-records` app50 `inValues` ステータス = [4 status ⭐] (STATUS bisa di-inValues), lalu jq filter assignee sandy, sort by ステータス期限 asc. Tandai 🔴 lewat 期限 / 🟡 hari ini-besok / 🟢 masih ada. Ini backlog akurat (ambil kondisi terkini, bukan tracking per-window).

**Bahasa**: narasi/penjelasan `cek` pakai Bahasa Indonesia; nama status, header tabel, & isi Kintone tetap Jepang.

Terkait: [[feedback_japan_timezone]] [[reference_kintone_apps]] [[feedback_bahasa_indonesia]]
