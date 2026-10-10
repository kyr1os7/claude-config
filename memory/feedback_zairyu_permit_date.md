---
name: feedback-zairyu-permit-date
description: Rule for filling 許可年月日 when not visible on newer ISA-design 在留カード
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f0e9cd6e-91ba-40e9-b7b1-4e3d0c06fbd3
  modified: 2026-07-23T03:02:48.704Z
---

新しいISAデザインの在留カードは許可年月日が読み取れない場合がある。

**Rule:** ユーザーから具体的な日付の指定がない場合：
- 年：タスクを実行した年（例：2026）
- 月日：在留期間満了日と同じ月日

**例：** 在留期間満了日 = 2029-06-15 → 許可年月日 = 2026-06-15

**Why:** 新しいISAカードのデザイン変更により、許可年月日フィールドが従来と異なる位置にあり読み取れない。ユーザーがこのルールを明示した。

**How to apply:** App 50の`residenceCardPermitDate`フィールドを更新する際に適用。

---

## 初回許可された日 の取得ルール（App 30）

**Rule:** 2回目以降の場合、`初回許可された日`はApp 30やApp 50のデータから推測しない。必ずGoogle Driveの1回目カード画像を開いて、カード記載の`許可年月日`を確認する。

**Why:** ユーザーから「2回目以降はカードの許可年月日ではなく、Drive内の1回目カードから初回日を確認するべき」と指摘を受けた。

**How to apply:** 申請書類が2回目以降の場合 → Drive > 4.OLD内の1.申請書類1回目 > 5.在留カード（または4.在留カード）フォルダ内の画像を読み込み、許可年月日を確認してからApp 30を更新する。
