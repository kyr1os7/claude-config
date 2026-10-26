# Panduan Funtoco Automation di Claude (Mac)

Panduan ini untuk rekan kerja yang memakai **Claude** di **Mac**.
Waktu setup: **±10 menit, cukup sekali**.

Setelah selesai, Anda cukup mengetik satu kata di Claude (misalnya `hibimendan`), dan Claude akan mengerjakan automation-nya.

> ⚠️ **Harus pakai tab "Code" di app Claude (Claude Code), bukan chat biasa.** Chat biasa tidak bisa mengakses Kintone dan Zendesk dari komputer Anda.

> 💡 Pakai Codex (ChatGPT)? Lihat [panduan Codex](../codex/SETUP_CODEX.md).

---

## ✅ Siapkan dulu

- [ ] Mac dengan koneksi internet
- [ ] Akun Claude berbayar (Pro / Max / Team). Kalau belum punya, tanyakan ke Sandy
- [ ] Email Funtoco `@funtoco.jp` + password Kintone
- [ ] *(Hanya untuk `hibimendan` / `blastmessage`)* Zendesk API token → minta ke Sandy lewat chat pribadi

---

## Langkah 1 — Install app Claude

1. Download app **Claude** untuk Mac dari situs resmi: https://claude.ai/download
2. Buka file yang terdownload, lalu drag ikon **Claude** ke folder **Applications**.
3. Buka app Claude, lalu **login** dengan akun Claude Anda.

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
bash <(curl -fsSL https://raw.githubusercontent.com/kyr1os7/claude-config/main/claude/setup_claude.sh)
```

**Berhasil kalau** muncul tulisan seperti ini di bagian akhir:

```
Bootstrap ditambahkan ke /Users/namaanda/.claude/CLAUDE.md
Selesai.
```

> 💡 Kalau muncul *"Bootstrap sudah ada … tidak diubah"*, artinya sudah pernah di-setup sebelumnya. Itu juga OK, lanjut saja.

---

## Langkah 4 — Sambungkan Google (Gmail, Drive, Calendar)

Beberapa automation perlu mengakses Google akun `@funtoco.jp` Anda.

1. Di app Claude, klik **nama/ikon akun** Anda di pojok kiri bawah → **Settings**
2. Buka menu **Connectors**
3. Sambungkan (**Connect**) ketiganya dengan akun `@funtoco.jp`:
   - **Gmail**
   - **Google Drive**
   - **Google Calendar**
4. Ikuti layar login Google sampai selesai.

> 💡 Hanya butuh `hibimendan` / `visastatus` / `kyuujin`? Langkah ini boleh dilewati dulu.

---

## Langkah 5 — Tes pertama

1. Tutup app Claude sepenuhnya (⌘ + Q), lalu buka lagi
2. Klik tab **Code** di bagian atas
3. Buat **session baru**. Kalau diminta memilih folder, pilih folder mana saja (misalnya **Documents**)
4. Ketik:
   ```
   automation
   ```
   → Claude akan menampilkan daftar semua trigger word. **Artinya setup berhasil 🎉**
5. Coba automation yang aman (hanya membaca data, tidak mengubah apa pun):
   ```
   visastatus
   ```
   Claude akan menanyakan email dan password Kintone Anda. Setelah diisi, ketik:
   ```
   cek
   ```
   → Claude menampilkan perubahan status visa untuk record Anda.

> 💡 Kalau Claude minta izin (misalnya *"Allow fetch?"* atau *"Allow this command?"*), pilih **Allow**.

Kalau langkah ini jalan, Anda siap memakai semua automation.

---

## 📋 Cara pakai sehari-hari

**Selalu mulai dari session baru di tab Code**, lalu ketik trigger word-nya. Setelah itu ikuti perintah yang diminta Claude (misalnya `CEK`, `MENDAN`, `laporan hari ini`).

| Ketik | Untuk apa | Butuh |
|---|---|---|
| `hibimendan` | 日々面談 — dari Zendesk / manual → Kintone | Zendesk token |
| `visastatus` | Cek perubahan status visa (App 50) | — |
| `kyuujin` | Teks lowongan + hitung 手取り | — |
| `teikimendan` | 定期面談記録 → Kintone | Google Drive |
| `zairyucard` | Update 在留カード → Kintone + Drive | Google Drive |
| `shoruikakunou` | 書類格納 — rename & simpan dokumen | Google Drive |
| `gyomuhoukoku` | 業務報告 harian + draft email | Google Calendar + Gmail |
| `mendanyoyaku` | Update tanggal dari email reservasi | Gmail |
| `hikkoshi` | Memo Calendar + rute mobil 引越し | Google Calendar |
| `blastmessage` | Kirim pesan massal FB / LINE | Ekstensi Claude in Chrome (hubungi Sandy) |
| `automation` | Lihat semua daftar di atas | — |

"Google Drive / Gmail / Google Calendar" = sudah disambungkan di Langkah 4.

---

## 💾 (Opsional) Supaya tidak ditanya data terus

Di Terminal, ketik ini lalu **Enter**:

```bash
open -e ~/.claude/CLAUDE.md
```

File akan terbuka di TextEdit. Scroll ke bagian **Data Pribadi**, isi nama, email, dan `KINTONE_USER_ID`, lalu simpan (⌘ + S).

> 🔒 **Jangan tulis password atau token di file ini.** Ketik saja saat Claude bertanya.
> `KINTONE_USER_ID` berupa **angka** (bukan email). Tanyakan ke admin Kintone.

---

## 🔄 Update

Tidak perlu apa-apa. Setiap kali Anda mengetik trigger word, Claude otomatis mengambil versi prompt terbaru dari GitHub.

---

## 🆘 Kalau ada masalah

| Masalah | Solusi |
|---|---|
| Ketik `automation` tapi Claude tidak mengerti | Pastikan Anda di tab **Code** (bukan chat). Tutup Claude (⌘ + Q), buka lagi, mulai **session baru**. Kalau masih gagal, ulangi Langkah 3 |
| Tab **Code** tidak ada | Update app Claude ke versi terbaru, dan pastikan akun Anda berbayar |
| Error saat akses Gmail / Drive / Calendar | Cek lagi Langkah 4, pastikan connector tersambung dengan akun `@funtoco.jp` |
| Hasil KPI 日々面談 = 0 | `KINTONE_USER_ID` salah. Harus angka, tanyakan ke admin Kintone |
| Masih bingung | Screenshot layar Anda dan kirim ke Sandy |
