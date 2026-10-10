---
name: feedback-zairyu-permit-check-period
description: App 50 juga wajib isi field 在留期間（支援のみ）dan centang 許可日チェック — dua field yang sebelumnya terlewat
metadata:
  node_type: memory
  type: feedback
  originSessionId: f0e9cd6e-91ba-40e9-b7b1-4e3d0c06fbd3
  modified: 2026-09-01T06:40:57.633Z
---

Selain 3 field App 50 yang biasa diisi (residenceCardNo, residenceCardPermitDate, residenceCardExpirationDate), ada 2 field lagi yang harus diisi setiap kali:

1. **`在留期間`** (label: 在留期間（支援のみ）) — DROP_DOWN, bukan tanggal. Nilai durasi seperti kartu (`1年`, `3年`, `1年2月`, dst — lihat opsi field). Ambil dari:
   - Screenshot aplikasi 在留カード読取 (field "在留期間" eksplisit, contoh: "3年"), atau
   - Hitung dari 許可年月日 → 在留期限 di kartu.
2. **`許可日ダブルチェック_一時的_`** (label: 許可日チェック) — CHECK_BOX, opsi `確認済み`. Centang (isi `{'value': ['確認済み']}`) setiap kali App 50 sudah diupdate & diverifikasi.

**Why:** User menegur karena field 在留期間（支援のみ）dibiarkan kosong di semua record termasuk yang lama (bukan cuma kelalaian sesi ini). Sejak ditegur, wajib isi kedua field ini setiap task 在留カード update, mulai dari kasus berikutnya (tidak perlu backfill record lama kecuali diminta).

**How to apply:** Di Step 2 (Update App 50), setelah isi residenceCardNo/PermitDate/ExpirationDate, isi juga `在留期間` dan centang `許可日ダブルチェック_一時的_`.
