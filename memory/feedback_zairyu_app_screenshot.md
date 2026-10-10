---
name: feedback-zairyu-app-screenshot
description: Kadang user kirim screenshot aplikasi 在留カード読取 berisi 許可年月日 — ambil dari situ, jangan pakai aturan ISA
metadata:
  node_type: memory
  type: feedback
  originSessionId: f0e9cd6e-91ba-40e9-b7b1-4e3d0c06fbd3
  modified: 2026-08-27T04:54:51.864Z
---

Mulai kadang (tidak selalu), user akan menyertakan screenshot hasil aplikasi 在留カード等読取アプリケーション (residence card reader app — tampilan "照会結果") selain foto kartu 表/裏. Screenshot ini berisi info 許可 (許可の種類 + 許可年月日) yang eksplisit dan akurat.

**Why:** User bilang "isinya ada 許可日, bisa ambil dr sana infonya" — ini menggantikan kebutuhan aturan ISA (tebak tahun=sekarang, bulan/hari=sama expire) saat kartu ISA design tidak mencetak 許可年月日.

**How to apply:**
1. Kalau ada file screenshot aplikasi (bukan foto fisik kartu — biasanya tampilan hijau "正常な在留カードを読み取りました" dengan bagian "許可" di bawah), baca 許可年月日 langsung dari situ. Ini prioritas di atas aturan ISA (tebak).
2. Jumlah file bisa 3 (表 + 裏 + アプリ) bukan cuma 2 — sesuaikan penghitungan.
3. Naming khusus untuk file screenshot ini: `［在留カードアプリ : 特定技能１号X回目］FULLNAME : 呼び名カタカナ.jpg` (bukan 表/裏, tapi "アプリ").
4. Foto kartu 表/裏 fisik tetap pakai naming biasa (`表`/`裏`).
5. Field `furigana` di App 30 (label: カタカナ_呼び名) adalah sumber nama panggilan katakana kalau belum tahu dari sesi sebelumnya.
