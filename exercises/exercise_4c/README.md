# Exercise 4C — Decision Tool (Your Choice)
**Time:** 20 minutes

Choose **Option A** or **Option B**. Pick whichever is closer to your real job.

---

## Option A — Loan Eligibility Checker
**Dataset:** `data/loan_applicants.csv`

Apply these lending rules to each applicant and output APPROVED / REFERRED / DECLINED:

| Rule | Threshold | Fail result |
|------|-----------|-------------|
| Income sufficiency | `annual_income / 12 >= 3 * monthly_repayment` | DECLINED |
| Credit score | `credit_score >= 650` | REFERRED |
| Loan-to-Value | `loan_amount / property_value <= 0.80` | DECLINED |

- If ALL rules pass → APPROVED
- If credit score fails but income and LTV pass → REFERRED
- If income or LTV fails → DECLINED

**Output**: `loan_decisions.csv` with columns `applicant_id`, `name`, `decision`, `reason`

**Extension**: make thresholds configurable at the top of the script as variables.
Add a summary: how many APPROVED / REFERRED / DECLINED?

---

## Option B — Transaction Alert Generator
**Dataset:** `data/transactions_clean.csv`

Flag transactions matching ANY of these alert rules:

| Alert type | Rule |
|------------|------|
| `HIGH_VALUE` | `amount > 10000` |
| `CASH_LIMIT` | `category == 'CASH_WITHDRAWAL'` and `amount > 5000` |
| `DUPLICATE_SUSPECT` | Same `customer_id`, same `amount`, same `date` |

**Output**: `flagged_transactions.csv` with columns:
`date`, `customer_id`, `amount`, `category`, `branch`, `alert_type`, `recommended_action`

**Extension**: add a summary count by `alert_type`. Sort output by `amount` descending.

---

## Starter scripts
- Option A: `option_a_starter.py`
- Option B: `option_b_starter.py`
