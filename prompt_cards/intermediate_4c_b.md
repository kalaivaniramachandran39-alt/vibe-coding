# Intermediate Card — Exercise 4C Option B: Transaction Alert Generator
**Write your own 5-element prompt**

---

Start with Card 0 (Plan the Plan), then use the TASK / INPUT / LOGIC / OUTPUT / LIBRARIES framework:

```
TASK:      Build a transaction alert generator
INPUT:     df_clean (your output from Exercise 4A)
LOGIC:     Flag on 3 rules:
             HIGH_VALUE: amount > 10000
             CASH_LIMIT: category == CASH_WITHDRAWAL & amount > 5000
             DUPLICATE_SUSPECT: same customer_id, amount, date
           Add alert_type and recommended_action columns
OUTPUT:    flagged_transactions.csv, sorted by amount descending
LIBRARIES: pandas
```

**Before you run:**
- Write your own prompt — use all 5 elements
- Consider: should a transaction be flagged by multiple rules, or just the first match?
- Extension: add a summary count by `alert_type`
