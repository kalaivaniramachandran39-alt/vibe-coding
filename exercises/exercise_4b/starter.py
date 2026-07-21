# Exercise 4B — Data Transformation & Reporting
#
# STEP 0 — PLAN THE PLAN (do this before anything else):
# Open Copilot Chat and send this prompt:
# "Before writing any code, tell me your step-by-step plan for transforming
#  this dataset into summary reports. Don't write code yet."
#
import pandas as pd

df = pd.read_csv('../../data/transactions_clean.csv')

# TODO 1: Compute total and average amount by customer segment

# TODO 2: Add a 'high_value' boolean column (True where amount > 10000)

# TODO 3: Export summary to CSV

# --- EXTENSION ---
# TODO 4: Export to Excel with two sheets: Segment Summary and Flagged Transactions

# TODO 5: Add a Branch Breakdown sheet
