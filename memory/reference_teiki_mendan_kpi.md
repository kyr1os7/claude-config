---
name: Regular interview KPI data source
description: 定期面談進捗率はKintone App 258のstructured filtersで取得 — supportStaff=sandy@funtoco.jp, targetQuarter=当四半期, supportInterviewDone=完了の割合
type: reference
originSessionId: e984976c-7770-49bb-912a-d2dccdc801ff
modified: 2026-08-07T08:56:57.906Z
---

業務報告メールの「定期面談進捗」KPI実績は Kintone App 258（定期面談管理 IM）から取得する。

## ✅ 正しい取得方法：完了数もフィルタで直接取得（手動カウント禁止）

**完了数（分子）** — supportInterviewDone=完了 をフィルタに入れて totalCount を読むだけ：
```
app: "258"
fields: ["supportInterviewDone"]
filters:
  inValues:
    - field: "supportStaff", values: ["sandy@funtoco.jp"]
    - field: "targetQuarter", values: ["2026年Q3"]  ← 当四半期に変更
    - field: "supportInterviewDone", values: ["完了"]
limit: 500
```
→ 返ってきた `totalCount` = 完了数（分子）。

**総数（分母）** — 上記から `supportInterviewDone` フィルタを外して totalCount を読む（= 106 等）。

進捗率 = 完了数 / 総数（小数点第1位まで）。

🚫 **絶対にやらないこと：全レコードを取得して "完了" を目視で数える。** 106件のような密なデータでは必ず数え間違える（2026-08-07 に 63 と誤カウント→実際は 50、ユーザー指摘で発覚）。必ず上記フィルタ方式で totalCount を使う。

## ⚠️ 禁止：raw query string
`query` パラメータは Kintone MCP では完全に無視される。絶対に使わないこと。

## フィールド情報
- `supportStaff`: USER_SELECT — value[0].code = "sandy@funtoco.jp"
- `targetQuarter`: DROP_DOWN — 例: "2026年Q2"
- `supportInterviewDone`: CHECK_BOX — 完了 = ["完了"], 未完了 = []

四半期の判定: Q1=1-3月, Q2=4-6月, Q3=7-9月, Q4=10-12月

目標（月次で上がる。ユーザーがKPI入力で毎回指定）: 7月末=35%, 8月末=70%, 9月末=100% など。分母は四半期全体。

実績参考（フィルタ方式で確認済み）:
- 2026年Q2（6月10日時点）：55/56 = 98.2%
- 2026年Q3（8月7日時点）：50/106 = 47.2%
