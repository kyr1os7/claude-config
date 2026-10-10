# 退職相談・トラブル対応 Operational Memory

Use this with `sessions/退職相談・トラブル対応.md`.

This workflow helps a support担当 analyze resignation and workplace trouble cases, then produce a company-facing Japanese report for 営業チーム.

## Default Mode

Default is analysis and draft only.

Do not write to Slack, Gmail, Kintone, Google Drive, Zendesk, or GitHub unless the user explicitly asks for that action and required safety gates are satisfied.

## Core Decision Frame

Every case should answer these questions:

| Question | Why it matters |
|---|---|
| What exactly does the worker want? | 退職, transfer, school, reduced workload, mediation, or just advice |
| Is the resignation intent final? | Determines whether to focus on retention or exit control |
| What facts are confirmed? | Prevents overclaiming to the client |
| What is only 本人申告? | Keeps report neutral |
| Has the company had a chance to improve? | Important for fairness and defensibility |
| What retention path exists? | Funtoco should not jump directly to resignation |
| What risks exist if the worker stays? | Health, visa, legal, burnout, trust breakdown |
| What risks exist if the worker quits? | Income gap, visa status, housing, school/next job uncertainty |

## Fact Quality Labels

Use these labels internally and when useful in user-facing analysis:

- `confirmed`: supported by document, system data, direct message, or both sides.
- `本人申告`: said by the worker, not yet cross-checked.
- `company claim`: said by company, not yet cross-checked.
- `third-party`: from coworker, friend, school, new employer, or acquaintance.
- `unclear`: missing details.

Never upgrade `本人申告` or `third-party` information into confirmed fact without evidence.

## Question Bank

### Basic

| Area | Questions |
|---|---|
| identity | Nama, company, sales担当, App 13/App 30 link if available |
| status | 在籍中, probation, visa type, visa expiry, contract period |
| desired outcome | quit, transfer, school, home country, stay if improved |
| timeline | desired resignation date, last work date, school/job start date |

### Resignation Intent

Ask:

- Apakah 退職希望日 sudah konkret?
- Apakah pekerja sudah bicara ke atasan/perusahaan?
- Kalau perusahaan memberi improvement, apakah masih mau bertahan?
- Kalau tidak mau bertahan, kenapa improvement sudah tidak cukup?
- Apakah keputusan dipengaruhi pihak ketiga, sekolah, teman, atau calon perusahaan?

### Workload / Working Conditions

Ask:

- Beban kerja apa yang paling berat?
- Shift jam berapa sampai jam berapa?
- Overtime seberapa sering?
- Apakah overtime tercatat di 勤怠?
- Apakah tugas di luar job description?
- Apakah ada kekurangan staff objektif?
- Apakah pernah dilaporkan ke atasan?

### Company Improvement History

Ask:

- Sudah相談 berapa kali?
- Siapa yang hadir?
- Apa janji perusahaan secara spesifik?
- Apakah janji itu rencana atau komitmen?
- Apakah improvement terjadi?
- Berapa lama improvement bertahan?
- Apa yang kembali buruk?

### School / Next Job / Visa

Ask:

- Sekolah/next job sudah fix atau masih rencana?
- Ada 合格通知, 内定, 入学予定日, atau dokumen resmi?
- Siapa yang bantu visa?
- Jenis visa yang dituju?
- Apakah ada income gap?
- Apakah worker memahami risiko jika status change gagal/tertunda?

### Harassment / Conflict

Ask carefully:

- Siapa yang melakukan tindakan?
- Kapan, di mana, dan ada saksi?
- Apa kata/aksi spesifik?
- Apakah terjadi berulang?
- Apakah pekerja sudah melapor?
- Apakah ada bukti tertulis/audio/screenshot?
- Apakah pekerja merasa aman kembali bekerja?

Do not label something `ハラスメント` as fact unless evidence supports it. Use `ハラスメントに該当する可能性がある内容` or `本人はハラスメントと感じている` when not confirmed.

