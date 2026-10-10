---
name: mendan-yoyaku-workflow
description: 面談予約日程ワークフロー — Gmail(funtoco@gmail.com)で予約完了メールを検索しKintone App 13の面談実施日を更新する
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9a12f717-0fbe-44c0-a42e-93235a7a8f2f
---

## ワークフロー（コマンド: 「CEK」）

1. Gmail (funtoco@gmail.com) を検索
   - 対象: 過去24時間以内の未処理メール
   - タイトル: `予約が完了しました: 【定期面談】(名前)`
2. メールから面談予定日を取得
3. Kintone App 13（就労_就労管理）の該当レコードを更新
   - 更新フィールド: `面談実施日（支援）`
4. 更新した全員の名前をリスト表示

## 注意
- 誤った名前を更新しないこと（turn 11: "daphne itu salah, lupakan"）
- バックグラウンドで実行

**How to apply:** 「CEK」コマンド受信時にこのフローを実行。
