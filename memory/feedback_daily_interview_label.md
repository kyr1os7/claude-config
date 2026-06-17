---
name: Daily interview label difference between Kintone and email
description: 日々面談イベントの扱い — Kintone App 241=ビデオ面談、メール=日々面談：名前 / 会社名。オンライン面談値は書込不可
type: feedback
originSessionId: e984976c-7770-49bb-912a-d2dccdc801ff
---
カレンダーの【日々面談】イベントの扱い（2026-06-17 ユーザー更新）:

- **メールドラフト**: 何があっても必ず `日々面談：(名前) / (会社名)` 形式で表記する（name / company）。
- **Kintone App 241** 作業内容: `ビデオ面談` を入れる。
  - ⚠️ ドロップダウンAPI上の表示ラベルは `オンライン面談` だが、これは「言語ごとの名称」の表示ラベルにすぎず、書き込むと `項目名が見つかりません`（CB_VA01）で**拒否される**。
  - **内部の本当の値 = `ビデオ面談`**（既存レコード多数で確認済み）。書込・検索は必ず `ビデオ面談` を使う。
  - 備考 = 会社名（既存パターン：例「柏原マルタマフーズ株式会社、医療法人社団恵宣会」）。
- **特例：カレンダーイベントが `【Zendesk対応】日々面談` の場合** → Kintone App 241 = `Zendesk対応`、ただしメールは通常どおり `日々面談：(名前) / (会社名)` と表記する。

**Why:** ユーザーが明示的に指定。Kintoneは作業実態（ビデオ面談 or Zendesk対応）、メールはKPI区分（日々面談）で表記を使い分ける。
**How to apply:** 「laporan harian」実行時に適用。[[daily-interview-kpi-data-source]] のKPI件数とは別物（こちらは表記ルール）。
