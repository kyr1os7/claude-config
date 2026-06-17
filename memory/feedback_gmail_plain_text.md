---
name: feedback-gmail-plain-text
description: Gmail draft harus plain text (body), bukan htmlBody — supaya URL tidak ke-wrap jadi link redirect google.com/url
metadata:
  node_type: memory
  type: feedback
  originSessionId: f0e9cd6e-91ba-40e9-b7b1-4e3d0c06fbd3
---

Saat membuat Gmail draft via Gmail MCP `create_draft`, gunakan field `body` (plain text) SAJA — JANGAN pakai `htmlBody`.

**Why:** Kalau draft dibuat sebagai HTML, Gmail otomatis membungkus semua URL jadi link redirect: `https://www.google.com/url?q=https://funtoco.jp&source=gmail&ust=...`.

**UPDATE 2026-06-17 — plain text TIDAK lagi cukup:** Tool `create_draft` sekarang me-rewrite SEMUA string yang terlihat seperti domain (dengan/tanpa `https://`, bahkan `funtoco.jp` polos) menjadi `https://www.google.com/url?q=...&source=gmail&ust=...`, dan menyisipkan karakter kontrol rusak `` di parameter `ust` → link jadi korup. Dikonfirmasi dengan `list_drafts` (cek `plaintextBody`).

**SOLUSI (wajib untuk signature URL):** Sisipkan zero-width space (U+200B) di dalam domain sebelum titik agar tidak terdeteksi sebagai URL, mis. `funtoco​.jp` dan `tokuteiginouvisa-college​.com`. Tampilan tetap normal (`funtoco.jp`), body tersimpan bersih tanpa wrapping. Trade-off: URL jadi tidak clickable & copy-paste membawa karakter tak terlihat — tapi lebih baik daripada link redirect korup.

**Verifikasi:** Setelah create_draft, selalu cek via `list_drafts` (field `plaintextBody`) untuk memastikan URL tidak ke-wrap.

**KEPUTUSAN USER 2026-06-17 — pilih link CLICKABLE:** User memilih link bisa diklik daripada teks bersih. Karena tool SELALU membungkus href jadi `google.com/url?q=<tujuan>&...` (tidak bisa dihindari, dan ini perilaku normal Gmail), gunakan `htmlBody` dengan anchor text bersih:
`URL：<a href="https://funtoco.jp">https://funtoco.jp</a>`
- Anchor TEXT tampil bersih (`https://funtoco.jp`), link bisa diklik.
- href di-wrap ke `google.com/url?q=https://funtoco.jp&...` — param `q=` (tujuan) selalu utuh & di urutan pertama, jadi redirect tetap mengarah ke funtoco.jp meski param `ust` ada char rusak ``.
- Tetap isi `body` (plain text) sebagai fallback, pakai ZWSP di URL-nya (`funtoco​.jp`) supaya versi plain juga bersih.

**Cara apply untuk laporan harian:** body = plain text (URL pakai ZWSP), htmlBody = HTML dengan `<a href>` (anchor text bersih). Link signature: funtoco.jp & tokuteiginouvisa-college.com.

Terkait: [[feedback-no-send-confirm]]
