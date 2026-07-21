# Exercise 4A — Data Cleaning & Wrangling
**Time:** 30 minutes  |  **Dataset:** `data/transactions_messy.csv`

## Your task
Fix the 8 known data quality issues in the transaction dataset using AI-generated Pandas code.

## The 8 issues (fix in this order)
1. `amount` column contains strings with `$` and commas — convert to float
2. `date` column has mixed date formats — standardise to `YYYY-MM-DD`
3. `category` has mixed case — standardise to uppercase
4. Some rows are fully duplicated — remove them
5. Some `amount` values are missing (NaN) — fill with `0` and add a `flag_missing` column
6. Some `amount` values are `-9999` (sentinel for "unknown") — remove these rows
7. `branch` column has leading/trailing whitespace — strip it
8. Some `customer_id` values don't follow the `CUST_XXXXXX` format — flag them

## How to work

**STEP 0 for ALL tiers — Plan the Plan:**
Before writing any code, open Copilot Chat and send:
> "Before writing any code, tell me your step-by-step plan for cleaning this dataset. What issues will you address, in what order? Don't write code yet."
Read the plan. Check it against the 8 issues below. Correct any gaps. Then execute.

- **Beginner**: use your prompt card (`prompt_cards/beginner_4a.md`) — the first card IS the plan-the-plan card
- **Intermediate**: write your own prompts using the 5-element framework
- **Advanced**: wrap the full pipeline in a `clean_transactions(df)` function that returns
  `(cleaned_df, quality_report_dict)` where the report summarises rows dropped/modified per issue

## Done?
Run `df.info()` and `df.describe()` on your cleaned DataFrame.
`amount` should be float64. `date` should be datetime64. No duplicates.

Save your cleaned data: `df_clean.to_csv('data/transactions_clean.csv', index=False)`
You'll need it for Exercise 4B.
