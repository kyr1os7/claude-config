---
name: japan-timezone-awareness
description: Userは日本在住（JST）— 日付処理時は必ずJSTで判断する
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9a12f717-0fbe-44c0-a42e-93235a7a8f2f
---

Userは日本在住のため、すべての日付・時刻はJST（UTC+9）で処理する。

**Why:** ユーザーが明示的に指摘（「kyaknya kamu ada salah, saya tinggal di jepang. jd tolong perhatikan jam nya ya」）。UTCと日本時間の日付がずれていた。

**How to apply:** カレンダー取得・Kintone記録作成・メール検索など日付を扱う全操作で、JSTの「今日」を基準にする。深夜0時前後は特に注意。
