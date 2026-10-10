# 退職相談・トラブル対応 Agent Pack

Paket ini membantu 支援担当 menganalisis `退職希望` dan masalah kerja, mencari kemungkinan retention, serta membuat laporan bahasa Jepang untuk 営業チーム.

## Cara Pakai

1. Extract ZIP ini ke folder lokal.
2. Buka folder hasil extract sebagai workspace di Codex.
3. Mulai percakapan menggunakan isi `START_PROMPT.md`.
4. Masukkan fakta kasus memakai format `CASE_INTAKE.md`.
5. Jawab pertanyaan lanjutan sampai data cukup untuk membuat laporan.

Tidak diperlukan memory atau repository milik pembuat paket.

## Isi Paket

| File | Fungsi |
|---|---|
| `AGENTS.md` | Aturan utama dan safety |
| `START_PROMPT.md` | Prompt awal siap pakai |
| `CASE_INTAKE.md` | Form pengumpulan data kasus |
| `sessions/退職相談・トラブル対応.md` | SOP penanganan kasus |
| `memory/retirement_trouble_operational_memory.md` | Pertanyaan, fact labels, retention level |
| `memory/retirement_trouble_report_template.md` | Template laporan 営業 |
| `.agents/skills/funtoco-retirement-trouble-advisor/SKILL.md` | Perilaku agent yang reusable |
| `.agents/evals/funtoco-retirement-trouble.md` | Contoh uji perilaku anonim |

## Batasan

- Agent membantu analisis dan drafting, bukan memberikan keputusan hukum atau menjamin hasil visa.
- Informasi dari pekerja harus dibedakan dari fakta yang sudah dikonfirmasi.
- Data pribadi kasus nyata jangan dimasukkan ke template atau contoh reusable.
