---
name: no-send-confirm
description: Gmailドラフト作成後に「送信しますか？」と確認しない — ユーザーが自分で手動送信する
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e984976c-7770-49bb-912a-d2dccdc801ff
---

業務報告などでGmailドラフトを作成した後、「送信しますか？」「AWAITING APPROVAL」といった送信確認を**しない**。ドラフトを作成したらそのままタスク完了とする。

**Why:** ユーザーは作成されたドラフトを必ず自分でGmail上から手動確認・送信するため、確認は不要。

**How to apply:** ドラフト作成完了を報告し、ドラフトIDと[[feedback_kintone_link]]のKintoneリンクを提示して終了。送信アクション自体は引き続き行わない（ユーザーが手動送信）。
