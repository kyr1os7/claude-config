---
name: project-zendesk-ai-agent-escalation
description: Status desain Zendesk AI agent Funtoco (semua percakapan berakhir eskalasi + tag + assign ke 支援担当) dan masalah terbuka per 2026-10-05
metadata:
  node_type: memory
  type: project
  originSessionId: 8e1b268e-11a0-46ec-b462-040a962bc736
  modified: 2026-10-06T08:06:13.975Z
---

Desain: semua use case AI berakhir di eskalasi async (Forward to an agent, Escalate to team = group ID 5704360793630 "AI Agent 引き継ぎ"), diberi tag `async_ai_resolved` / `async_ai_unresolved` lewat configured action (Sunshine Conversations). Tujuan akhir: tiket editable supaya staf bisa isi 【対応詳細】 + analisis pertanyaan. 17 trigger per 支援担当 ("xxx（AI Agentから引き継ぎ）", kategori AI agents, dibuat via API 2026-10-05) meng-assign tiket ke 担当 berdasarkan field user shien_tanto_name + tag async_ai_*.

**Why:** tiket AI-only read-only, trigger tidak jalan di situ; satu-satunya jalan agar editable adalah eskalasi (passControl).

**Masalah terbuka (2026-10-05):**
1. BSAT yang diabaikan pekerja TIDAK pernah tereskalasi: dialogue BSAT menunggu klik tanpa batas waktu; tiket akhirnya Solved AI-only read-only (terukur 1–100 menit, dokumentasi ±2 jam).
2. Procedure Knowledge reply: cabang "no response for N minutes" tidak punya timer yang berfungsi (tes 5 menit, 10 menit, 1 menit tidak tereskalasi). Cabang gratitude berfungsi (langsung ke 確認用エスカレーション).
3. Trigger BSAT (Settings Collect BSAT) dan cabang diam saling meniadakan: BSAT muncul mengambil alih percakapan. Escalation tidak bisa ditaruh sebelum BSAT question (block abu-abu).
4. KEPUTUSAN user: tidak mau trigger End Session otomatis; End Session dilakukan MANUSIA setelah selesai menangani. Konsekuensi: setelah eskalasi, pesan pekerja berikutnya masuk ke tiket (staf), AI diam sampai staf End Session. Jadi desain "eskalasi langsung setelah tiap jawaban" tidak cocok; renzoku harus dijawab AI sebelum eskalasi (eskalasi di ujung: gratitude/BSAT).
5. Tag dobel: conversation tags menumpuk di thread Facebook; diperbaiki dengan configured action "Overwrite conversation tags" (belum diverifikasi).
6. (SELESAI, dikonfirmasi user) Omnichannel routing membagikan tiket tanpa assignee ke agent online; sudah ditangani user.

**Desain terbaru (2026-10-06):** Knowledge reply Procedure disederhanakan (Collect parameter response_language → Search → Answer; No knowledge → Default reply). Pertanyaan penutup "ada pertanyaan lain?" harus berupa step "Generate answer" (kirim pesan, tidak menunggu), BUKAN "Ask question" (menyerap balasan sebagai parameter) dan instruksi di step Search tidak berpengaruh ke teks jawaban (terbukti tes). Sinyal "selesai" ditangkap use case terpisah "感謝・会話終了（確認用エスカレーション）" (Escalation + tag resolved); 簡易返信・確認のみ untuk ok/ya polos. BSAT trigger hanya kondisi "knowledge answer shared", 180 detik (kesempatan kedua). End Session tetap manual.

**Tes lolos (2026-10-06):** terima kasih/selesai → eskalasi resolved; "oke kak" → eskalasi resolved; renzoku satu percakapan; BSAT muncul 3 menit setelah diam; mengetik "tidak, terima kasih" saat BSAT muncul → tertangkap 感謝・会話終了, eskalasi resolved. Masih tersisa: publish Procedure versi terakhir (Generate answer satu kalimat; copilot cenderung mengubahnya jadi Ask question atau menjawab ulang), tes 16 trigger assign 担当 lain, pantau view AI Agent解決済み (celah pekerja diam + BSAT diabaikan).

**Daftar terbuka saat user istirahat (2026-10-06 malam):**
- Procedure Knowledge reply sudah dikembalikan & dipublish ke Version 15 (Search = instruksi bahasa; Answer; Generate answer satu kalimat penutup). Langkah Collect parameter `active_language` (V16) terbukti tidak berpengaruh, dibuang.
- BAHASA: pesan tunggu + jawaban utama knowledge tetap Jepang untuk pesan Indonesia; pertanyaan penutup & pesan use case sudah ikut bahasa pekerja. Sudah dicoba: instruksi di Search, response_language lebih tegas, step active_language, tambah bahasa aktif di akun (Burmese/English/Indonesian/Nepali). Dropdown Language di profil user hanya Jepang dan "-" (tak bisa kosong); tooltipnya bilang itu bahasa UI Support. Dugaan: komponen bawaan pakai active_language Zendesk (sticky). Langkah berikut: tanya support Zendesk.
- RESEND: SELESAI (dikonfirmasi user 2026-10-07, "done clear"). Catatan lama: balasan AI muncul di tiket tapi bertanda "Resend" (gagal terkirim ke Facebook); panel Test AI agent juga tidak membalas. Belum didiagnosis. Cek: pesan error di ikon seru, koneksi Facebook Page (Admin Center → Channels → Messaging and social), status.zendesk.com, tes balasan manual dari tiket, Change log AI agent.
- 16 trigger assign 担当 lain sudah dites, aman (dikonfirmasi user 2026-10-07). Masih: pantau view AI Agent解決済み. Temuan: pesan baru pekerja (mis. "selamat pagi") masuk ke tiket eskalasi lama yang sesinya masih Active (End session manual belum dilakukan) → langsung ke staf, AI diam. TERKONFIRMASI (user lupa End session; setelah di-End, tes ulang normal, tidak ke hikitsugi). (Pesan penutup satu kalimat Version 15 sudah terbukti, dicoret.)
- SELESAI (dikonfirmasi user): Failed escalation response + Escalation fallback + nomor darurat, verifikasi terjemahan Nepali/Myanmar, assign tiket lama manual. Aturan End session manual oleh staf sudah aturan lama kaisha. DISKIP: update flowchart artifact, checklist 支援担当名.
- SELESAI (2026-10-07): use case baru "休暇・有給の個別相談" → langsung ke 担当 (dipicu laporan rekan: AI menjawab umum soal cuti pribadi; pesan pekerja cuma "有" jadi salah paham). Celah: pesan sangat pendek tetap bisa salah klasifikasi; BSAT 180 dtk bisa memotong pertanyaan balik AI.
- Belum dikerjakan: isi 対応詳細 otomatis (automation Claude+API), AI hanya di luar jam kerja (Availability).

**How to apply:** saat user lanjut soal Zendesk AI agent, mulai dari daftar masalah ini. Pilihan desain yang sedang dipertimbangkan: gratitude→eskalasi langsung + BSAT trigger ON (celah: BSAT diabaikan jadi AI-only), atau eskalasi langsung setelah jawaban (renzoku pecah jadi beberapa tiket). Token Zendesk API ada di reference_kintone_auth.md (read ok; write butuh izin eksplisit user).
