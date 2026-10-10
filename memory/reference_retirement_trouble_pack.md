---
name: reference-retirement-trouble-pack
description: 退職相談・トラブル対応 Agent Pack location + how cases are stored (anonymized learning vs full PII archive).
metadata: 
  node_type: memory
  type: reference
  originSessionId: b8794b69-d072-483e-89cd-d4f9bc35ffae
---

Agent Pack untuk menangani kasus 退職相談 / workplace trouble (analisis fakta → retention check → laporan 営業 Jepang). Lokasi: **`~/Claude/retirement-trouble-agent/`** (AGENTS.md, START_PROMPT, CASE_INTAKE, sessions, memory, .agents/skills+evals). Diterima dari rekan dalam bentuk ZIP di ~/Downloads.

Mode: analisis & draft saja; tidak menulis ke sistem eksternal tanpa approval + preview.

**Aturan penyimpanan kasus (penting):**
- Pola pembelajaran → simpan **anonim** (tanpa PII) di Portable Examples pack (`memory/retirement_trouble_operational_memory.md`), karena pack bisa di-share ulang.
- Arsip kasus nyata (PII) → simpan di folder terpisah **`~/Claude/retirement-trouble-cases/`**, BUKAN di dalam pack.

Kasus aktif: [[project-anisa-taishoku-case]].
