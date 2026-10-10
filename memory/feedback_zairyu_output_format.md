---
name: feedback-zairyu-output-format
description: 在留カード処理後の出力フォーマット — 変更内容をテーブルで表示
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f0e9cd6e-91ba-40e9-b7b1-4e3d0c06fbd3
---

在留カード処理完了後、変更内容を必ずテーブル形式で表示する。

**Rule:** 各Appの更新内容を「フィールド / 変更前 / 変更後」の形でまとめる。

**Why:** ユーザーが何が変わったかを一目で確認できるようにするため。

**How to apply:** 在留カード処理（zairyucard workflow）の完了報告時に適用。全App（50・30・13）を必ず記載し、変更がないAppは「変更なし」と明記する。
