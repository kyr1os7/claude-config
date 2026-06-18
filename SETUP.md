# Setup Guide — Funtoco Claude Automation

Panduan setup automation Claude Code untuk staf Funtoco.

---

## Prasyarat

- [Claude Code](https://claude.ai/code) sudah terinstall
- Akses internet (untuk fetch prompt dari GitHub)
- MCP connections (lihat section "Setup MCP" di bawah)
- Akun Funtoco: email `@funtoco.jp` + password Kintone

---

## Setup (5 menit)

### 1. Buka file CLAUDE.md

```bash
nano ~/.claude/CLAUDE.md
```

Jika file belum ada, buat baru — tidak apa-apa.

### 2. Tambahkan blok berikut

Copy-paste seluruh blok ini ke dalam file:

```md
## Automation Bootstrap
Jika user mengetik salah satu trigger word berikut di awal session,
fetch URL-nya terlebih dahulu lalu ikuti semua instruksi di file tersebut:

| Trigger Word | URL |
|--------------|-----|
| teikimendan | https://raw.githubusercontent.com/kyr1os7/claude-config/main/prompts/AUTO_teiki_mendan.md |
| hibimendan | https://raw.githubusercontent.com/kyr1os7/claude-config/main/prompts/AUTO_hibi_mendan.md |
| zairyucard | https://raw.githubusercontent.com/kyr1os7/claude-config/main/prompts/AUTO_zairyu_card.md |
| shoruikakunou | https://raw.githubusercontent.com/kyr1os7/claude-config/main/prompts/AUTO_shorui_kakunou.md |
| gyomuhoukoku | https://raw.githubusercontent.com/kyr1os7/claude-config/main/prompts/AUTO_laporan_harian.md |
| mendanyoyaku | https://raw.githubusercontent.com/kyr1os7/claude-config/main/prompts/AUTO_mendan_yoyaku.md |

Jika user mengetik `automation`, tampilkan list trigger word di atas beserta fungsinya.
```

### 3. Save dan tutup

```bash
# Di nano: Ctrl+O → Enter → Ctrl+X
```

---

## Cara Pakai

Buka session Claude Code baru, ketik trigger word sesuai kebutuhan:

| Trigger Word | Fungsi |
|--------------|--------|
| `teikimendan` | 定期面談記録 — input laporan interview ke Kintone |
| `hibimendan` | 日々面談 — input dari Zendesk atau manual |
| `zairyucard` | 在留カード — update data kartu + Google Drive |
| `shoruikakunou` | 書類格納 — rename & simpan dokumen ke Google Drive |
| `gyomuhoukoku` | 業務報告 — buat laporan harian + Kintone + Gmail draft |
| `mendanyoyaku` | 面談予約日程 — update tanggal dari email reservasi |
| `automation` | Tampilkan semua trigger word yang tersedia |

**Claude akan otomatis fetch instruksi dari GitHub, lalu siap menerima perintah.**

---

## Setup MCP

Automation pakai koneksi MCP berikut. Setup di Claude Code masing-masing (pakai kredensial sendiri):

| MCP | Dipakai untuk | Wajib? |
|-----|---------------|--------|
| Gmail | `gyomuhoukoku` (draft email) | ✅ |
| Google Calendar | `gyomuhoukoku` (ambil event) | ✅ |
| Google Drive | `zairyucard`, `shoruikakunou` (upload dokumen) | ✅ |
| Zendesk | `hibimendan` (mode CEK) | Opsional |
| Kintone MCP | bikin/ubah **APP** Kintone (development) — BUKAN untuk automation | Opsional |

> **Penting soal Kintone:** SEMUA automation (baca/tulis record + KPI) pakai **Python urllib + email/password**, jadi **TIDAK butuh Kintone MCP**. Kintone MCP hanya perlu kalau Anda mau **bikin/ubah app Kintone** (development).

### Kintone akses record (untuk automation) — Python urllib

Tidak perlu install apa-apa. Prompt membangun request sendiri:
- Domain: `funtoco.cybozu.com`
- Auth: `X-Cybozu-Authorization: <base64("email:password")>` (Basic auth)
- Pakai **Python `urllib.request`** (JANGAN plain curl)

Cukup sediakan EMAIL + PASSWORD (ditanya otomatis di Step 0).

### Kintone MCP (opsional — untuk development app)

Hanya perlu kalau Anda mau bikin/ubah app, field, layout, atau deploy app Kintone.
Repo resmi: https://github.com/kintone/mcp-server — package npm: `@kintone/mcp-server`.

**1. Install (perlu Node.js):**
```bash
npm install -g @kintone/mcp-server
```
Ini membuat binary bernama `kintone-mcp-server`.

**2. Tambahkan ke MCP config** (`~/.claude/mcp.json`). Dua cara:

Cara A — npx (paling simpel & portable):
```json
{
  "mcpServers": {
    "kintone": {
      "command": "npx",
      "args": ["-y", "@kintone/mcp-server"],
      "env": {
        "KINTONE_BASE_URL": "https://funtoco.cybozu.com",
        "KINTONE_USERNAME": "email@funtoco.jp",
        "KINTONE_PASSWORD": "password-anda"
      }
    }
  }
}
```

Cara B — global install + path (yang dipakai Sandy sekarang):
```json
{
  "mcpServers": {
    "kintone": {
      "type": "stdio",
      "command": "node",
      "args": ["<HOME>/.npm-global/bin/kintone-mcp-server"],
      "env": {
        "KINTONE_BASE_URL": "https://funtoco.cybozu.com",
        "KINTONE_USERNAME": "email@funtoco.jp",
        "KINTONE_PASSWORD": "password-anda"
      }
    }
  }
}
```
Auth Kintone MCP mendukung `KINTONE_USERNAME`/`KINTONE_PASSWORD` ATAU `KINTONE_API_TOKEN`.
Template siap-pakai: `mcp.json.template` (repo ini).

---

## Data Personal (ditanya otomatis saat pertama pakai)

Saat pertama kali ketik `gyomuhoukoku`, Claude akan tanya data ini (Step 0):

| Data | Keterangan | Cara dapat |
|------|-----------|-----------|
| NAMA_LENGKAP | nama kapital (utk subject & signature) | — |
| NAMA_KANA | nama katakana (utk signature) | — |
| EMAIL | email Funtoco Anda | — |
| KINTONE_USER_ID | **ID numerik** di App 98 | **Tanya admin Kintone** — bukan email, tapi angka (contoh: 6142474) |
| PASSWORD | password Kintone | — |

> **Penting:** `KINTONE_USER_ID` adalah angka, bukan email. Kalau salah, query KPI 日々面談 hasilnya 0 tanpa error. Tanyakan ke admin Kintone Anda.

Untuk `hibimendan`, Anda juga perlu **Zendesk API token** — minta ke admin/Sandy secara pribadi (jangan ditulis di file).

---

## Catatan

- Prompt diambil langsung dari repo ini — kalau ada update, otomatis dapat versi terbaru di session berikutnya
- Trigger word hanya perlu diketik **sekali per session** (saat pertama buka)
- Setelah fetch, gunakan trigger internal masing-masing automation (`CEK`, `MENDAN`, `laporan hari ini`, dll)
