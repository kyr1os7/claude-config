---
name: project-ai-server-migration
description: Rencana pindah ke PC server 24 jam (akses via Remote Control); repo private = sumber migrasi; MCP config ada di ~/.claude.json; transcript tidak dibawa
metadata:
  node_type: memory
  type: project
  originSessionId: 20e01b5b-8397-4ef9-a090-3e366faaf0ab
  modified: 2026-10-10T15:30:02.230Z
---

Sandy berencana memindahkan semua kerja Claude ke **1 PC yang menyala 24 jam** dan berhenti menyimpan file di laptop. Status 2026-10-10: PC **belum dibeli, OS belum ditentukan**.

## Keputusan (2026-10-10)
- Akses: **Remote Control** (session di PC server, dikontrol dari claude.ai/code)
- Sumber migrasi: repo **private** `kyr1os7/claude-config-private` — panduan lengkap di `MIGRATION.md`
- Session transcript lama (`*.jsonl`, 568MB): **tidak dibawa**
- Riwayat repo public di-reset jadi 1 commit (buang credential & PII lama); branch grok + proyek sniper dihapus atas permintaan user

## Temuan penting saat persiapan
- **Konfigurasi MCP yang aktif ada di `~/.claude.json`** (kintone, google-slides, google-sheets) — BUKAN `~/.claude/mcp.json` (file lama, tidak dibaca Claude Code). Blok `mcpServers` dibackup ke private `local-config/claude.json.mcpServers.json`.
- Kredensial OAuth Google dibackup ke private `local-config/google/`: `~/.mcp-google-sheets/` (Sheets MCP), `~/.google-slides-mcp/` (Slides MCP), `~/.config/funtoco-gdocs/` (script gdoc lama, tidak dipakai prompt mana pun), file `client_secret_…json`.
- 4 session pinned tanpa backup sudah diekstrak: `nichiisheet` (【AGENT】ニチイ学館シート), `kyuujin` (【AGENT】求人Generative), `hikitsugi` (【PROJECT】引き継ぎシート), dan 【PROJECT】しえん-ちゃん → memory [[project-shien-chan-slack-agent]].
- `zairyucard` & `shoruikakunou` **tetap membaca dari folder Downloads** — user download manual dulu dari Zendesk. Keputusan user 2026-10-11: JANGAN diubah ke Zendesk API ([[feedback-keep-existing-workflow]]).

**Why:** User mau kerja dari mana saja tanpa file lokal; PC 24 jam juga membuat scheduled task/routine bisa jalan terus.

**How to apply:**
- Saat setup PC server → ikuti `MIGRATION.md` di repo private, sesuaikan OS. Rekomendasi macOS (mis. Mac mini) atau Windows — Remote Control butuh Claude desktop app (Linux hanya CLI).
- Session tidak ikut otomatis: buat ulang session per trigger word (daftar ada di `MIGRATION.md`).
- Sebelum hari migrasi, sync ulang memory lokal → private (flow [[feedback-up-github-flow]]).
- Routine visa status yang dulu dibatalkan bisa ditawarkan lagi setelah PC 24 jam jalan (connector Gmail kini punya fitur kirim).
