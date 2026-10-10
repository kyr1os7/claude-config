---
name: feedback-zairyu-postal-code
description: 郵便番号 tidak ada di kartu 在留カード — cari sendiri via web search berdasarkan alamat
metadata:
  node_type: memory
  type: feedback
  originSessionId: f0e9cd6e-91ba-40e9-b7b1-4e3d0c06fbd3
  modified: 2026-08-19T07:28:55.407Z
---

在留カード tidak pernah mencetak 郵便番号 (kode pos) — hanya alamat teks. Saat alamat orang berubah (pindah rumah) dan perlu update App 30, jangan biarkan 郵便番号 kosong/lama begitu saja atau menebak.

**Why:** User menegur ("kode pos tidak ada di zairyu card, cari sndiri berdasarkan alamat") saat kode pos dibiarkan tetap ke alamat lama karena tidak ditemukan di dokumen Drive.

**How to apply:** Jika alamat App 30 berbeda dari kartu (pindah), setelah update alamat — WebSearch `"<alamat lengkap>" 郵便番号` untuk cari kode pos yang benar, lalu isi field `postNumber` di App 30. Jangan tanya user, cari sendiri dulu.

**Catatan teknis terkait:** field `address` di App 30 adalah calculated/expression field (`prefectures&municipalities&townName&streetAddress`) — tidak bisa diedit langsung via PUT, harus update 4 field komponennya: `prefectures` (都道府県), `municipalities` (市区町村), `townName` (町名), `streetAddress` (番地等). Lihat [[reference_zairyu_card_update]].
