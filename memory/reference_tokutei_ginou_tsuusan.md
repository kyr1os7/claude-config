---
name: reference-tokutei-ginou-tsuusan
description: "Cara baca sisa kuota 特定技能1号 (60 bulan) di Kintone App 30, termasuk field 現在の年/現在の月 yang harus diisi manual"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 874789db-3152-47ad-8541-ae7830072e90
  modified: 2026-08-05T01:12:04.915Z
---

Sisa kuota 特定技能1号 (batas 60 bulan seumur hidup, akumulatif lintas perusahaan) dibaca dari App 30 マスタ_人材管理 — bukan App 13.

**Dua angka hasil, letaknya tepat di bawah tabel 職歴一覧:**
- `特定技能勤務年` → label sebenarnya **特定技能勤務月数** (satuan BULAN, bukan tahun — namanya menyesatkan)
  = `SUM(特定技能勤務月) + SUM(nextWorkGapCountedMonths)`
- `特定技能勤務月_0` → label sebenarnya **特定技能残り月数** = `60 − 特定技能勤務月数`

**Field pendukung (tidak boleh diubah tanpa instruksi):**
- `初回許可された日` = tanggal pertama kali 特定技能1号 diizinkan
- `終了予定日` = 初回許可された日 + 5 tahun = tanggal mati kuota

**⚠️ Jebakan utama — `現在の年` / `現在の月`:**
Dua NUMBER field ini adalah titik waktu acuan rumus, dan **diisi MANUAL** (tidak auto-update).
Letaknya di grup lipat **「特定技能通算」** di paling bawah form App 30, default **tertutup**, jadi jarang terlihat.

Akibatnya angka 残り月数 berhenti di bulan yang terakhir diisi. Per Agustus 2026, nilai antar record berbeda-beda (2026/6, 2026/7, 2026/8) karena hanya terisi kalau ada yang kebetulan membukanya. Contoh nyata: Asmariah terbaca 41ヶ月 padahal sebenarnya 42ヶ月.

**Selalu cek 現在の年/現在の月 dulu sebelum melaporkan angka 残り月数.** Kalau basi, minta izin dulu ke Sandy sebelum memperbaruinya — lihat [[feedback-jangan-ubah-field-tak-disebut]].

**Catatan 分野介護:** 介護 TIDAK punya 特定技能2号. Setelah 60 bulan habis, satu-satunya jalur lanjut adalah lulus 介護福祉士国家試験 → 在留資格「介護」. Syaratnya 実務経験3年 + 介護福祉士実務者研修 (didaftarkan di App 214, ada di dropdown 資格名). Ujian tiap Januari, hasil akhir Maret — jadi hitung mundur dari 終了予定日.

Terkait: [[reference-kintone-apps]]
