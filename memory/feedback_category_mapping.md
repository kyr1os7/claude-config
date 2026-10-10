---
name: category-mapping-zendesk-vs-sonota
description: カテゴリ分類ルール — 支援者向け案内/フォロー=Zendesk対応、社内事務/記録作成=その他（email・App241両方）
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e984976c-7770-49bb-912a-d2dccdc801ff
---

業務報告のカテゴリ分類（メール【本日の業務】と Kintone App 241 の作業内容、両方に適用・一致させる）。2026-06-22 ユーザー修正。

## 支援者（外国人労働者）向けの案内・フォローアップ・手続き対応 → `Zendesk対応`
Zendesk経由で対応するため。カレンダーのタイトルが【作業】や【更新申請】でも、内容が支援者向け案内ならZendesk対応にする。
例：
- 資格変更案内
- 更新申請案内
- FunEduフォローアップ
- ライフライン案内、自転車保険案内 等の各種手続き案内

## 社内事務・記録作成 → `その他`
例：
- 来客アポ設定・メール案内（社内/来客向け、支援者向けではない）
- 面談記録作成・退職面談記録作成（※`Kintone作業`ではない → `その他`）

## 判別ポイント
- 受け手が**支援者（外国人労働者）**で案内/フォロー/手続き対応 → `Zendesk対応`
- **社内事務**（来客対応、アポ調整）や**記録の作成** → `その他`
- 「案内」という語だけで判断しない（来客メール案内は その他）。受け手と性質で判断。

関連: [[feedback-email-format]] / [[daily-interview-label-difference-between-kintone-and-email]]
