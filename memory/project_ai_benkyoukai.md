---
name: project-ai-benkyoukai
description: "Sandy jadi pembicara benkyoukai AI internal Funtoco — seri 3 sesi, materi & deck ada di ~/Claude/benkyoukai-ai"
metadata: 
  node_type: memory
  type: project
  originSessionId: 52e79bdd-de0f-47f3-b710-121b6955024b
  modified: 2026-08-13T18:35:38.882Z
---

Sandy ditunjuk jadi pembicara 社内AI勉強会 (study session AI internal) di Funtoco, seri **3 sesi**:

- **第1回 — 2026-07-30**: 「AIとは？」 (AI itu apa / 自動化とは / プロンプトの作り方) — deck 40 slide **sudah selesai**
- **第2回**「AIを仕事で使う方法 ── つなげる技術」— **sedang dibangun**, 15 slide
  `1DMwRPM5HxzES6wnoQ0Cvxgn6ke8q0BFt7apyJDsrdFw` (社内AI勉強会_第2回 v0.1)
  Isi atas permintaan peserta: 3つの入り方 / アクセス権限 / API / MCP / connector standar (dulu Zendesk連携) / 誰が何をやるか
  **Section Zendesk連携 (5 slide) DIHAPUS TOTAL** atas permintaan user ("slide 13 kyk pengulangan part 1") — diganti section baru **「自分で作らなくていい連携」** (3 slide, posisi 12-14, sebelum slide penutup):
  - Slide 12 (divider, objectId `SLIDES_API399107350_0`): 「自分で作らなくていい連携」／Claude・Codexにある標準connector
  - Slide 13 (list, objectId `SLIDES_API1482615389_0`): 「標準で用意されているconnector」. Intro 2 baris (objectId `SLIDES_API1482615389_4`) mendefinisikan connector dan menyambungkan ke API+MCP yang sudah diajarkan: 「connectorとは、あらかじめ用意された「つなぐ部品」のこと。connectorの中身はMCP。その下で、APIが働いています。」 — versi final setelah 2x revisi: (1) "中身は…APIとMCPそのものです" ditolak karena mengesankan API "ada di dalam" connector, padahal API itu servis eksternal independen (Gmail API dsb, bukan bagian dari connector); (2) "set/paket API+MCP" juga ditolak karena mengesankan API-MCP itu 2 komponen SEJAJAR, padahal hubungannya bertingkat (API duluan ada & berdiri sendiri, MCP dibangun belakangan DI ATASnya — asimetris, sama seperti 土台/橋 di slide 10). Frasa "その下で〜働いています" dipilih karena otomatis membawa kesan bertingkat tanpa perlu dijelaskan ulang. Lalu Gmail/Google Calendar/Google Drive/Notion/Slack, masing-masing 1 baris "できること", DIBUNGKUS card abu-abu terang (`rgb(0.957,0.961,0.969)`, objectId `card1`..`card5`, harus di-`SEND_TO_BACK` setelah dibuat karena createShape baru selalu nempel di depan/menutupi teks yang sudah ada, DAN outline default-nya harus di-set `NOT_RENDERED` lewat `updateShapeProperties` — kalau tidak, border tipis default nampak nabrak/coret teks di sekitarnya) — awalnya plain text tanpa card, user bilang "kosongan polos banget", jadi pola card ini WAJIB dipertahankan kalau slide diedit lagi. Penutup: 「MCPサーバーを自分で書かなくても、もう使えるものがあります。」
  - Slide 14 (how-to, objectId `SLIDES_API1162378790_0`, duplikat dari slide09 APIトークンとは — pola ○+judul bold+detail abu-abu): 「使うには」— HANYA 2 item sekarang (ON/OFF切り替えるだけ／何を許可するか選べる). Item ke-3 (使うには、許可が要ります／リーダーかシステム管理者に、まず相談) DAN closing bar oranye DIHAPUS atas permintaan user — dianggap terlalu abstrak, user maunya bagian ini lebih teknis "cara connect"-nya. Sebagai gantinya ditambah **screenshot asli** menu Claude Connectors (bahasa Inggris, punya user sendiri, diupload user langsung ke chat), objectId gambar `image_5f91bd36-88a0-4f4b-b9bf-c6f108117928`, sumber gambar di Drive: `https://drive.google.com/uc?id=14_srPHI-cZ36B1Lt70Ycjtvm7wltdBSK&export=download` (permission "anyone with link", diupload via script bukan lewat Drive connector). User lalu MEMPERBESAR gambar ini manual langsung di Google Slides (jadi ~7.5×4.8in, geser ke kanan slide) — layout final jadi **2 kolom**: kiri = 2 item card yang di-*narrow*-kan (lebar ~4.15in, teks wrap 2 baris), kanan = screenshot besar + caption 「実際の画面（英語表示の例）」(objectId `textbox_58b8735b-55ba-4791-b88b-5bfce5670a02`) tepat di bawah gambar. Kalau user edit manual lagi di Slides langsung (bukan lewat sesi ini), SELALU re-fetch posisi elemen aktual (`get_slide`/script custom) sebelum reposisi apa pun — jangan asumsikan posisi lama masih berlaku.
  Slide 14 final: ditambah **card ke-3** (objectId `card3rect`/`card3icon`/`card3headline`/`card3detail`) 「カスタムMCPを追加できる／名前とURLを入力するだけ」 — untuk kasus connector yang tidak ada di list resmi. Plus **tip kecil paling bawah kolom kiri** (objectId `card14tip`, 11pt abu-abu, 1 baris) 「迷ったら、Claude Code／Codexに直接頼んでもOK」 — alternatif kalau bingung pakai menu, tinggal minta AI-nya install MCP lewat prompt langsung. Ruang vertikal di slide ini SANGAT mepet (card3 sengaja dibikin pendek 0.80in, teks card3detail diperpendek jadi 1 baris, supaya tip ini muat sebelum footer). Kalau mau nambah apa pun lagi di slide 14, kemungkinan perlu geser/kecilkan elemen lain dulu — jangan asal tambah tanpa cek ulang sisa ruang. Dokumentasi resmi Anthropic (support.claude.com/ja) dicek untuk verifikasi langkah — SEMUA artikelnya teks murni tanpa screenshot, jadi tidak ada sumber gambar resmi Jepang yang bisa dipakai; langkah resminya: カスタマイズ＞コネクタ→「+」→pilih dari daftar→「接続」→ikuti autentikasi.
  Konsep kunci slide ini: connector bawaan Claude/Codex = **contoh nyata MCP** yang sudah dibuat orang lain (persis metafora jembatan slide 10) — bukan konsep baru, sintesis dari 方式(biasanya OAuth)+API(tetap ada di baliknya)+MCP yang sudah diajarkan.
  Judul "実はもう、つながっている" sempat diusulkan untuk divider tapi **ditolak user** (gk suka), diganti "自分で作らなくていい連携" (opsi yang dipilih user dari 3 opsi).
  Slide 「権限には3つのレベル」 (①だれが使うか/②どうやって入るか/③どこまで触れるか) **dihapus** — dianggap kerangka abstrak yang tidak perlu, karena ②③ sudah dijelaskan lebih konkret di slide berikutnya (tabel ID+パスワード/トークン/OAuth, dan slide APIトークンの範囲)
  Slide tabel 「プログラムに、何を渡しているのか」 (objectId slide03) sudah direvisi final: ditambah subtitle 「AIをツールに『つなげる』には、プログラムに何かを渡す必要があります。」 (objectId slide03subtitle) menjawab kenapa kredensial diserahkan; kolom 評価 diperbaiki isi+warna — ID+パスワード=要注意(oranye/bold, elem032), APIトークン=安全(biru, elem036, sebelumnya tanpa warna evaluasi sama sekali), OAuth=比較的安全(biru, elem040, tidak diubah). Hindari kata "危険" untuk評価 — user anggap konotasinya terlalu negatif, pakai "要注意" sebagai gantinya. Kolom 「例」 juga direvisi jadi 「特徴」 (objectId `elem027`, di v0.1 DAN di `_Master`) — pola sama kayak masalah 評価: isinya baris1/2 (多くのシステムで使える／システムごとに発行する) itu karakteristik bukan contoh, cuma baris OAuth(→Google) yang contoh sungguhan; ganti header (bukan isi) karena tidak perlu ngarang contoh produk yang tidak nyambung ke ID+パスワード. Baris penutup diganti dari 「プログラムが持つのは『その人自身』です」(metafora, dianggap ambigu) jadi 「プログラムは『あなたに代わって』動けるようになります」(elem041).
  Slide 7「前回の在留カードの流れで見ると」(objectId slide08, elem096): klausa 「AIが文章を作ったのではなく、」dihapus dari baris penutup — struktur "bukan X tapi Y" bikin bingung karena X (文章を作った) tidak ada rujukan visual di diagram. Sekarang tinggal 「青い3つが、APIを使っているところです。AIがKintoneとDriveに、直接『お願いした』ということです。」 Pelajaran: kalau mau kontraskan sesuatu, pastikan sisi yang dinegasikan sudah muncul/tergambar duluan di slide, kalau tidak — buang saja negasinya, langsung pernyataan positif.
  Slide divider 5「APIとは？」(slide06) dan 9「MCPとは？」(slide10): ditambah caption kecil kepanjangan istilah — "Application Programming Interface の略" / "Model Context Protocol の略" (14pt, slate muted, di bawah subtitle).
  Slide 10「MCPとは、AIに『使い方』を教える共通の形」(objectId slide11): baris MCPがなかった/MCPがあると (elem122, elem125) dan penutup (elem126) diubah pakai analogi **jembatan** biar lebih gampang dimengerti orang umum — MCPがなかった: 「AIをKintoneにつなぐには → 橋を、そのたびに、イチから架けていた」; MCPがあると: 「誰かが橋を一度架ければ → あとは、みんなで渡るだけ」; penutup: 「MCPはAPIの代わりではありません。APIという土台の上に架けた、橋のようなものです。土台がなければ、橋も架けられません。」 (API=土台/pondasi, MCP=jembatan di atasnya — metafora konsisten sampai baris penutup).
  Slide 11「実例：こんなことができます」(objectId slide12, dulu judulnya "実例：この資料そのものです" — digeneralisasi atas permintaan user, jangan spesifik ke dokumen presentasi ini). Diagram AI→MCP→システム (generik, dulu →Google Slides) + 3 contoh konkret di bawahnya (Kintone/Google Drive/Gmail). Penutup final (elem140): 「人が頼む → AIがMCP経由で動く → システムに届く。それだけです。」 — sengaja pakai gaya panah yang sama dengan diagram di atasnya, dan eksplisit menaruh 人 di depan rantai karena diagramnya sendiri tidak menampilkan manusia sama sekali (AI→MCP→システム saja) — user minta ditegaskan posisi manusia di alurnya.
  Format tetap **berbagi pengetahuan**, bukan workshop — Sandy menolak PR & praktik, "praktiknya jalan sambil kerja"
