# Intermediate Card — Exercise 4A: Data Cleaning
**Write your own 5-element prompt for each issue**

---

Start with Card 0 (Plan the Plan), then write your own prompt for each of the 8 issues using the TASK / INPUT / LOGIC / OUTPUT / LIBRARIES framework:

```
TASK:      Clean the transaction dataset
INPUT:     df with columns: date, customer_id, segment,
           product, amount, currency, category, branch
LOGIC:     Fix the 8 issues below (one prompt per issue):
             1. amount has $ signs → strip and convert to float
             2. date has mixed formats → standardise to datetime
             3. category has mixed case → strip and uppercase
             4. duplicate rows → remove
             5. missing amount → fillna(0) + flag_missing column
             6. amount == -9999 → remove rows
             7. branch has whitespace → strip
             8. customer_id wrong format → add flag_bad_id
OUTPUT:    Cleaned DataFrame df
LIBRARIES: pandas
```

**Before you run:**
- Write one prompt per issue — don't combine all 8 in one prompt
- After each fix, run `df.info()` to verify the change
- Save output: `df.to_csv('data/transactions_clean.csv', index=False)`
