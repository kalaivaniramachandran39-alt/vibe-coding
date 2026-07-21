# Beginner Cards — Exercise 4C Option B: Transaction Alert Generator
**Start with Card 0 (Plan the Plan) before using any card below.**

Each card below = one fresh Copilot Chat conversation.

---

## Card 4C-B-B — Alert generator (guided)

Paste into Copilot Chat:
```
"I have a cleaned pandas DataFrame called df_clean with
columns: date, customer_id, segment, product, amount,
currency, category, branch.

Flag transactions matching any of these three rules:
1. HIGH_VALUE:        amount > 10000
2. CASH_LIMIT:        category == 'CASH_WITHDRAWAL'
                      AND amount > 5000
3. DUPLICATE_SUSPECT: same customer_id, same amount,
                      same date

Add an alert_type column (use the rule name above).
Add a recommended_action column with a plain-English
description of what should happen.
Save flagged rows to flagged_transactions.csv."
```

**Before you run:**
- Test: run `df_clean[df_clean['amount'] > 10000].shape` before coding — how many HIGH_VALUE rows?
- A transaction can match more than one rule — decide how to handle this (first match wins, or list all)
- Run `df_flagged['alert_type'].value_counts()` to see your results

---

## Extension — Summary by alert type

Paste into Copilot Chat:
```
"Write Python code to print a count of flagged
transactions per alert_type."
```

**Before you run:**
- Sort the output by `amount` descending before exporting