- **第3回**: belum ditentukan

**Why:** Seri berlanjut, sesi 2 & 3 harus nyambung dengan janji yang sudah dibuat di deck sesi 1 (PR, alur レベル0〜3, 「5点セット」).

**How to apply:**

Folder `~/Claude/benkyoukai-ai/`:
- `01_AIとは_台本ドラフト.md` — naskah/konten
- `01_AIとは_スライド構成書.md` — storyboard per-slide
- `build_deck.js` — generator pptxgenjs (jalankan `node build_deck.js`)
- `audit.js` — cek overflow/out-of-bounds/tabrakan footer (`node audit.js`)
- `preview.js` — pecah jadi 40 deck 1-slide untuk di-render QuickLook (mesin ini **tidak punya** LibreOffice/pdftoppm, python cuma 3.9 jadi validate.py skill pptx tidak jalan)

Konsep kunci yang dipakai sepanjang seri (jangan diganti di sesi 2/3):
- Metafora inti: **AI =「優秀だけど、うちを知らない新人」**, prompt = 指示書
- **プロンプトの5点セット**: ①誰として ②なぜ ③何を ④どう出す ⑤NG
- **自動化レベル Lv.0〜Lv.3**, aturan penutup: **「下書きはAI、責任は人間」**
- Warna: navy `1B2A4A` + oranye `F26C21` (belum dikonfirmasi warna brand resmi Funtoco)
- **Font `Noto Sans JP`** — Sandy presentasi dari **Google Slides di browser** (tidak punya PowerPoint/Keynote di Mac-nya), dan Noto Sans JP tersedia native di Slides

