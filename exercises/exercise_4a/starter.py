# Exercise 4A — Data Cleaning & Wrangling
#
# STEP 0 — PLAN THE PLAN (do this before anything else):
# Open Copilot Chat and send this prompt:
# "Before writing any code, tell me your step-by-step plan for cleaning
#  this dataset. What issues will you address, in what order? Don't write code yet."
# Read the plan. Check it against the 8 issues below. Then ask Copilot to execute step 1.
#
# Use GitHub Copilot to complete each TODO block.
# Tip: write a comment describing what you want, then let Copilot suggest code.

import pandas as pd

# Load the messy dataset
df = pd.read_csv('../../data/transactions_messy.csv')

print(f"Loaded {len(df)} rows")
print(df.dtypes)

# TODO 1: Strip $ and commas from 'amount', convert to float

# TODO 2: Convert 'date' column to datetime (handle mixed formats)

# TODO 3: Strip whitespace and convert 'category' to uppercase

# TODO 4: Remove fully duplicate rows

# TODO 5: Fill missing 'amount' values with 0 and add a 'flag_missing' boolean column

# TODO 6: Remove rows where amount == -9999

# TODO 7: Strip whitespace from 'branch' column

# TODO 8: Flag rows where customer_id does not match 'CUST_' followed by 6 digits

# Save the cleaned data
df.to_csv('../../data/transactions_clean.csv', index=False)
print(f"Saved cleaned data: {len(df)} rows")
print(df.info())
