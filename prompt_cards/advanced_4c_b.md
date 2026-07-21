# Advanced Card — Exercise 4C Option B: Configurable Alert Engine
**Design & critique — use the Twice Rule**

---

Start with Card 0 (Plan the Plan), then paste into Copilot Chat:

```
Design a generate_alerts(df, rules=None, output_path=None) function:
  • rules is a dict of {alert_name: filter_function} so new
    alert types can be added without changing the function
  • Default rules implement the 3 alert types:
      HIGH_VALUE, CASH_LIMIT, DUPLICATE_SUSPECT
  • Thresholds (10000, 5000) are parameters, not hardcoded
  • Returns flagged_df and a summary dict
  • Exports to output_path (default 'flagged_transactions.csv')
  • Sorts output by amount descending
```

**Before you run:**
- **Twice Rule**: alert rules change — the architecture must support adding new rules without rewriting the function
- Check: is duplicate detection using pandas `groupby + transform` or a merge? Avoid `iterrows`.
- Check: what happens if `df_clean` is empty? Add a guard.
- Data check: `recommended_action` must be deterministic — same input always gives same output
