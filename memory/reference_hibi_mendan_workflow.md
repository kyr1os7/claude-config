---
name: reference-hibi-mendan-workflow
description: "Aturan operasional sistem CEK/MANUAL untuk input 日々面談 ke Kintone App 98 (trigger \"hibimendan\")"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 3b378773-03be-4a05-826c-89ce8a01ff35
  modified: 2026-10-23T08:47:00.305Z
---

Sistem otomatis input laporan 日々面談 ke Kintone App 98, dengan 2 trigger: **CEK** (ambil dari Zendesk) dan **MANUAL** (input teks langsung). Full prompt tersinkron di GitHub public `kyr1os7/claude-config/prompts/AUTO_hibi_mendan.md` (trigger word: `hibimendan`).

**Why:** Dibangun bertahap selama sesi panjang, banyak koreksi dari user yang harus diingat supaya tidak diulang kesalahan yang sama.

**How to apply:**

1. **CEK** = fetch SEMUA ticket Zendesk assignee=staff, **hari ini saja (JST)** — cek `created_at` tiap comment, bukan cuma `updated_at` ticket (1 ticket bisa berisi chat dari beberapa hari). Tidak harus subject 【日々面談】 — semua ticket valid apapun judulnya. Tandai ⚠️ kalau ticket itu kelihatan lanjutan dari hari sebelumnya yang sudah pernah di-input, lalu tampilkan list untuk dikonfirmasi user sebelum input (user boleh skip).
2. **MANUAL** = format `MANUAL\nNAMA\nisi soudan` → langsung input tanpa konfirmasi.
3. **面談日** = tanggal user kasih perintah (JST), BUKAN system clock kalau user kasih tahu beda. Selalu konfirmasi kalau ragu — user tinggal di Jepang.
4. **対象四半期**: bulan 1-3=第1, 4-6=第2, 7-9=第3, 10-12=第4, selalu sertakan tahun (`2026年第2四半期`). Field ini **kehapus otomatis oleh Kintone automation setelah create** → WAJIB lakukan `kintone-update-records` terpisah segera setelah `kintone-add-records` untuk isi ulang, cek revision naik jadi 2.
5. **tableStorageDaily** bukan field native — cuma `MULTI_LINE_TEXT` berisi JSON, UI render via JS custom. Format: `[{"dai":"日々の対応報告","chu":"<中項目>","shou":[],"notes":"<isi JP>","funbaseVisibility":"pending","salesReviewReasons":[],"salesReviewMemo":""}]`. Field flat duplikatnya: `tableStorageDaily_大項目/中項目/小項目/内容`.
6. **FunBase表示 mapping** (raw JSON → UI dropdown): `"visible"`→表示する, `"pending"`→営業担当確認, (表示しない belum diketahui raw value-nya). **Default saat ini = `"pending"`** (営業担当確認) — diubah dari `"visible"` atas instruksi user 2026-06, terverifikasi visual langsung di Kintone oleh user.
7. Field standar lain: `interviewPlace`="Web", `interviewMethod`=["メール","オンラインMTG"], `timeInterview`="日々の面談", `personInCharge`(テンプレート)="支援担当". Lookup WOID/HRID/COID dari App 13 by `name`. **Kasus khusus 面会/kunjungan langsung** (mis. 留置場): `interviewPlace`="訪問", `interviewMethod`=["対面"].
7b. **Gaya bahasa 内容 (mulai 2026-10-20, record lama tidak diubah)** — dibaca pihak kaisha client → **gaya laporan 常体** (〜した／〜している／〜である, divariasikan: 説明した・案内した・確認した・〜と報告があった・〜予定である・〜とのことである). DILARANG です・ます. **Hindari 体言止め** (「〜について相談あり。」→「〜について相談があった。」). **〜済み maks 1x per laporan** (dulu overused). Boleh gabung 「〜し、〜した」. Contoh: `本人より、国民年金の免除手続きについて相談があった。必要書類と記入方法を説明し、提出先は市役所である旨を案内した。` (Aturan lama 2026-07 = 済み + 体言止め, sudah diganti.)
7d. **中項目 (`chu`) hanya dari daftar tetap (mulai 2026-10-23)**: 手続き関連／生活支援（居住）／生活支援（引越し）／生活支援（手続き）／生活支援（医療）／キャリア関連／給与関連／退職相談／仕事関連（労働条件）／仕事関連（業務内容）／ビザ申請__更新__在留カード受け取り／ビザ申請__更新__書類の確認／SIMカード・インターネット対応／郵便対応／その他. Jangan pakai 件名 ticket atau variasi baru (dulu ada ±10 record tidak seragam: ビザ更新対応, 病院対応, 面談日程調整 dll.; record lama tidak diubah). Daftar sama dengan skill shien-chan.
7c. **Format 内容 (mulai 2026-07-13)** — awali dengan judul dalam kurung 【】 lalu deskripsi: **`【<subject>】<deskripsi>`**. Subject = 件名 ticket Zendesk (untuk CEK) atau ringkasan topik (untuk MANUAL). Contoh: `【新在留カード受け取り】本人から送付された書類を確認し、申請受付番号について案内した。` Berlaku di `notes` (JSON) dan `tableStorageDaily_内容`.
8. **JANGAN edit/test coba-coba langsung di record yang sudah ada** tanpa izin eksplisit — kalau perlu verifikasi sesuatu, tanya user cara teraman dulu (insiden: pernah ditegur "jangan sembarangan" karena test value langsung di record live).
9. Setelah input, selalu kasih link record: `https://funtoco.cybozu.com/k/98/show#record=<ID>`.

Lihat juga [[feedback-up-github-flow]] untuk cara push update prompt ini ke GitHub.
