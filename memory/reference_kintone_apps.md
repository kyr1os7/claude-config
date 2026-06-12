---
name: kintone-apps-reference
description: Kintoneアプリ一覧と用途 — よく使うApp IDのまとめ
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9a12f717-0fbe-44c0-a42e-93235a7a8f2f
---

| App ID | 名前 | 用途 |
|--------|------|------|
| 13 | 就労_就労管理 | 人材マスタ、面談実施日（支援）更新 |
| 50 | 就労_ビザ管理 | 在留カード情報、書類チェックリスト |
| 98 | 就労_面談記録 | 日々面談・定期面談の記録登録 |
| 241 | 社内管理_支援工数管理 | 業務報告の工数登録 |
| 258 | 定期面談管理（IM） | 定期面談完了率トラッキング |

## 認証
- 方法: X-Cybozu-Authorization ヘッダー（base64エンコード）
- または MCP経由（kintone-mcp-server）
- API: Python urllib.request 推奨（MCP使用禁止の場合あり）

**How to apply:** 各automationでApp IDを参照する際に使用。
