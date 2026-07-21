# Advanced Card — Exercise 4C Option A: Configurable Eligibility Engine
**Design & critique — use the Twice Rule**

---

Start with Card 0 (Plan the Plan), then paste into Copilot Chat:

```
Design a check_eligibility(df, income_mult=3.0, min_credit=650,
    max_ltv=0.80) function that:
  • Applies the 3 rules using the configurable thresholds
  • Handles edge cases (zero repayment, missing values)
  • Returns df with decision, reason, and pass_fail per rule columns
  • Prints a summary: N approved / N referred / N declined
  • Saves to a path parameter (default 'loan_decisions.csv')

Thresholds change each quarter — all must be configurable.
```

**Before you run:**
- **Twice Rule**: thresholds change quarterly — `income_mult`, `min_credit`, `max_ltv` must all be parameters
- Edge case: what if `monthly_repayment` is 0? (division by zero — add a guard)
- Check: does the AI use `.apply()` or vectorised boolean operations? Prefer vectorised.
- Check: are `NaN` values in the input handled before rules are applied?
