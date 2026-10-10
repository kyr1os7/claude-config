---
name: feedback-up-github-flow
description: "Trigger \"up github\" — back up session artifacts to GitHub (anonim→public, PII→private)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b8794b69-d072-483e-89cd-d4f9bc35ffae
---

Saat user mengetik **"up github"** (biasanya setelah selesai konsultasi/kasus), jalankan flow backup ke GitHub yang sama seperti yang sudah disepakati.

**Why:** User mau cadangan tiap selesai konsultasi, dengan pemisahan data yang ketat (PII tidak boleh ke public).

**How to apply:**
1. Identifikasi artefak sesi → pisahkan **anonim** (pack/template/metodologi/contoh anonim) vs **PII** (arsip kasus nyata: nama, perusahaan, kondisi mental/visa).
2. Scan materi anonim untuk **PII dan token (`ghp_`)** SEBELUM push ke public. Kalau ada temuan → stop, jangan push public.
3. Push **anonim → public** repo `kyr1os7/claude-config` (mis. folder `retirement-trouble-agent/`).
4. Push **PII → private** repo `kyr1os7/claude-config-private` (mis. `retirement-trouble-cases/<nama>.md`). PII TIDAK PERNAH ke public.
5. Mekanik: pakai token dari [[reference-github-token]]; clone ke /tmp, set user.email kyr1os.10bit@gmail.com, commit dengan footer `Co-Authored-By: Claude Opus 4.8`, push ke HEAD:main.
6. Verifikasi: public TIDAK punya folder PII (cek API → Not Found), private punya arsipnya.
7. **Cleanup**: hapus clone /tmp (berisi token di .git/config).
8. Update arsip kasus + memori bila ada perubahan status.

**Catatan:** `.gitignore` repo meng-ignore `sessions/` → kalau ada file SOP/kasus di folder `sessions/`, force-add (`git add -f`). Konfirmasi pembagian dulu kalau kasus baru belum jelas anonim/PII-nya.
