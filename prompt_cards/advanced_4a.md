# Advanced Card — Exercise 4A: Data Cleaning with Quality Report
**Design & critique — use the Twice Rule**

---

Start with Card 0 (Plan the Plan), then paste into Copilot Chat:

```
Design a clean_transactions(df) function that:
  • Fixes all 8 issues in the correct order
  • Keeps a quality_report dict counting rows affected per issue
  • Returns (df_clean, quality_report)
  • Has configurable sentinel value (default -9999)
  • Raises a warning if >10% of rows are dropped

Use AI for boilerplate; write the logic spec yourself.
Critique: check for vectorised ops, no iterrows(), type safety.
```

**Before you run:**
- **Twice Rule**: this function will be called every month — make thresholds configurable parameters, not hardcoded values
- Check: does the AI use `pd.iterrows()`? If so, reject and ask for a vectorised equivalent
- Check: are all column names used as strings, not hardcoded indices?
- Data check: no `customer_id` or `amount` values should be printed in debug output
