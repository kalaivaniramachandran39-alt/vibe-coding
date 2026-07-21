# Intermediate Card — Exercise 4C Option A: Loan Eligibility Checker
**Write your own 5-element prompt**

---

Start with Card 0 (Plan the Plan), then use the TASK / INPUT / LOGIC / OUTPUT / LIBRARIES framework:

```
TASK:      Build a loan eligibility checker
INPUT:     df_loans with columns: applicant_id, name,
           annual_income, credit_score, loan_amount,
           property_value, monthly_repayment
LOGIC:     Apply 3 rules (income, credit, LTV — see exercise brief)
           Produce APPROVED / REFERRED / DECLINED + reason
OUTPUT:    loan_decisions.csv with decision and reason columns
LIBRARIES: pandas
```

**Before you run:**
- Write your own prompt using the framework above
- Verify with `df_loans['decision'].value_counts()`
- Check edge cases: what if `monthly_repayment` is 0?
