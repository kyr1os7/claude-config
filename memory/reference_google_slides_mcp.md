---
name: reference-google-slides-mcp
description: "MCP Google Slides + Sheets: project tethys-office sejak 2026-11-18 (Sandyfuntocodocs terhapus), re-auth via bin/google-mcp-auth, batasan get_slide/update_text"
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
- Paket global: `~/.nvm/versions/node/v24.14.1/bin/mcp-google-slides`
- Terdaftar di `~/.claude.json` → `mcpServers.google-slides` (berisi GOOGLE_CLIENT_ID/SECRET)
- Token OAuth: `~/.google-slides-mcp/tokens.json` — **catatan: README paket salah**, dia menulis `~/.mcp-google-slides/`
- Salinan kredensial: `~/.mcp-google-slides/credentials.env` (chmod 600)
- **Sejak 2026-11-18: project Google Cloud `tethys-office`** (milik Funtoco, consent Internal), client Desktop **`hyperion-mcp`** (terpisah dari client Atlas `tethys-office-hermes`). Project lama `Sandyfuntocodocs` (442369801536) tak sengaja dihapus Sandy 2026-11-18 dan TIDAK dipulihkan (keputusan Sandy: satukan di tethys-office).
- Satu refresh token dipakai Sheets (`~/.mcp-google-sheets/gdrive-token.json`) dan Slides (`~/.google-slides-mcp/tokens.json`). Client: Sheets di `gdrive-credentials.json` (format `installed`), Slides di env `~/.claude.json` + `~/.mcp-google-slides/credentials.env`. Backup lama `*.bak-sandyfuntocodocs` (mati).
- **Re-auth / ganti client: `~/hyperion/bin/google-mcp-auth url <client.json>` → Sandy login di Mac, kirim URL localhost:3456 → `finish '<URL>'` → `check`.** Script memasang semua tempat sekaligus, cek akun sandy@funtoco.jp. auth_slides.js lama tidak perlu lagi.
- Scope token: spreadsheets, drive, presentations, documents, calendar, gmail.readonly, gmail.compose. **Akses lebar ini disetujui Sandy (2026-11-18: "banyak gpp, emang mau saya kasih") — jangan tawarkan mempersempit lagi.** Script meminta scope yang sama secara eksplisit.
- Cek kesehatan: refresh token sukses BELUM berarti jalan — project terhapus tetap memberi refresh 200, tapi API 403 CONSUMER_INVALID. Selalu tes panggilan API sungguhan (`google-mcp-auth check` memanggil Drive about).

Jebakan yang sudah dipecahkan:
1. **Paketnya tidak menjalankan server OAuth callback sama sekali** (`createServer` nol di dist/server.js) — `mcp-google-slides auth` bawaan selalu berakhir ERR_CONNECTION_REFUSED dan menuntut paste kode manual. Gantinya pakai `~/hyperion/benkyoukai-ai/auth_slides.js` yang menjalankan server di :3000 dan menangkap kode otomatis (riwayat; sejak 2026-11-18 login ulang pakai `~/hyperion/bin/google-mcp-auth`).
2. Google Slides API **dan** Drive API harus di-enable di project yang sama dengan OAuth client-nya.
3. UI Google Cloud lama vs baru berbeda — di akun Sandy masih UI lama (APIs & Services → Credentials + OAuth consent screen di sidebar).

Batasan yang sudah diuji:
- `get_slide` mengembalikan **geometri saja, tanpa isi teks**. Untuk memetakan objectId ke konten, konversi EMU ke inci (**914400 EMU = 1 inci**) lalu cocokkan dengan koordinat di `build_deck.js`.
- `update_text` **mempertahankan** warna, bold, dan ukuran font (sudah diuji di file scratch, bukan di deck asli).
- Jangan tes coba-coba di deck asli — bikin presentasi scratch, tes, lalu `delete_presentation`. Lihat [[reference-hibi-mendan-workflow]] poin 8 untuk prinsip yang sama.

Lihat [[project-ai-benkyoukai]] untuk deck yang sedang dikerjakan.
