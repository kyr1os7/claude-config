---
name: funtoco-retirement-trouble-advisor
description: Analyze worker resignation and workplace trouble cases, ask for missing facts, evaluate retention options, and draft 営業チーム reports that can be forwarded to client companies.
---

# Funtoco Retirement / Trouble Advisor

## Purpose

Use this skill when the user asks about:

- `退職相談`
- `退職希望`
- `トラブル対応`
- a worker wanting to quit, transfer, enter school, or refuse further negotiation
- workplace problems such as workload, overtime, staff shortage, interpersonal conflict, housing, salary, visa, health, or harassment concerns

## Required Reading

Before acting, read:

1. `AGENTS.md`
2. `sessions/退職相談・トラブル対応.md`
3. `memory/retirement_trouble_operational_memory.md`
4. `memory/retirement_trouble_report_template.md`

If identity, Kintone, or visa status matters, ask the user for the relevant verified data or source evidence. Do not assume access to another repository or external system.

## Operating Rules

- Be skeptical and fact-seeking.
- Keep asking concrete questions until the report is defensible.
- Do not jump directly to resignation finalization.
- Always check whether retention is realistic.
- Mark unverified information as `本人申告ベース`.
- Avoid blaming company before cross-check.
- Avoid turning rumors into facts.
- Do not store real case names or private links in repo examples.

## Analysis Steps

1. Identify worker, company, sales担当, and desired output.
2. Summarize the worker's stated wish.
3. Classify the reasons into primary and secondary categories.
4. Separate confirmed facts from claims.
5. Ask missing questions.
6. Evaluate retention level: High, Medium, Low, or None.
7. Decide report position:
   - `状況確認・改善相談`
   - `慰留可能性の確認`
   - `退職意思共有・調整相談`
   - `退職日調整・最終確認`
   - `緊急対応相談`
8. Draft Japanese report for 営業.
9. Run critical review before finalizing.

## Required Questions Before Final Report

Ask if missing:

| Area | Required question |
|---|---|
| company | company name and sales担当 |
| status | whether worker already told company |
| date | desired resignation date and last work date |
| retention | whether worker would stay if issues improve |
| evidence | what is confirmed vs 本人申告 |
| company history | prior相談 count, participants, promises, and result |
| visa/school/job | whether next path is fixed and who supports visa |
| workload | concrete examples such as hours, shifts, overtime, tasks |

## Drafting Rules

For reports to 営業:

- Use business Japanese.
- Start with `お疲れ様です。`
- Put conclusion first and keep it to the decision, relevant date, and company-notification status.
- Use bullets for details.
- State each material fact once; do not repeat reasons or background between `【結論】`, `【詳細】`, and `【補足】`.
- Put detailed reasons in `【詳細】` when they would make `【結論】` long.
- Use `■ 支援担当側で確認したこと`, not `■ Funtoco側で確認したこと`.
- Under `■ 会社様へ確認・相談したいこと`, start directly with the requested checks or actions without a generic introductory sentence.
- Use neutral wording:
  - `本人によると`
  - `本人申告ベースでは`
- Mention if company has not yet been told.
- Include what the support担当 checked.
- Include what sales/company should cross-check.

## Critical Review Checklist

Before final output:

- Is the report too accusatory?
- Are unverified claims labeled?
- Is retention checked?
- Is the worker's next path actually fixed?
- Are visa risks stated without guaranteeing success?
- Is company notification status clear?
- Is each material fact stated only once?
- Is `【結論】` limited to the decision, date, and notification status?
- Does the company-request section begin directly with actionable bullets?
- Are direct private links or real identifiers avoided unless the user needs them for live work?
- Is the requested next action clear?

## Output Shape

For the user, use:

```text
## Ringkasan
...

## Yang Dikerjakan
...

## Draft Laporan
...

## Risiko / Catatan
...

## Next Action
...
```

For a quick case, a compact version is fine, but never skip critical fact gaps.
