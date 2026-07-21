# Beginner Cards — Exercise 4B: Data Transformation & Reporting
**Start with Card 0 (Plan the Plan) before using any card below.**

Each card below = one fresh Copilot Chat conversation.

---

## Card 4B-B1 — Segment summary

Paste into Copilot Chat:
```
"I have a cleaned pandas DataFrame called df_clean
with columns: date, customer_id, segment, product,
amount (float), currency, category, branch.
Use .groupby('segment').agg() to compute the total
and average amount per segment. Store the result in
a variable called segment_summary."
```

**Before you run:**
- Run `print(segment_summary)` — should show 4 rows (RETAIL, SME, PRIVATE, CORPORATE)
- Make sure you're using `df_clean`, not the original messy `df`

---

## Card 4B-B2 — Flag high-value transactions

Paste into Copilot Chat:
```
"Add a boolean column called high_value to df_clean.
It should be True where amount is greater than 10000."
```

**Before you run:**
- Run `df_clean['high_value'].sum()` — shows the count of flagged rows

---

## Card 4B-B3 — Export to CSV

Paste into Copilot Chat:
```
"Write Python code to save segment_summary to a file
called summary_report.csv in the data/ folder.
Do not include the row index."
```

**Before you run:**
- Check the `data/` folder in the file explorer — `summary_report.csv` should appear

---

## Extension — Multi-sheet Excel report

Paste into Copilot Chat:
```
"Using pandas and pd.ExcelWriter with the openpyxl
engine, write Python code to create a file called
transaction_report.xlsx with two sheets:
'Segment Summary' (the segment_summary DataFrame)
and 'Flagged Transactions' (only rows from df_clean
where high_value is True)."
```

**Before you run:**
- For Excel: use `pd.ExcelWriter` as a context manager
- Open the file in the file explorer to verify it looks right

---

## Extension — Branch breakdown sheet

Paste into Copilot Chat:
```
"Add a third sheet called 'Branch Breakdown' to the
same Excel file, containing a count of high-value
transactions per branch."
```
