---
name: feedback-gmail-plain-text
description: Gmail draft harus plain text (body), bukan htmlBody — supaya URL tidak ke-wrap jadi link redirect google.com/url
metadata:
  node_type: memory
  type: feedback
  originSessionId: f0e9cd6e-91ba-40e9-b7b1-4e3d0c06fbd3
---

Saat membuat Gmail draft via Gmail MCP `create_draft`, gunakan field `body` (plain text) SAJA — JANGAN pakai `htmlBody`.

**Why:** Kalau draft dibuat sebagai HTML, Gmail otomatis membungkus semua URL jadi link redirect: `https://www.google.com/url?q=https://funtoco.jp&source=gmail&ust=...`. Dengan plain text, URL tetap apa adanya (`https://funtoco.jp`).

**How to apply:** Berlaku untuk SEMUA pembuatan Gmail draft (laporan harian / business report dan email lain), bukan cuma satu prompt. Isi `body`, kosongkan `htmlBody`.

Terkait: [[feedback-no-send-confirm]]