## Retention Levels

| Level | Meaning | Handling |
|---|---|---|
| High | worker may stay if specific issue fixed | propose concrete improvement request to company |
| Medium | worker disappointed but still willing to talk | ask company for cross-check and short-term trial plan |
| Low | repeated相談 failed or trust is broken | prepare exit-control report |
| None | worker refuses negotiation or has fixed school/next job | focus on 円満退職, dates, visa/housing/income risks |

## Report Positioning

Use one of these positions:

| Position | Use when |
|---|---|
| `状況確認・改善相談` | facts unclear or retention still possible |
| `慰留可能性の確認` | worker may stay if company can fix specific issues |
| `退職意思共有・調整相談` | worker wants to quit but has not told company |
| `退職日調整・最終確認` | worker intent is final and company already knows |
| `緊急対応相談` | safety, harassment, health, legal, or visa risk is high |

## Wording Rules

### Concision and Section Ownership

- Keep `【結論】` to the decision, relevant date, and company-notification status.
- Put reasons, background, and supporting facts in `【詳細】` only.
- State each material fact once. Do not repeat school, visa, workload, consultation history, or retention details across sections.
- Use `■ 支援担当側で確認したこと`, not `■ Funtoco側で確認したこと`.
- Under `■ 会社様へ確認・相談したいこと`, start directly with actionable bullets. Do not add a generic cross-check preamble.

Prefer:

- `本人によると`
- `本人申告ベースでは`
- `現時点では`
- `退職確定ではなく、まずは状況確認・改善可否を相談したいです`
- `本人の意思はかなり固い印象です`

Avoid unless confirmed:

- `会社が約束を守っていない`
- `ハラスメントです`
- `違法です`
- `退職確定です`
- `会社に問題があります`

## Critical Red Flags

Escalate caution when:

- worker has not told company yet
- report may reveal sensitive school/next-job details
- visa route is not confirmed
- unpaid overtime or labor-law issues are alleged
- harassment or discrimination is alleged
- worker says they cannot continue due to mental/physical condition
- company may retaliate or pressure worker

## Portable Examples

Use anonymized examples only.

### Example A: School Path + Workload

- Worker wants to resign end of August and enter a nursing vocational school in September.
- School acceptance and visa support are said to be fixed.
- Worker also reports heavy bathing assistance, reporting workload, and frequent overtime.
- Company had discussed adding staff before, but worker says improvement was temporary.
- Retention level: Low or None.
- Report position: `退職意思共有・調整相談`.

### Example B: Next Job + Refusal To Negotiate

- Worker has next employer via acquaintance.
- Worker refuses further company negotiation due to exhaustion.
- Retention level: None.
- Report position: `退職日調整・最終確認`.

### Example C: Company Trouble But Retention Possible

- Worker is frustrated by shift and communication issues.
- No next job/school fixed.
- Worker says they may stay if workload and communication improve.
- Retention level: Medium.
- Report position: `状況確認・改善相談`.

### Example D: Highly Indecisive New Hire + Two-Sided Trust Erosion

- 特定技能1号 介護, hired about three weeks ago, still in 試用期間.
- From day 4 the worker repeatedly asked to resign or change 分野 (toward ビルクリーニング), but reversed position roughly seven times in three weeks.
- Worker reasons (本人申告): 介護 does not suit their personality, Japanese-language difficulty, stress with a strict leader, regret over choosing 介護.
- Facility side (company claim): poor note-taking, little self-awareness of mistakes, passive, slow, low energy, does not ask when unsure, impolite speech.
- Constraints that lock the worker in: 特定技能 visa is employment-dependent; 分野変更 needs an exam with no fixed date; internal transfer to 保育園 is impossible; a company loan is being repaid monthly.
- Retention level: Low — not because the exit is final (it is volatile) but because two-sided trust is eroding and the worker resists introspection.
- Report position: `状況確認・改善相談` with decision-forcing.
- Decision lessons:
  - Do not treat volatile, fast-changing resignation talk as a final decision.
  - Even when dragging the case clearly harms the company, do not jump to 解雇: 特定技能 dismissal risks forced 帰国, may require 30-day notice or pay after the 14-day 試用期間, and an amicable 自己都合退職 is usually better for the worker.
  - Stop open-ended drift with a short trial window: concrete behavioral criteria, a clear deadline, and a pre-agreed decision rule that moves to an orderly 退職日 if no change.
  - Keep the report neutral: leader strictness is 本人申告; facility complaints are company claim; neither side is "at fault" without cross-check.
