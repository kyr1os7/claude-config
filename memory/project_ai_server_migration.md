---
name: project-ai-server-migration
description: Rencana pindah ke PC server 24 jam (akses via Remote Control); repo private = sumber migrasi; transcript tidak dibawa
metadata:
  node_type: memory
  type: project
  originSessionId: 20e01b5b-8397-4ef9-a090-3e366faaf0ab
  modified: 2026-10-10T08:26:54.316Z
---

Sandy berencana memindahkan semua kerja Claude ke **1 PC yang menyala 24 jam** dan berhenti menyimpan file di laptop. Status 2026-10-10: PC **belum dibeli, OS belum ditentukan**.

Keputusan (2026-10-10):
- Akses: **Remote Control** (session di PC server, dikontrol dari claude.ai/code)
- Sumber migrasi: repo **private** `kyr1os7/claude-config-private` — full backup 2026-10-10, panduan lengkap di `MIGRATION.md`
- Session transcript lama (`*.jsonl`, 568MB): **tidak dibawa** — pengetahuan sudah ada di memory
- Riwayat repo public di-reset jadi 1 commit (buang credential & PII lama); branch grok + proyek sniper dihapus atas permintaan user

**Why:** User mau kerja dari mana saja tanpa file lokal; PC 24 jam juga membuat scheduled task/routine bisa jalan terus.

**How to apply:**
- Saat user mulai setup PC server → ikuti `MIGRATION.md` di repo private, sesuaikan OS yang dipilih. Rekomendasi macOS (mis. Mac mini) atau Windows, karena Remote Control butuh Claude desktop app (Linux hanya CLI).
- `zairyucard` & `shoruikakunou` membaca file dari Downloads → di server butuh cara intake baru (mis. folder Google Drive "inbox"). Tanyakan user dulu sebelum mengubah prompt.
- Sebelum hari migrasi, sync ulang memory lokal → private (flow [[feedback-up-github-flow]]).
- Routine visa status yang dulu dibatalkan bisa ditawarkan lagi setelah PC 24 jam jalan (connector Gmail kini punya fitur kirim).
