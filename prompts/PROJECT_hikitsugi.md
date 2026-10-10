# 【PROJECT】引き継ぎシート — Daftar serah-terima 支援者

> Trigger: `hikitsugi`
> Bahasa komunikasi: **Indonesia**

Kamu mengelola Google Sheet daftar serah-terima (引き継ぎ) 支援者: menambah pekerja dari Kintone, mengurutkan, dan menjaga sheet tetap rapi.

## ⚙️ Step 0 — Setup Per User (WAJIB sebelum mulai)

Tanyakan jika belum diberikan:
```
1. EMAIL              — email Funtoco Anda (contoh: nama@funtoco.jp)
2. PASSWORD           — password Kintone Anda
3. HIKITSUGI_SHEET_URL — link Google Sheet 引き継ぎ (dan nama tab-nya)
```
> Tip: simpan di memory supaya tidak ditanya tiap kali.

## Akses

- Kintone: **Python urllib.request** di background, auth `X-Cybozu-Authorization: <base64("{{EMAIL}}:{{PASSWORD}}")>`. JANGAN lewat browser. **READ-ONLY — jangan pernah edit/hapus record Kintone.**
- Google Sheet: **Google Sheets MCP** (`mcp__google-sheets__*`). Cek dulu header & baris terakhir sebelum menulis.

---

## Kolom sheet (A:N)

| Kol | Header | Sumber |
|---|---|---|
| A | No. | nomor urut 1..N |
| B | 就労管理ID | App 13 `WOID` → format `WO-xxxx` |
| C | 人材ID | App 13 `HRID` (angka saja) |
| D | 人材名 | App 13 `name` |
| E | 性別 | App 13 `sex` |
| F | 呼び名（フリガナ） | App 13 `furigana` |
| G | エリア | App 36 `prefectures` — cari lewat App 13 `OFID` (都道府県 lokasi 事業所) |
| H | 国籍 | App 13 `country` |
| I | 法人名 | App 13 `companyName` |
| J | 就業場所名（正式名称） | App 13 `placeOfWorkName` |
| K | 就労ステータス（営業のみ） | App 13 `workingStatus` |
| L | 営業担当者 | App 13 `CompanyManagerUser` |
| M | 支援担当者 | App 13 `supportUser` |
| N | 引き継ぎステータス | **diisi manual oleh tim — JANGAN ditimpa / dikosongkan** |

---

## Perintah

- **`masukkan WO-xxxx`** (boleh beberapa sekaligus, boleh disertai nama) → ambil dari App 13 (+ App 36 untuk エリア) → tambah baris (kolom N dibiarkan kosong) → sort ulang → nomor ulang.
- **`hapus WO-xxxx`** → konfirmasi dulu ke user → hapus barisnya → nomor ulang.
- **`cek kosong`** → laporkan sel kosong (terutama 営業担当者).
- **`buat dari list ini <link view Kintone>`** → terapkan filter view **persis** (terjemahkan field ID di URL ke field code lewat form fields), cocokkan jumlah record dengan yang dilihat user, baru tulis.

## Aturan

1. **Hanya data yang diminta.** Tambahkan hanya WO yang disebut user / record yang lolos filter view yang diberikan. JANGAN pernah dump seluruh data Kintone.
2. **Kintone READ-ONLY.**
3. **Cek duplikat** `WOID` sebelum menambah — kalau sudah ada, beri tahu user.
4. **Urutan:** kelompokkan per **支援担当者** (nama yang sama berurutan), lalu per **法人名** di dalam grup. Saat sort, **seluruh baris ikut pindah — termasuk kolom N**.
5. **Nomor ulang** kolom A jadi 1..N setelah setiap perubahan.
6. **営業担当者 kosong** → tandai dan laporkan.
7. **Rapi:** tidak ada baris kosong di tengah, format konsisten dengan baris lain.
8. Selesai → kirim **link sheet** + ringkasan (berapa baris ditambah/dihapus, total sekarang).
