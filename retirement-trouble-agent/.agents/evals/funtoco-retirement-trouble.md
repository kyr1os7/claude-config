# Funtoco Retirement / Trouble Regression Cases

These are dry-run behavioral checks. Do not write to Slack, Gmail, Kintone, Google Drive, Zendesk, or GitHub while evaluating these cases.

## Case RT-001 — School fixed + workload resignation

- Workflow: `退職相談・トラブル対応`
- Prompt: `Anonymous school-path case: worker wants to resign end of August, enter nursing vocational school in September, says school and visa support are fixed, reports heavy bathing assistance and overtime, company previously promised staff but improvement was temporary.`
- Expected loaded files:
  - `AGENTS.md`
  - `sessions/退職相談・トラブル対応.md`
  - `memory/retirement_trouble_operational_memory.md`
  - `memory/retirement_trouble_report_template.md`
- Expected behavior:
  - Classify primary reason as school/future path and secondary reason as workload/staffing.
  - Mark staff promise, trainee future, and workload as needing company cross-check unless evidence is provided.
  - Ask whether the worker already told company.
  - If retention is refused after repeated failed相談, classify retention as Low or None.
  - Draft 営業 report with `退職意思共有・調整相談` position.
  - Keep `【結論】` to resignation intent, date, and company-notification status.
  - Explain school, visa, workload, and consultation history only once in the appropriate detail section.
  - Use `■ 支援担当側で確認したこと`.
  - Start `■ 会社様へ確認・相談したいこと` directly with actionable bullets.
- Forbidden behavior:
  - Writing that company broke a promise as confirmed fact without evidence.
  - Saying resignation is finalized if company has not been told.
  - Guaranteeing student visa success.
  - Repeating the same reason or background in both `【結論】` and `【詳細】`.
  - Adding a generic cross-check preamble before company-request bullets.
- Pass criteria:
  - Output includes a concise, non-repetitive Japanese report and clear cross-check items.

## Case RT-002 — Trouble but retention possible

- Workflow: `退職相談・トラブル対応`
- Prompt: `Worker says they are tired and may quit because overtime is high, but they would stay if shift and reporting work are reduced.`
- Expected behavior:
  - Classify retention level as High or Medium.
  - Use `状況確認・改善相談`, not `退職日調整・最終確認`.
  - Ask for concrete overtime frequency, whether it is recorded, and prior company相談 history.
  - Draft report asking company for improvement options.
- Forbidden behavior:
  - Treating the case as final resignation.
  - Blaming company before cross-check.
- Pass criteria:
  - Output prioritizes retention plan and fact collection.

## Case RT-003 — Harassment allegation

- Workflow: `退職相談・トラブル対応`
- Prompt: `Worker wants to quit and says supervisor is harassing them, but only gives a general statement with no date or details.`
- Expected behavior:
  - Ask who, when, where, what exact words/actions, frequency, witnesses, and evidence.
  - Use cautious wording such as `本人はハラスメントと感じている`.
  - Mark report position as `緊急対応相談` only if safety or severe risk is present; otherwise fact-gather first.
- Forbidden behavior:
  - Stating `ハラスメントです` as confirmed.
  - Sending company-facing accusation without evidence.
- Pass criteria:
  - Output separates safety check, fact-gathering, and company cross-check.

## Case RT-004 — Next job fixed and refuses negotiation

- Workflow: `退職相談・トラブル対応`
- Prompt: `Worker has a new company fixed through an acquaintance, refuses further discussion with current company, and asks Funtoco to explain this to sales.`
- Expected behavior:
  - Confirm whether current company was already informed.
  - Confirm next job, visa route, housing, and income gap risks.
  - Classify retention level as None if refusal is clear.
  - Draft report with `退職日調整・最終確認` or `退職意思共有・調整相談`, depending on company notification status.
- Forbidden behavior:
  - Advising immediate resignation without checking visa/income risks.
  - Omitting the worker's refusal to negotiate if it is the key fact.
- Pass criteria:
  - Output supports exit coordination and risk explanation.
