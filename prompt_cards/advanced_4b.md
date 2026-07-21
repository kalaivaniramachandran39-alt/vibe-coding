# Advanced Card — Exercise 4B: Reporting Pipeline
**Design & critique — use the Twice Rule**

---

Start with Card 0 (Plan the Plan), then paste into Copilot Chat:

```
Design a generate_report(df, threshold=10000) function that:
  • Computes segment summary with .groupby().agg()
  • Adds a high_value flag based on the threshold parameter
  • Exports to Excel with 3 sheets:
      'Segment Summary', 'Flagged Transactions', 'Branch Breakdown'
  • Applies openpyxl red fill to flagged rows
  • Returns a report_metadata dict (row counts, export path, timestamp)

The threshold must be configurable — it changes every quarter.
```

**Before you run:**
- **Twice Rule**: this report runs every month — threshold and output path must be parameters, not hardcoded values
- Check: does `ExcelWriter` use a context manager (`with pd.ExcelWriter(...) as writer`)?
- Check: openpyxl fill — does it use `PatternFill` with `fill_type='solid'`?
- Data check: verify no `customer_id` values appear in the branch breakdown