**Sumber kebenaran sejak 2026-07-29 = file Google Slides**, bukan lagi `build_deck.js`:
`1c2VW9kCspLw2_ZSKXUgixdkaAz1L-i82ZBwDtebXkWk` — 「社内AI勉強会_第1回_AIとは」 (native Slides, hasil konversi dari pptx v1)

**Pola "_Master" untuk script romaji**: setiap sesi punya 2 file Slides — file kerja (`v0.1`/`v1.0`, terus diedit) dan **copy terpisah bernama `..._Master`** yang isinya sama tapi ditambah speaker notes script romaji per slide (untuk Sandy baca pas presentasi, karena dia bukan native Japanese reader). Kalau user bikin copy baru dan minta "script romaji kyk sebelumnya", itu maksudnya isi speaker notes di file `_Master` itu, formatnya:
- 1 script Node per file `_Master` (lihat `set_notes.js` utk 第1回, `set_notes2.js` utk 第2回), object `NOTES` dengan key = objectId slide, value = template literal romaji
- Header tiap slide: `【SLIDE N｜Judul singkat】yaku XX byou` (perkiraan durasi ucap)
- Stage direction Indonesia dalam `—— (...) ——`, tips penyampaian pakai `← catatan`
- Istilah Inggris/Latin yg sudah ada di deck (API, MCP, OAuth, connector, URL, ChatGPT dst) TETAP ditulis Latin, bukan diromajikan — romaji cuma untuk bagian Jepang, karena Sandy sudah bisa baca Inggris sendiri
- Duplikasi file via Drive "make a copy" mempertahankan objectId slide yang SAMA dengan file sumber (beda dgn `duplicate_slide` dalam 1 file yg generate ID baru) — jadi script NOTES bisa langsung reuse objectId yang sudah dikenal dari sesi kerja
- Selalu `node <script> --dry` dulu buat verifikasi pemetaan slide sebelum kirim beneran
- 第2回 v0.1_Master: `1HCFPWlr2-8DuVySseLP5xJ_9YIxqwHtU-mdvPxXhmtQ`, scriptnya `set_notes2.js`, 15 slide, per-slide DIBIKIN LEBIH SINGKAT dari pola 第1回 (user: "gk usah terlalu panjang2")
Claude mengedit langsung lewat connector [[reference_google_slides_mcp]]. `build_deck.js` jadi arsip/referensi koordinat saja — jangan regenerate lalu upload, itu akan menimpa editan di Slides.

