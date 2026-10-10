---
name: reference-google-slides-mcp
description: "Google Slides MCP connector sudah terpasang — cara kerja, batasan, dan file penting untuk edit deck langsung di Google Slides"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 52e79bdd-de0f-47f3-b710-121b6955024b
  modified: 2026-07-28T16:15:17.717Z
---

Connector **`google-slides`** (paket npm `mcp-google-slides`) sudah terpasang dan terautentikasi sejak 2026-07-29. Claude bisa membaca dan mengedit Google Slides milik `sandy@funtoco.jp` secara langsung.

**Why:** Setup-nya makan waktu ~1 jam dan ada beberapa jebakan yang tidak terdokumentasi di README paketnya. Jangan diulang dari nol.

**How to apply:**

Setup yang sudah jadi:
- Paket global: `~/.npm-global/bin/mcp-google-slides`
- Terdaftar di `~/.claude.json` → `mcpServers.google-slides` (berisi GOOGLE_CLIENT_ID/SECRET)
- Token OAuth: `~/.google-slides-mcp/tokens.json` — **catatan: README paket salah**, dia menulis `~/.mcp-google-slides/`
- Salinan kredensial: `~/.mcp-google-slides/credentials.env` (chmod 600)
- Google Cloud project: `Sandyfuntocodocs` (id 442369801536), consent screen tipe **Internal** (tidak perlu verifikasi/test user)
- Scope: `presentations` + `drive.file`

Jebakan yang sudah dipecahkan:
1. **Paketnya tidak menjalankan server OAuth callback sama sekali** (`createServer` nol di dist/server.js) — `mcp-google-slides auth` bawaan selalu berakhir ERR_CONNECTION_REFUSED dan menuntut paste kode manual. Gantinya pakai `~/Claude/benkyoukai-ai/auth_slides.js` yang menjalankan server di :3000 dan menangkap kode otomatis. Jalankan itu kalau token kadaluarsa.
2. Google Slides API **dan** Drive API harus di-enable di project yang sama dengan OAuth client-nya.
3. UI Google Cloud lama vs baru berbeda — di akun Sandy masih UI lama (APIs & Services → Credentials + OAuth consent screen di sidebar).

Batasan yang sudah diuji:
- `get_slide` mengembalikan **geometri saja, tanpa isi teks**. Untuk memetakan objectId ke konten, konversi EMU ke inci (**914400 EMU = 1 inci**) lalu cocokkan dengan koordinat di `build_deck.js`.
- `update_text` **mempertahankan** warna, bold, dan ukuran font (sudah diuji di file scratch, bukan di deck asli).
- Jangan tes coba-coba di deck asli — bikin presentasi scratch, tes, lalu `delete_presentation`. Lihat [[reference_hibi_mendan_workflow]] poin 8 untuk prinsip yang sama.

Lihat [[project_ai_benkyoukai]] untuk deck yang sedang dikerjakan.