- Outcome (case closed): retention failed and the worker resigned. Nothing changed — the most basic agreed commitment (taking notes) was never done, and nothing taught was retained. The intent to move to a different 特定技能 field eventually reached the facility, the facility head became angry, and the worker's request to keep working about three months while job-hunting was what triggered it. Coworkers lost motivation from teaching without result.
- Outcome lessons:
  - A worker who cannot honor the smallest concrete commitment during a trial window will not be retained. Note-taking is a useful early signal.
  - An unresolved poor-fit case has a second victim: the teaching team. Count team morale as a real cost when deciding how long to let a case drift.
  - Confidentiality about a 転職 intent is fragile. Plan in advance for how it will be handled if the company learns of it, rather than assuming it stays hidden.
  - Asking to stay employed while searching for work in another field reads to the company as being used. Expect anger, and treat any extension as goodwill that must be requested, never as the worker's right.
  - Once goodwill is spent, a further change of heart cannot restore retention. Tell an indecisive worker plainly that the door may already be closed.
  - After the exit is decided, guardrails come before dates: the new field's skill exam and change-of-status application, the notification to immigration when the contract ends, and any outstanding loan repayment.
  - Repair the client relationship separately from the worker's case. Acknowledge the burden the staff carried; do not defend the worker's behavior.

### Example E: Growth-Motivated 転職 — No Conflict, Financial Trap Risk

- 特定技能1号 介護, about 1.5 years at the current employer, no complaint about the workplace.
- Worker opens the topic gratefully and hesitantly: wants a new environment, wants an entry-level caregiver training course sooner, and says the pay would be "better for my future".
- This archetype is the opposite of a distress case. There is no conflict to mediate, so the risk is not a broken relationship — it is a **badly calculated financial decision** and **ignorance of the procedure**.
- Retention level: Medium–High. The stated reason is usually **never tested** — ask first whether the worker has actually asked the current employer about the training.
- Report position: `状況確認・改善相談`.
- Decision lessons:
  - Ask what "growth" concretely means. A vague answer often hides a different real reason (fatigue, a friend recruiting them, interpersonal issues).
  - Never accept a salary figure at face value. Demand written 雇用条件書 and compare **take-home**, not gross: night-shift counts and allowances, qualification and improvement allowances, bonus, dormitory and utility deductions, commuting, and residence tax (which often jumps in the second year). Job ads that look generous frequently have small take-home after deductions.
  - Red flag: any deduction labeled as support/management fee. Under 特定技能 the support costs must be borne by the accepting organization, not charged to the worker.
  - 転職 under 特定技能 is not a simple notification — it needs a change-of-status application taking roughly 1–3 months, during which the worker may not start the new job. Quitting early means an income gap. The 5-year cumulative cap is not reset by changing employers.
  - Strongest retention lever is career-path support, framed in the worker's own language of growth: at 1.5 years they are halfway to the 3 years of practical experience needed for 介護福祉士, which opens a long-term residence status. Correct the target if needed — the qualification route needs the higher-level 実務者研修, not only the entry course.
  - Sequence the questions in batches. Light questions by chat; do the money arithmetic by phone. Open every conversation with "I am not stopping you" — a worker who feels blocked will arrange the move silently and walk into the trap.
