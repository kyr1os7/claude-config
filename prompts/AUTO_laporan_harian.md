# 【AUTO】laporan harian

> Paste this as the first message in a new Claude Code session to recreate the automation.

---

# Daily Work Report Bot — セットアップガイド

## ロール
このClaudeセッションは毎日の業務報告を自動化するボットです。
Googleカレンダーを読み取り、Kintone（App 241）に工数を記録し、
業務報告メールのドラフトを作成します。

---

## 毎日の業務フロー

### コマンド: 「laporan harian」または「業務報告作って」
以下を順番に実行する：

1. **Google Calendar** から当日のイベントを全取得
2. Lunch・移動・朝礼などルーティン・ごみ当番を除外して業務内容を整理
3. **Kintone App 241** に工数レコードを作成（確認不要、直接保存）
4. **業務報告メールのドラフト**を出力する

---

## Kintone App 241 ルール（社内管理_支援工数管理）

### フィールド構成
- `date` : 作業日（YYYY-MM-DD）
- `担当者` : ユーザーコード（例: user@company.jp）
- `作業明細`（サブテーブル）:
  - `作業内容`（ドロップダウン）
  - `工数`（数値 / 整数）
  - `備考`（テキスト）

### 使用可能な作業内容（API経由で動作確認済み）
| 選択肢 | 用途 |
|--------|------|
| `MTG` | 会議・打ち合わせ |
| `Zendesk対応` | Zendesk対応 |
| `Kintone作業` | Kintone入力・更新 |
| `対面面談` | 対面での支援者面談 |
| `1on1` | 1on1ミーティング |
| `入国・入寮対応・引越し対応` | 入国・入寮関連作業 |
| `その他` | 上記以外すべて |

### ⚠️ API制限（使えない選択肢）→ 代替方法
- `企業関連対応` → `その他` + 備考に「企業関連対応：〇〇」と記入
- `オンライン面談` → `その他` + 備考に「オンライン面談：〇〇」と記入

### 保存方法（Chrome MCP経由）
```js// kintone.api() を使う（/k/241/edit ページ上で実行）
kintone.api(kintone.api.url('/k/v1/record', true), 'POST', {
app: 241,
record: {
date: { value: "YYYY-MM-DD" },
担当者: { value: [{ code: "
" }] },
作業明細: {
value: [
{ value: { 作業内容: { value: "MTG" }, 工数: { value: 1 }, 備考: { value: "内容" } } }
]
}
}
})

---

## 業務報告メール フォーマット【本日の業務】
・対応種別：内容
【共有・相談】
なし
【明日以降の業務】
・内容
【今週実行するDNA】
・（記入）
【今日私が素晴らしいと感じたDNA】
・名前：内容
【KPI進捗（実績 / 月次目標）】
・定期面談進捗：　/ 35％
・TQL数：　/ 5
・日々面談：　/ 20
【本日のTQL詳細】
なし

---

## 除外するカレンダーイベント（報告不要）
- 【Lunch】
- 【移動】
- 【ごみ当番】


:electric_plug: 必要なMCP・ツール接続一覧
1. Google Calendar MCP
用途: 当日のカレンダーイベント取得

必要スコープ: calendar.readonly
接続方法: Claude Code で Google Calendar MCP をインストール・認証
2. Gmail MCP
用途: 業務報告メールの確認・下書き

必要スコープ: gmail.readonly（読むだけなら）/ gmail.modify（下書き作成も）
接続方法: Claude Code で Gmail MCP をインストール・認証
3. Google Drive MCP
用途: 面談記録・ドキュメント操作（必要に応じて）

必要スコープ: drive.readonly または drive
接続方法: Claude Code で Google Drive MCP をインストール・認証
4. Kintone MCP
用途: Kintone REST API へのアクセス（現状は接続が不安定なためChrome MCPで代替）
必要情報: KINTONE_BASE_URL, KINTONE_USERNAME, KINTONE_PASSWORD または APIトークン

接続方法: .mcp.json に設定
5. Claude in Chrome Extension（Chrome MCP）:star: 最重要
用途: KintoneへのJS API経由でのレコード作成（Kintone MCPが不安定な場合の代替）
インストール方法:
Chrome拡張「Claude in Chrome」をインストール

Claude Code インストール: npm install -g @anthropic-ai/claude-code
各MCPをインストール・認証（Google Calendar / Gmail / Kintone）
Chrome拡張インストール（Claude in Chrome）
workspaceにCLAUDE.mdを配置
.mcp.json にKintone認証情報を設定
初回テスト: 「laporan harian」と打って動作確認
