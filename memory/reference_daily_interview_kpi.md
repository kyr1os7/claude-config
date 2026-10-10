---
name: daily-interview-kpi-data-source
description: 日々面談の実績数はKintone App 98のstructured filtersで取得する — raw queryは使用禁止
metadata: 
  node_type: memory
  type: reference
  originSessionId: e984976c-7770-49bb-912a-d2dccdc801ff
  modified: 2026-08-28T09:04:08.520Z
---

業務報告メールの「日々面談」KPI実績は Kintone App 98（面談記録）から取得する。

## ✅ 正しい取得方法：structured filters（inValues + dateRange）

```
app: "98"
fields: ["timeInterview", "Created_by", "作成日"]
filters:
  inValues:
    - field: "timeInterview", values: ["日々の面談"]
    - field: "Created_by", values: ["sandy@funtoco.jp"]
  dateRange:
    - field: "作成日", from: "YYYY-MM-01", to: "YYYY-MM-30"
limit: 500
```

`totalCount` の値がそのまま日々面談件数。

## 🚫 落とし穴：filter直後の totalCount が古い値のまま返ることがある
2026-08-25〜28 の4日間、この日々の面談フィルタの `totalCount` が **86 に張り付いたまま**（実際は record が毎日増えていた）。8/28にユーザー指摘で発覚し、全record を生取得して数え直したら **実際は 104**（127件中 定期面談23を引いた数）だった。
**対策：日々面談KPIは filter の totalCount を鵜呑みにしない。**
- ①フィルタ無し（Created_by + dateRange のみ）で全件取得 → 返ってきた records を実際に数え、`定期面談` を引く、または
- ② `日々の面談` フィルタと `定期面談` フィルタを両方かけて件数を出し、合計が全件と一致するか検算する。
1つのクエリの totalCount だけで報告しないこと。

## ⚠️ 禁止：raw query string
`query` パラメータは Kintone MCP では完全に無視される。絶対に使わないこと。

## フィールド情報
- `timeInterview`: DROP_DOWN — "日々の面談" または "定期面談"
- `Created_by`: CREATOR — sandy@funtoco.jp
- `作成日`: CREATED_TIME — 記録作成日（interviewDate ではない）

目標: 40件/月

実績参考:
- 2026年6月10日時点：47件
