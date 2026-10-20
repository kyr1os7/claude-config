# Setup Funtoco Automation di Codex (ChatGPT)

Panduan untuk rekan kerja yang memakai **Codex** (bukan Claude). Prompt automation-nya sama dengan versi Claude — hanya cara memasangnya yang beda.

> ⚠️ Harus pakai **Codex** (app Codex / Codex CLI / ekstensi IDE). **ChatGPT chat biasa tidak bisa**, karena tidak bisa mengakses Kintone/Zendesk dari komputer Anda.

---

## 1. Prasyarat

- Codex terinstall dan sudah login dengan akun ChatGPT
- `git` terinstall (cek: buka Terminal, ketik `git --version`)
- Akun Funtoco: email `@funtoco.jp` + password Kintone
- Untuk `hibimendan` / `blastmessage`: Zendesk API token (minta ke Sandy secara pribadi)

---

## 2. Install (sekali saja, ±2 menit)

Buka **Terminal**, copy-paste perintah ini, lalu Enter:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/kyr1os7/claude-config/main/codex/setup_codex.sh)
```

Script ini:
1. Mengunduh semua prompt ke folder `~/funtoco-automation`
2. Menambahkan daftar trigger word ke `~/.codex/AGENTS.md` (isi lama tidak dihapus, ada backup)

---

## 3. Izin network

Automation memanggil API Kintone dan Zendesk lewat Python, jadi Codex perlu akses internet saat menjalankan perintah.

**Cara paling gampang (app Codex):** saat Codex minta izin menjalankan perintah yang butuh internet, pilih **Allow / Approve**. Kalau sering ditanya, ubah mode izin (permission) session ke mode yang mengizinkan akses network.

**Cara permanen (opsional):** buka file `~/.codex/config.toml` lalu tambahkan:

```toml
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = true
```

Simpan, lalu tutup dan buka lagi Codex.

---

## 4. Cara pakai — apa yang diketik di Codex

Buka session/chat Codex baru, lalu **ketik trigger word saja**, contoh:

```
hibimendan
```

Codex akan membaca prompt-nya, menanyakan data Anda (Step 0), lalu siap menerima perintah. Setelah itu pakai perintah internal seperti biasa, misalnya:

```
CEK
```

Ketik `automation` untuk melihat semua trigger word.

| Ketik | Fungsi | Jalan di Codex? |
|---|---|---|
| `hibimendan` | 日々面談 — Zendesk / manual → Kintone | ✅ |
| `visastatus` | Cek perubahan status visa App 50 | ✅ |
| `nichiisheet` | Laporan ニチイ学館シート (teks saja) | ✅ |
| `kyuujin` | Teks lowongan + hitung 手取り | ✅ |
| `teikimendan` | 定期面談記録 → Kintone | 🟡 perlu Google Drive (lihat bagian 5) |
| `zairyucard` | 在留カード → Kintone + Drive | 🟡 perlu Google Drive |
| `shoruikakunou` | 書類格納 → Drive + Kintone | 🟡 perlu Google Drive |
| `gyomuhoukoku` | 業務報告 harian | 🟡 perlu Google Calendar + Gmail |
| `mendanyoyaku` | Update tanggal dari email reservasi | 🟡 perlu Gmail |
| `hikkoshi` | Memo Calendar + rute mobil | 🟡 perlu Google Calendar |
| `hikitsugi` | Google Sheet serah-terima | 🟡 perlu Google Sheets MCP |
| `blastmessage` | Blast FB / LINE lewat browser | ⚠️ eksperimental — selalu cek sebelum kirim |

✅ = cukup Kintone/Zendesk (Python), langsung bisa.
🟡 = butuh koneksi Google. Kalau koneksinya tidak ada, Codex akan mengerjakan bagian Kintone-nya dan memberi tahu langkah mana yang harus Anda lakukan manual.

---

## 5. Koneksi Google (untuk yang 🟡)

Di app Codex, cek menu **Settings → Plugins / Apps / Connectors**. Kalau tersedia **Google Drive, Gmail, Google Calendar**, sambungkan dengan akun `@funtoco.jp` Anda.

Kalau tidak ada di daftar, automation 🟡 tetap bisa dipakai sebagian (bagian Kintone), dan sisanya manual (misalnya upload file ke Drive sendiri).

Untuk `hikitsugi` (Google Sheets) perlu MCP server khusus — hubungi Sandy untuk setup-nya.

---

## 6. Simpan data supaya tidak ditanya terus (opsional)

Buka `~/.codex/AGENTS.md`, cari bagian **Data Pribadi**, isi nama, email, dan KINTONE_USER_ID.

> Jangan tulis **password** atau **token** di file — ketik saja saat ditanya.

---

## 7. Update

Prompt otomatis di-update (`git pull`) setiap kali Anda mengetik trigger word. Tidak perlu install ulang.

## Troubleshooting

| Masalah | Solusi |
|---|---|
| Codex tidak mengenali trigger word | Pastikan `~/.codex/AGENTS.md` berisi blok `FUNTOCO-AUTOMATION`. Jalankan ulang script di bagian 2, lalu buka session baru |
| Error koneksi ke Kintone/Zendesk | Izin network belum aktif — lihat bagian 3 |
| Hasil KPI 日々面談 = 0 | `KINTONE_USER_ID` salah — harus **angka**, bukan email. Tanya admin Kintone |
| `git: command not found` | Install Xcode Command Line Tools: jalankan `xcode-select --install` di Terminal |
