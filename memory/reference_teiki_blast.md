---
name: reference-teiki-blast
description: Trigger blastmessage — blast pesan ke 支援者 lewat Chrome (Meta Business Suite / LINE OA) pakai link Zendesk sns_link_11_20; isi pesan berubah-ubah
metadata:
  type: reference
---
Blast pesan ke 支援者 (prompt lengkap: GitHub `prompts/AUTO_blast_message.md`, trigger `blastmessage`):
1. **Isi pesan tidak selalu sama** (kadang 定期面談, kadang pesan lain). Pakai persis yang ditempel user di request itu; kalau tidak ada → tanya, jangan pakai pesan lama.
2. Cari user di Zendesk API (`users/search.json?query=name:"NAMA"`), ambil field `sns_link_11_20`. Kredensial: token Zendesk milik user sendiri (LOCAL ONLY).
3. Prioritas akun tanpa "(LINE)" (= Facebook, link business.facebook.com inbox). Kalau hanya ada link chat.line.biz → kirim lewat LINE OA Manager. Ada akun tanpa "(LINE)" yang link-nya tetap LINE → pakai LINE.
4. Chrome (claude-in-chrome): buka link, ketik per baris dengan shift+Enter, lalu klik Send. FB: cari tombol Send via `find` (koordinat bergeser setelah teks diketik). LINE: tombol 送信 hijau kanan bawah.
5. Nama di Messenger/LINE sering beda dari nama Zendesk. User bilang tidak perlu dipikirkan/dilaporkan: selama link dari Zendesk benar, langsung kirim.
6. Perlu sesi Bypass permissions + allow rule `mcp__claude-in-chrome__computer`/`browser_batch` di ~/Claude/.claude/settings.local.json; di auto mode aksi kirim massal diblokir.
7. Di laporan akhir selalu sertakan link chat (dari Zendesk) per orang di tabel, supaya User bisa 確認 sendiri nanti.
