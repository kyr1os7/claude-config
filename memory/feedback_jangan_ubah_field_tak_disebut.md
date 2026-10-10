---
name: feedback-jangan-ubah-field-tak-disebut
description: Jangan menulis ke field Kintone yang tidak Sandy sebutkan namanya secara spesifik — tanya dulu
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 874789db-3152-47ad-8541-ae7830072e90
  modified: 2026-08-05T01:12:16.213Z
---

Jangan pernah menulis ke field Kintone yang namanya tidak Sandy sebutkan secara eksplisit. Kalau perlu mengubah field lain untuk mencapai hasil yang diminta, **tanya dulu**, jangan tafsirkan sendiri.

**Why:** 2026-08-05, Sandy bilang "ya udah recordnya simpan" soal angka 特定技能通算 yang basi. Saya menafsirkannya sebagai "refresh", lalu menulis `現在の年`/`現在の月` di 10 record App 30. Sandy kaget dan harus meminta konfirmasi bahwa 初回許可された日, 終了予定日, dan tanggal 許可年月日/入社年月/退社年月 di 職歴一覧 tidak tersentuh. Data visa itu krusial — perhitungan salah bisa berakibat ke 申請 dan status 在留 orang.

**How to apply:**
- "simpan" ≠ "ubah nilai". Kalau menyimpan saja tidak menghasilkan efek yang diminta, laporkan itu dan tanya, jangan lanjut menulis.
- Sebelum update, tarik dulu nilai lamanya dan simpan di jawaban, supaya bisa dikembalikan persis.
- Setelah update subtable, selalu verifikasi ulang dengan get-records (baris yang tidak dikirim akan TERHAPUS oleh Kintone — selalu sertakan semua baris beserta `id`-nya).
- Field visa yang tidak boleh disentuh tanpa instruksi eksplisit: `初回許可された日`, `終了予定日`, dan di 職歴一覧: `許可年月日_1`, `workHistoryJoinYear_1/Month_1`, `workHistoryLeaveYear_1/Month_1`.
- Laporkan daftar lengkap apa saja yang ditulis di akhir pekerjaan.

Terkait: [[reference-tokutei-ginou-tsuusan]], [[feedback-dropbox-no-overwrite]]
