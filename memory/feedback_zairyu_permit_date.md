---
name: feedback-zairyu-permit-date
description: Rule for filling 許可年月日 when not visible on newer ISA-design 在留カード
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f0e9cd6e-91ba-40e9-b7b1-4e3d0c06fbd3
---

新しいISAデザインの在留カードは許可年月日が読み取れない場合がある。

**Rule:** ユーザーから具体的な日付の指定がない場合：
- 年：タスクを実行した年（例：2026）
- 月日：在留期間満了日と同じ月日

**例：** 在留期間満了日 = 2029-06-15 → 許可年月日 = 2026-06-15

**Why:** 新しいISAカードのデザイン変更により、許可年月日フィールドが従来と異なる位置にあり読み取れない。ユーザーがこのルールを明示した。

**How to apply:** App 50の`residenceCardPermitDate`フィールドを更新する際に適用。
