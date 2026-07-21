# Beginner Cards — Exercise 4C Option A: Loan Eligibility Checker
**Start with Card 0 (Plan the Plan) before using any card below.**

---

## Card 4C-A-B — Loan eligibility (guided)

Paste into Copilot Chat:
```
"I have a pandas DataFrame called df_loans with columns:
applicant_id, name, annual_income, credit_score,
loan_amount, property_value, monthly_repayment.

Apply these three rules to each row:
1. Income rule: annual_income / 12 >= 3 * monthly_repayment
2. Credit rule: credit_score >= 650
3. LTV rule:    loan_amount / property_value <= 0.80

Decision logic:
  If ALL rules pass → APPROVED
  If only credit fails → REFERRED
  If income or LTV fails → DECLINED

Add a decision column and a reason column.
Save to loan_decisions.csv."
```

**Before you run:**
- Run `df_loans['decision'].value_counts()` — check APPROVED / REFERRED / DECLINED appear
- Test on the first 5 rows before running on all 50: `df_loans.head(5)`
- Make sure you loaded `df_loans = pd.read_csv('data/loan_applicants.csv')` first

---

## Extension — Configurable thresholds

Paste into Copilot Chat:
```
"Refactor the code so the credit score threshold (650),
LTV threshold (0.80), and income multiplier (3) are
defined as variables at the top of the script instead
of hardcoded inside the function."
```

---

## Extension — Summary counts

Paste into Copilot Chat:
```
"Write Python code to print how many applicants fall
into each decision category using value_counts()."
```
