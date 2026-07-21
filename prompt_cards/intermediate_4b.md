# Intermediate Card — Exercise 4B: Data Transformation & Reporting
**Write your own 5-element prompt**

---

Start with Card 0 (Plan the Plan), then use the TASK / INPUT / LOGIC / OUTPUT / LIBRARIES framework:

```
TASK:      Transform clean transaction data into reports
INPUT:     df_clean (your output from Exercise 4A)
LOGIC:
             1. Compute total and average amount by segment
             2. Add high_value column (True where amount > 10000)
             3. Export segment summary to data/summary_report.csv
             Extension: export Excel with 2 sheets:
               Sheet 1 'Segment Summary'
               Sheet 2 'Flagged Transactions'
OUTPUT:    CSV file + optional Excel file
LIBRARIES: pandas, openpyxl (for Excel)
```

**Before you run:**
- Use `df_clean` from Exercise 4A — not the original messy `df`
- For Excel: use `pd.ExcelWriter` as a context manager
- Verify: open the CSV in the file explorer to confirm it looks right
