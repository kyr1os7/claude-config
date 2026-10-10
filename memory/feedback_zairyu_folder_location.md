---
name: feedback-zairyu-folder-location
description: 在留カードフォルダの作成場所 — 申請書類X回目の中に作る
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f0e9cd6e-91ba-40e9-b7b1-4e3d0c06fbd3
---

Google Driveの「4.在留カード」フォルダは、個人フォルダのルートではなく、**現在の申請書類フォルダ（例：1.申請書類2回目）の中**に作成する。

**Why:** ユーザーが誤った場所（ルート）に作成されたフォルダを手動で移動する必要があったため。

**How to apply:** create_fileで4.在留カードを作る際、parentIdは個人フォルダIDではなく、最新の「1.申請書類X回目」フォルダIDを使う。
