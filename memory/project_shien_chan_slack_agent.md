---
name: project-shien-chan-slack-agent
description: "しえん-ちゃん = AI agent 支援担当 Funtoco di Slack yang dilatih Sandy; penilaian knowledge Sesi 1-2, 5 lapisan, roadmap use case, next step A/B/C"
metadata:
  node_type: memory
  type: project
  originSessionId: 20e01b5b-8397-4ef9-a090-3e366faaf0ab
  modified: 2026-10-10T08:43:16.395Z
---

**しえん-ちゃん** = AI agent internal Funtoco khusus pekerjaan 支援担当, berjalan di **Slack**, rencananya terhubung ke Kintone. Sandy bertugas melatihnya. Konsultasi awal: 2026-10-08 (session 【PROJECT】しえん-ちゃん).

## Bahan knowledge yang sudah ada
- Sesi 1: `Funtoco_支援業務ナレッジ_特定技能・在留・退職帰国.md` — pengetahuan 制度 (bertanggal 基準日, ada sumber resmi)
- Sesi 2: `Funtoco_AI_Agent_Knowledge_Session2.docx` — perilaku & batasan AI, alur 受付→ヒアリング→整理→報告→対応→改善確認, level トラブル, 共通指示文 (siap jadi system prompt)
- Backup kedua file: repo private `workspace/shien-chan/` (asalnya ~/Downloads)

## Celah yang ditemukan
1. Tidak ada contoh jadi (面談記録 / 業務報告 terisi & dianonimkan, termasuk contoh buruk + perbaikannya)
2. Eskalasi tanpa tujuan jelas (siapa, channel Slack mana, batas waktu)
3. Sesi 1 & 2 tidak sinkron (定期面談 本人+上司, syarat rekam/persetujuan online, 通報, 届出 14 hari, checklist 退職・帰国)
4. Tidak ada glosarium Funtoco (mis. 支援者 = pekerja asing yang didampingi — lihat [[funtoco-terminology]]) & peta field/app Kintone
5. Belum ada aturan bahasa pekerja / やさしい日本語
6. Belum ada aturan data pribadi di Slack

## Prinsip "melatih" = merawat 5 lapisan
Instruksi · Knowledge stabil · Data hidup (Kintone) · Playbook per tugas · **Evaluasi (paling penting, belum ada)**.
Mulai dari evaluasi: ±30 kasus nyata dianonimkan → jawaban ideal + hal terlarang → uji → perbaiki → ulangi; koreksi staf mingguan jadi knowledge baru. Knowledge dipecah per topik (基準日, sumber, pemilik). Contoh format: pack `~/Claude/retirement-trouble-agent`.

## Kintone
Mulai **read-only** dengan API token per app (App 30, 50, 98, 241, 258, 13, 264). Penulisan baru setelah stabil, pola draf → staf setujui → AI simpan.

## Roadmap use case
1. Risiko rendah: catatan/voice memo → draf 面談記録/業務報告; Q&A 制度 + 基準日; ringkasan persiapan 面談
2. Pengingat proaktif (butuh Kintone): 定期面談 3 bulan, target 日々面談, 在留期限, sisa 通算5年, 届出 14 hari; checklist 退職・帰国; laporan KPI mingguan
3. Komunikasi: draf pesan ke pekerja dalam bahasanya + terjemahan balik; draf ke perusahaan; triase (通報, darurat)
4. Lanjutan: profil per perusahaan, cek kelengkapan dokumen 更新/変更, onboarding staf baru

## Status / next step
Belum dipilih. Opsi yang ditawarkan: **A** (rekomendasi) 30 soal uji + jawaban ideal + hal terlarang; **B** draf Sesi 3 (peta eskalasi, glosarium, contoh jadi); **C** peta data Kintone yang boleh dibaca/ditulis agent.

**How to apply:** Kalau user menyebut しえん-ちゃん / agent Slack 支援 → lanjutkan dari status ini, tanyakan opsi mana yang mau dikerjakan.
