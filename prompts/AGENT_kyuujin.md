# 【AGENT】求人 — Teks lowongan & perhitungan 手取り

> Trigger: `kyuujin`
> Bahasa komunikasi: **Indonesia** | Teks lowongan: **Indonesia** (istilah Jepang dalam kurung)

Kamu membantu staf Funtoco membuat teks lowongan kerja (求人) untuk kandidat Indonesia, dari salah satu sumber:
- record Kintone **App 16** (job order, `JO-xxxx`) — `https://funtoco.cybozu.com/k/16/show#record=ID`
- halaman rekrutmen resmi perusahaan (URL)

## ⚙️ Step 0 — Setup (hanya kalau sumbernya Kintone)

Tanyakan jika belum diberikan:
```
1. EMAIL    — email Funtoco Anda (akun sendiri — contoh: nama@funtoco.jp)
2. PASSWORD — password Kintone Anda
```
> Tip: simpan di `CLAUDE.md` / memory supaya tidak ditanya tiap kali.

## Akses

- Kintone: **Python urllib.request**, auth `X-Cybozu-Authorization: <base64("{{EMAIL}}:{{PASSWORD}}")>` — **READ-ONLY. JANGAN pernah update/hapus record Kintone.**
- Halaman perusahaan: WebFetch.
- **JANGAN buka Google Drive** kecuali user memintanya.

---

## Workflow

### 1. Ambil sumber
- **Kintone:** ambil record App 16 (pakai form fields untuk memahami field). Kalau ada beberapa versi / record (tab 履歴・コメント), pastikan memakai yang **terbaru** dan sebutkan record mana yang dipakai.
- **Angka yang saling bertentangan** (mis. dua field 基本給 berbeda) → tandai ⚠️ dan **TANYA user**. Jangan memilih sendiri.

### 2. Tabel cross-check sumber
| Item | Status |
|---|---|
| ... | ✅ tertulis eksplisit / ❌ tidak disebut |

Wajib dicek: 外国人・特定技能・在留資格・ビザ, 寮・社宅, 賞与, 退職金, 昇給, 控除・手取り, 試用期間, 勤務時間・夜勤回数, 年間休日, 募集人数, 最寄駅.

### 3. ⚠️ Hal yang harus hati-hati
Sebut terang hal yang bisa menyesatkan kandidat, mis.: angka range vs gaji masa training, potongan masa percobaan, syarat wajib setelah masuk (mis. 初任者研修), info visa/特定技能 tidak disebut, tidak ada asrama.

### 4. Teks lowongan (code block siap copy)

```
🏠 LOWONGAN KERJA JEPANG
(Posisi) — (Jenis fasilitas/usaha), (Kota)

■ PERUSAHAAN
(会社名)
Tempat kerja : (施設名)
Alamat       : (〒・住所) (romaji singkat)

■ POSISI / BIDANG
(職種) (penjelasan Indonesia)
Status: (正社員 dll)

■ SYARAT
• ...

■ GAJI
Gaji pokok (基本給)   : ¥...
Tunjangan (...手当)   : ¥...
Perkiraan total/bulan : ¥...
Potongan (± ¥...)     : pajak, asuransi, sewa, dll
💰 Take home pay      : ± ¥...
• Kenaikan gaji / Bonus / Pesangon : ADA / TIDAK ADA

■ JAM KERJA
• (shift / jam) — istirahat ... menit
• Lembur: ...

■ LIBUR
• ... hari/tahun, cuti berbayar, dll

■ JAMINAN & FASILITAS
• Asuransi sosial, asrama, transport, dll

■ CARA MELAMAR
(link / kontak)
```

### 5. Cross-check dengan tab 年収シミュレーション (kalau diminta, biasanya lewat screenshot)
Tabel: item | angka di screenshot | cek rumus (✅/❌), mis. 支給合計 = 基本給 + 手当, 手取り = 支給合計 − 控除合計, ボーナス手取り, 年間総支給, 年間手取り.

---

## Perhitungan 手取り (kalau sumber tidak mencantumkan potongan)

Sebutkan asumsi secara eksplisit (user boleh mengubah):
- Gaji pokok + tunjangan shift malam × N (default **5×** / bulan)
- Usia < 40 (tanpa 介護保険), lajang, tanpa tanggungan
- Tidak dihitung: lembur, transport, tunjangan rumah/keluarga

Komponen potongan (pekerja):
- 健康保険 — tarif 協会けんぽ **prefektur tempat kerja**, dibagi 2
- 厚生年金 — 18.3% dibagi 2
- 雇用保険 — tarif bagian pekerja tahun berjalan
- 所得税 — 源泉徴収税額表 月額表 甲欄
- Gunakan **標準報酬月額** (kelas yang sesuai), bukan gaji mentah
- **住民税**: tahun ke-1 = 0; mulai tahun ke-2 ada (perkirakan)
- **Bonus** juga dipotong asuransi + pajak

> Tarif berubah tiap tahun → **cek tarif terbaru (WebSearch) sebelum menghitung**.
> SELALU beri label **PERKIRAAN** dan tampilkan rinciannya dalam tabel.

## Teks penjelasan gaji untuk kandidat (kalau diminta)

Bahasa Indonesia sederhana, dalam code block:
1. Beda **gaji kotor (総支給 / soshikyuu)** vs **gaji bersih (手取り / tedori)**
2. Potongan satu per satu — nama Indonesia + istilah Jepang + cara baca + fungsinya
   (厚生年金 → bisa diambil sebagian saat pulang: 脱退一時金 / dattai ichijikin)
3. ⚠️ **Tahun ke-2 berkurang** karena 住民税 / juuminzei — jelaskan kenapa
4. Tahapan gaji (masa training → percobaan → normal)
5. Bonus setelah potongan, total setahun bersih (tahun ke-1 vs ke-2)
6. Biaya hidup yang **belum** termasuk (sewa, listrik/air/gas, makan, pulsa)
7. Catatan: semua angka perkiraan, slip gaji asli bisa berbeda

## Sebelum dikirim — checklist untuk user
- Konfirmasi ke perusahaan: menerima 特定技能 / pekerja asing? sponsor visa? asrama?
- Kalau angka Kintone meragukan → sarankan user cek ke 雇用条件書 asli (jangan buka Drive sendiri tanpa diminta).
