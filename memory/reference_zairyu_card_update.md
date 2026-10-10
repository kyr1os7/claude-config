---
name: zairyu-card-update-workflow
description: 在留カード更新ワークフロー — 写真からKintone App 50の3フィールドを更新し、Dropboxに保存してリンク返却
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9a12f717-0fbe-44c0-a42e-93235a7a8f2f
---

## ワークフロー

1. 写真から以下3フィールドを読み取る:
   - `在留カード番号（支援のみ）`
   - `在留カード記載_許可年月日（支援のみ）`
   - `在留期限（支援のみ）`
2. Kintone App 50（就労_ビザ管理）の該当レコードを更新
3. 写真をDropboxの正しいパスに移動・リネーム（[[Google Drive file naming convention (書類格納)]] に従う）
4. 入力した**全アプリのリンク**を返す（App 50だけでなく更新した全app）

## 注意
- Dropboxは絶対に削除・上書き禁止（[[Cloud storage no overwrite rule]]）
- タスク完了後は全アプリのKintoneリンクを提供 [[Kintone record link after task]]

**How to apply:** 在留カード写真が届いたらこのフローを実行。
