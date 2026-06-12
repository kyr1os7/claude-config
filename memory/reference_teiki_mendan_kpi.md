---
name: Regular interview KPI data source
description: 定期面談進捗率はKintone App 258のstructured filtersで取得 — supportStaff=sandy@funtoco.jp, targetQuarter=当四半期, supportInterviewDone=完了の割合
type: reference
originSessionId: e984976c-7770-49bb-912a-d2dccdc801ff
---

業務報告メールの「定期面談進捗」KPI実績は Kintone App 258（定期面談管理 IM）から取得する。

## ✅ 正しい取得方法：structured filters（inValues）

```
app: "258"
fields: ["supportStaff", "supportInterviewDone", "targetQuarter"]
filters:
  inValues:
    - field: "supportStaff", values: ["sandy@funtoco.jp"]
    - field: "targetQuarter", values: ["2026年Q2"]  ← 当四半期に変更
limit: 500
```

完了数 = `supportInterviewDone.value` に「完了」が含まれるレコード数
進捗率 = 完了数 / totalCount（小数点第1位まで。例: 98.2%）

## ⚠️ 禁止：raw query string
`query` パラメータは Kintone MCP では完全に無視される。絶対に使わないこと。

## フィールド情報
- `supportStaff`: USER_SELECT — value[0].code = "sandy@funtoco.jp"
- `targetQuarter`: DROP_DOWN — 例: "2026年Q2"
- `supportInterviewDone`: CHECK_BOX — 完了 = ["完了"], 未完了 = []

四半期の判定: Q1=1-3月, Q2=4-6月, Q3=7-9月, Q4=10-12月

目標: 100%

実績参考:
- 2026年Q2（6月10日時点）：55/56 = 98.2%
