# Beginner Cards — Exercise 4A: Data Cleaning
**Start with Card 0 (Plan the Plan) before using any card below.**

Each card below = one fresh Copilot Chat conversation. Close the previous chat before starting the next.

---

## Card 4A-B1 — Strip $ signs from amount

Paste into Copilot Chat:
```
"I have a Pandas DataFrame called df. The column amount
contains strings like "$1,250.00". Write Python code to
strip the $ symbol and commas, then convert the column
to float. Store the result back in df['amount']."
```

**Before you run:**
- `amount` should now show as `float64` in `df.dtypes`
- Test: `print(df['amount'].dtype)`

---

## Card 4A-B2 — Standardise mixed date formats

Paste into Copilot Chat:
```
"My df['date'] column has dates in three formats:
YYYY-MM-DD, DD/MM/YYYY, and Mon DD YYYY.
Write Python code using pd.to_datetime with
errors='coerce' to convert all to datetime."
```

**Before you run:**
- Run `df['date'].dtype` — should show `datetime64`
- `NaT` means a date couldn't be parsed — check that row

---

## Card 4A-B3 — Uppercase and strip category

Paste into Copilot Chat:
```
"Write Python code to strip leading and trailing
whitespace from df['category'] and convert all
values to uppercase. Store back in df['category']."
```

**Before you run:**
- Run `df['category'].unique()` — all values should be UPPERCASE with no spaces

---

## Card 4A-B4 — Remove duplicate rows

Paste into Copilot Chat:
```
"Write one line of pandas code to remove fully duplicate
rows from df (all columns identical). Keep the first
occurrence."
```

**Before you run:**
- Run `df.shape` before and after — row count should decrease by ~15

---

## Card 4A-B5 — Handle missing amounts

Paste into Copilot Chat:
```
"My df['amount'] has missing values (NaN). Write Python
code to:
(1) add a boolean column flag_missing that is True where
    amount is NaN;
(2) fill the missing amount values with 0."
```

**Before you run:**
- Run `df['flag_missing'].sum()` — should be ~20
- `df['amount'].isna().sum()` should now be 0

---

## Card 4A-B6 — Remove sentinel −9999 values

Paste into Copilot Chat:
```
"Write Python code to remove all rows from df where
df['amount'] == -9999. Use boolean indexing and
reassign to df."
```

**Before you run:**
- Run `(df['amount'] == -9999).sum()` — should be 0 after removal

---

## Card 4A-B7 — Strip whitespace from branch

Paste into Copilot Chat:
```
"Write one line of pandas code to strip leading and
trailing whitespace from the branch column in df."
```

**Before you run:**
- Run `df['branch'].unique()` — no entry should have leading or trailing spaces

---

## Card 4A-B8 — Flag invalid customer IDs

Paste into Copilot Chat:
```
"My df['customer_id'] should follow the format CUST_
followed by exactly 6 digits (e.g. CUST_123456).
Add a boolean column flag_bad_id that is True for rows
that do NOT match this pattern. Use str.match()."
```

**Before you run:**
- Run `df['flag_bad_id'].sum()` — should be ~10
- Don't remove these rows — just flag them

---

**Done?** Save your cleaned data:
```python
df.to_csv('data/transactions_clean.csv', index=False)
```
You'll need it for Exercise 4B.
