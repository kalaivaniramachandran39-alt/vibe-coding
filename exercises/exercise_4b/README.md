# Exercise 4B — Data Transformation & Reporting
**Time:** 20 minutes  |  **Dataset:** `data/transactions_clean.csv` (your output from 4A)

## Your task
Transform the clean data into business-ready reports.

## Core tasks
1. Compute **total and average transaction amount by customer segment** using `.groupby().agg()`
2. Add a `high_value` boolean column — `True` where `amount > 10000`
3. Export a summary table to `summary_report.csv`

## Extension (Intermediate / Advanced)
4. Use `pd.ExcelWriter` to produce `transaction_report.xlsx` with two sheets:
   - Sheet 1: `Segment Summary`
   - Sheet 2: `Flagged Transactions` (only rows where `high_value` is True)
5. Add a third sheet: `Branch Breakdown` — count of high-value transactions per branch
6. **Advanced bonus**: apply red fill to flagged rows using `openpyxl` styles

## Prompt tip
Include the column names and expected output format in your prompt.
Tell Copilot exactly what libraries to use.

## Verify your output (don't just run — assert)

After generating code, add these checks before moving to Exercise 4C.
If any assertion fails, the generated code has a bug — go back and fix it.

```python
# Paste these lines at the end of your script and run them
assert 'high_value' in df.columns, "missing high_value column"
assert df['high_value'].dtype == bool, "high_value should be boolean"
assert df.loc[df['amount'] > 10000, 'high_value'].all(), "high_value not set correctly"
assert df.loc[df['amount'] <= 10000, 'high_value'].eq(False).all(), "false positives in high_value"

import pathlib
assert pathlib.Path('summary_report.csv').exists(), "summary_report.csv not saved"
print("All checks passed.")
```

> **Why assertions instead of just looking?** Visual inspection misses edge cases.
> An assertion either passes or tells you exactly what broke.
> This is the same technique used to verify this repo was built correctly.
