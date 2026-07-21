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
segment_summary = df.groupby('segment')['amount'].agg(['sum', 'mean']).reset_index()
segment_summary = segment_summary.rename(columns={'sum': 'total_amount', 'mean': 'average_amount'})

# TODO 2: Add a 'high_value' boolean column (True where amount > 10000)
df['high_value'] = df['amount'] > 10000

# TODO 3: Export summary to CSV
segment_summary.to_csv('../../data/segment_summary.csv', index=False)

# --- EXTENSION ---
# TODO 4: Export to Excel with two sheets: Segment Summary and Flagged Transactions
flagged_transactions = df[df['high_value']].copy()
branch_breakdown = (
    df.groupby('branch')['amount']
    .agg(['sum', 'mean', 'count'])
    .reset_index()
    .rename(columns={'sum': 'total_amount', 'mean': 'average_amount', 'count': 'transaction_count'})
)
with pd.ExcelWriter('../../data/segment_report.xlsx') as writer:
    segment_summary.to_excel(writer, sheet_name='Segment Summary', index=False)
    flagged_transactions.to_excel(writer, sheet_name='Flagged Transactions', index=False)
    branch_breakdown.to_excel(writer, sheet_name='Branch Breakdown', index=False)

# TODO 5: Add a Branch Breakdown sheet
