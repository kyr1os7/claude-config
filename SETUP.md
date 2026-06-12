# Setup Guide — Funtoco Claude Automation

Panduan setup automation Claude Code untuk staf Funtoco.

---

## Prasyarat

- [Claude Code](https://claude.ai/code) sudah terinstall
- Akses internet (untuk fetch prompt dari GitHub)

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
| shorouikakou | https://raw.githubusercontent.com/kyr1os7/claude-config/main/prompts/AUTO_shorui_kakou.md |
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
| `shorouikakou` | 書類格納 — rename & simpan dokumen ke Google Drive |
| `gyomuhoukoku` | 業務報告 — buat laporan harian + Kintone + Gmail draft |
| `mendanyoyaku` | 面談予約日程 — update tanggal dari email reservasi |
| `automation` | Tampilkan semua trigger word yang tersedia |

**Claude akan otomatis fetch instruksi dari GitHub, lalu siap menerima perintah.**

---

## Catatan

- Prompt diambil langsung dari repo ini — kalau ada update, otomatis dapat versi terbaru di session berikutnya
- Trigger word hanya perlu diketik **sekali per session** (saat pertama buka)
- Setelah fetch, gunakan trigger internal masing-masing automation (`CEK`, `MENDAN`, `laporan hari ini`, dll)
