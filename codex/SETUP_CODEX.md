# Panduan Funtoco Automation di Codex (Mac)

Panduan ini untuk rekan kerja yang memakai **Codex** (dari OpenAI / ChatGPT) di **Mac**.
Waktu setup: **±10 menit, cukup sekali**.

Setelah selesai, Anda cukup mengetik satu kata di Codex (misalnya `hibimendan`), dan Codex akan mengerjakan automation-nya.

> ⚠️ **Harus pakai app Codex, bukan ChatGPT biasa.** ChatGPT chat biasa tidak bisa mengakses Kintone dan Zendesk dari komputer Anda.

---

## ✅ Siapkan dulu

- [ ] Mac dengan koneksi internet
- [ ] Akun ChatGPT (untuk login ke Codex)
- [ ] Email Funtoco `@funtoco.jp` + password Kintone
- [ ] *(Hanya untuk `hibimendan` / `blastmessage`)* Zendesk API token → minta ke Sandy lewat chat pribadi

---

## Langkah 1 — Install app Codex

1. Download app **Codex** dari situs resmi OpenAI: https://openai.com/codex
   (Kalau bingung, minta link ke Sandy.)
2. Buka file yang terdownload, lalu drag ikon **Codex** ke folder **Applications**.
3. Buka app Codex, lalu **login dengan akun ChatGPT** Anda.

---

## Langkah 2 — Buka Terminal

Terminal adalah aplikasi bawaan Mac untuk mengetik perintah.

1. Tekan **⌘ Command + Spasi** (membuka Spotlight)
2. Ketik `Terminal`
3. Tekan **Enter**

Akan muncul jendela putih/hitam berisi teks. Biarkan terbuka.

---

## Langkah 3 — Jalankan perintah install

**Copy** baris di bawah ini, **paste** ke Terminal (⌘ + V), lalu tekan **Enter**:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/kyr1os7/claude-config/main/codex/setup_codex.sh)
```

**Berhasil kalau** muncul tulisan seperti ini di bagian akhir:

```
Bootstrap ditambahkan ke /Users/namaanda/.codex/AGENTS.md
Selesai.
```

> 💡 **Muncul jendela "install command line developer tools"?**
> Klik **Install**, tunggu sampai selesai (bisa 5–10 menit), lalu ulangi Langkah 3.

---

## Langkah 4 — Izinkan Codex mengakses internet

Automation perlu internet untuk mengambil dan menyimpan data di Kintone/Zendesk.

Masih di Terminal, **copy-paste** baris ini lalu **Enter**:

```bash
grep -q '^\[sandbox_workspace_write\]' ~/.codex/config.toml 2>/dev/null || printf '\n[sandbox_workspace_write]\nnetwork_access = true\n' >> ~/.codex/config.toml
```

Tidak akan muncul tulisan apa-apa, dan itu normal.

Lalu **tutup app Codex sepenuhnya** (⌘ + Q) dan buka lagi.

> 💡 Kalau nanti Codex tetap bertanya *"Allow this command?"* / minta izin menjalankan perintah, pilih **Allow / Approve**.

---

## Langkah 5 — Tes pertama

1. Di app Codex, buka **chat/session baru**
2. Ketik:
   ```
   automation
   ```
   → Codex akan menampilkan daftar semua trigger word. **Artinya setup berhasil 🎉**
3. Coba automation yang aman (hanya membaca data, tidak mengubah apa pun):
   ```
   visastatus
   ```
   Codex akan menanyakan email dan password Kintone Anda. Setelah diisi, ketik:
   ```
   cek
   ```
   → Codex menampilkan perubahan status visa untuk record Anda.

Kalau langkah ini jalan, Anda siap memakai semua automation.

---

## 📋 Cara pakai sehari-hari

**Selalu mulai dari session baru**, lalu ketik trigger word-nya. Setelah itu ikuti perintah yang diminta Codex (misalnya `CEK`, `MENDAN`, `laporan hari ini`).

| Ketik | Untuk apa | Status |
|---|---|---|
| `hibimendan` | 日々面談 — dari Zendesk / manual → Kintone | ✅ Bisa |
| `visastatus` | Cek perubahan status visa (App 50) | ✅ Bisa |
| `kyuujin` | Teks lowongan + hitung 手取り | ✅ Bisa |
| `teikimendan` | 定期面談記録 → Kintone | 🟡 Butuh Google Drive |
| `zairyucard` | Update 在留カード → Kintone + Drive | 🟡 Butuh Google Drive |
| `shoruikakunou` | 書類格納 — rename & simpan dokumen | 🟡 Butuh Google Drive |
| `gyomuhoukoku` | 業務報告 harian + draft email | 🟡 Butuh Google Calendar + Gmail |
| `mendanyoyaku` | Update tanggal dari email reservasi | 🟡 Butuh Gmail |
| `hikkoshi` | Memo Calendar + rute mobil 引越し | 🟡 Butuh Google Calendar |
| `blastmessage` | Kirim pesan massal FB / LINE | ⚠️ Percobaan — cek isi sebelum kirim |
| `automation` | Lihat semua daftar di atas | ✅ |

**✅ Bisa** — langsung jalan.
**🟡 Butuh Google** — di app Codex buka **Settings → Plugins / Apps / Connectors**. Kalau ada Google Drive / Gmail / Google Calendar, sambungkan dengan akun `@funtoco.jp`. Kalau tidak ada, Codex tetap mengerjakan bagian Kintone-nya dan memberi tahu langkah mana yang perlu Anda kerjakan manual.

---

## 💾 (Opsional) Supaya tidak ditanya data terus

Di Terminal, ketik ini lalu **Enter**:

```bash
open -e ~/.codex/AGENTS.md
```

File akan terbuka di TextEdit. Scroll ke bagian **Data Pribadi**, isi nama, email, dan `KINTONE_USER_ID`, lalu simpan (⌘ + S).

> 🔒 **Jangan tulis password atau token di file ini.** Ketik saja saat Codex bertanya.
> `KINTONE_USER_ID` berupa **angka** (bukan email). Tanyakan ke admin Kintone.

---

## 🔄 Update

Tidak perlu apa-apa. Setiap kali Anda mengetik trigger word, Codex otomatis mengambil versi prompt terbaru.

---

## 🆘 Kalau ada masalah

| Masalah | Solusi |
|---|---|
| Ketik `automation` tapi Codex tidak mengerti | Tutup Codex (⌘ + Q), buka lagi, lalu mulai **session baru**. Kalau masih gagal, ulangi Langkah 3 |
| Muncul error koneksi / network / Kintone | Ulangi Langkah 4, tutup lalu buka lagi Codex. Kalau ditanya izin, pilih **Allow** |
| `command not found: git` | Jalankan `xcode-select --install` di Terminal, klik **Install**, lalu ulangi Langkah 3 |
| Hasil KPI 日々面談 = 0 | `KINTONE_USER_ID` salah. Harus angka, tanyakan ke admin Kintone |
| Masih bingung | Screenshot layar Anda dan kirim ke Sandy |
