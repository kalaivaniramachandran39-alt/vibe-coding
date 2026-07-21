# Exercise 4C — Option B: Transaction Alert Generator
#
# STEP 0 — PLAN THE PLAN (do this before anything else):
# Open Copilot Chat and send this prompt:
# "Before writing any code, tell me your step-by-step plan for flagging
#  transactions against the alert rules below. Don't write code yet."
#
import pandas as pd

df = pd.read_csv('../../data/transactions_clean.csv')

# Alert rules (a transaction can match more than one):
#   HIGH_VALUE:         amount > 10000
#   CASH_LIMIT:         category == 'CASH_WITHDRAWAL' and amount > 5000
#   DUPLICATE_SUSPECT:  same customer_id, same amount, same date as another row

# TODO 1: Write a function/logic that returns a list of matched alert_types per row

# TODO 2: Build the flagged_transactions DataFrame with columns:
#         date, customer_id, amount, category, branch, alert_type, recommended_action

# TODO 3: Export to flagged_transactions.csv, sorted by amount descending

# --- EXTENSION ---
# TODO 4: Print a summary count by alert_type