Hasil konversi pptx→Slides ternyata bagus: emoji 💬 tampil normal, font tersubstitusi rapi, layout utuh. Jadi file `_v2.pptx` (Noto Sans JP + shape vektor) **tidak jadi dipakai** — perbaikan itu tidak diperlukan di Slides.

Gotcha teknis `mcp__google-slides__batch_update` (mahal kalau lupa):
- `createShape` MENGABAIKAN `elementProperties.size` custom — shape baru selalu dibuat base 3.000.000×3.000.000 EMU apa pun size yang dikirim. Ukuran akhir HARUS diatur lewat `transform.scaleX/scaleY` (scaleX = target_width_EMU/3000000, scaleY = target_height_EMU/3000000), sama seperti pola yang dipakai di seluruh deck ini (semua elemen existing pun begitu — bukan cuma sisa konversi pptx). Kalau lupa dan pakai scaleX=scaleY=1 dengan size custom, box jadi kotak default 3.28in×3.28in → teks wrap tidak semestinya.
- Selalu cek hasil layout dengan `get_thumbnail` (lalu buka URL-nya di browser & screenshot) setelah createShape/updatePageElementTransform — jangan cuma percaya dump teks, karena overlap/wrap tidak kelihatan dari situ.
- `duplicate_slide` MENGABAIKAN parameter `insertionIndex` — hasil duplikat selalu nempel tepat setelah slide sumbernya, apa pun index yang dikirim. Kalau butuh posisi lain, duplicate dulu (di mana pun dia jatuh), lalu panggil `reorder_slides` dengan array LENGKAP semua slideId presentasi dalam urutan final yang diinginkan.
- `createShape` (ROUND_RECTANGLE dsb) hasilnya punya OUTLINE/BORDER default yang kelihatan (bukan invisible) — beda dari shape yang sudah ada di deck lama (yang outline-nya `propertyState: NOT_RENDERED`). Kalau bikin card/box baru buat background dekoratif, WAJIB `updateShapeProperties` dengan `outline: {propertyState: "NOT_RENDERED"}`, kalau tidak border tipisnya bisa nampak nabrak/coret elemen teks di sekitarnya walau posisinya sebenarnya tidak overlap.
- **Cara masukkan gambar/screenshot lokal ke deck Slides** (dipakai untuk screenshot Connectors di slide 14): JANGAN coba base64-encode file lalu tempel manual ke tool call — file >20KB langsung kena limit token Read tool dan retype manual berisiko korup. Cara yang benar: pakai script Node reusing auth `~/.mcp-google-slides/credentials.env` + `~/.google-slides-mcp/tokens.json` (scope-nya sudah termasuk `drive.file`, cukup untuk upload+set permission), panggil `drive.files.create` dengan `media.body: fs.createReadStream(path)` (Bash baca file langsung dari disk, TIDAK lewat context Claude sama sekali), lalu `drive.permissions.create({fileId, role:'reader', type:'anyone'})` supaya publik-view, ambil `webContentLink` (format `https://drive.google.com/uc?id=FILEID&export=download`), baru itu dipakai sebagai `imageUrl` di `mcp__google-slides__add_image`. Google Drive Desktop app di Mac ini TIDAK selalu jalan (`ps aux` kosong) — jangan andalkan local-sync folder untuk ini.
- Setelah insert/delete/reorder slide, nomor halaman (elemen teks statis pojok kanan bawah, x>10in) TIDAK auto-update — harus di-fix manual satu-satu ke urutan 1..N. Warna nomor halaman beda tergantung background: slide gelap (divider/title/closing) pakai slate terang `{0.36,0.42,0.53}`, slide putih pakai abu `{0.439,0.475,0.541}` — cek dulu slide-nya gelap/putih sebelum apply style.

