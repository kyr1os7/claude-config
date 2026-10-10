---
name: Exclude routine events from report
description: 確認リマインド・タスク確認はKintone工数・メールドラフト両方から除外する。Lunch・移動・ごみ当番と同じルーティン扱い。
type: feedback
originSessionId: e984976c-7770-49bb-912a-d2dccdc801ff
---
以下のカレンダーイベントはKintone工数登録・メールドラフト両方から除外する:
- 【Lunch】
- 【移動】
- 【ごみ当番】
- 【タスク確認】
- 【確認リマインド】

**Why:** ユーザーが明示的に指定。ルーティン業務のため報告不要。
**How to apply:** 「laporan harian」実行時、上記イベントはフィルターで除外し、Kintone工数にもメールドラフトにも含めない。