Gotcha teknis pptxgenjs (mahal kalau lupa):
- Di mode array-of-runs, `\n` **tidak** bikin line break — wajib `breakLine: true` per run
- Font Jepang merender salah kalau `「` atau `──` langsung diikuti huruf Latin/angka (mis. 「AIが…, ── 5点) — sisipkan kata Jepang dulu di depannya
- Jangan pakai emoji di deck (💬 dll) — ganti shape vektor (`wedgeRoundRectCallout` dsb)
- Mesin ini tidak punya Noto Sans JP, jadi preview lokal tampil serif — di Google Slides tetap sans-serif

Prinsip revisi yang berulang muncul dan disepakati Sandy:
- **Jangan menaruh klaim yang bisa dibantah peserta dari HP.** Slide 得意・苦手 dihapus karena 4 dari 6 item "AI tidak bisa" sudah usang (計算, 最新情報, dll). Slide ハルシネーション diselamatkan dengan mengubah bingkai dari "AI salah" jadi "kamu tidak tahu jawabannya dari mana".
- Hindari bahasa yang terkesan memerintah/mengeksploitasi (`〜て帰ってください`, `24時間働ける`, `文句も言わない`) — sensitif karena Funtoco justru melindungi pekerja asing.
- Angka 在留カード更新 `従来 約10分 → 現在 約2分` adalah **estimasi dari langkah kerja, bukan pengukuran**. Kalau ditanya, jawab 「体感です」.

Lihat juga [[reference_kintone_apps]] dan [[reference_zairyu_card_update]] — dipakai sebagai contoh kasus di deck.
