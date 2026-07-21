# Instructor reference solution — Exercise 4C, Option B: Transaction Alert Generator
import pandas as pd

df = pd.read_csv('../data/transactions_clean.csv')

ACTIONS = {
    'HIGH_VALUE': 'Review with customer',
    'CASH_LIMIT': 'Verify cash source',
    'DUPLICATE_SUSPECT': 'Check for duplicate posting',
}

df['is_high_value'] = df['amount'] > 10000
df['is_cash_limit'] = (df['category'] == 'CASH_WITHDRAWAL') & (df['amount'] > 5000)
df['is_duplicate_suspect'] = df.duplicated(subset=['customer_id', 'amount', 'date'], keep=False)

rule_cols = ['is_high_value', 'is_cash_limit', 'is_duplicate_suspect']
rule_names = ['HIGH_VALUE', 'CASH_LIMIT', 'DUPLICATE_SUSPECT']


def alert_types(row):
    return ', '.join(name for col, name in zip(rule_cols, rule_names) if row[col])


df['alert_type'] = df.apply(alert_types, axis=1)
flagged = df[df[rule_cols].any(axis=1)].copy()
flagged['recommended_action'] = flagged['alert_type'].apply(
    lambda types: '; '.join(ACTIONS[t] for t in types.split(', '))
)

output_cols = ['date', 'customer_id', 'amount', 'category', 'branch', 'alert_type', 'recommended_action']
flagged[output_cols].sort_values('amount', ascending=False).to_csv(
    'flagged_transactions.csv', index=False
)

print(flagged['alert_type'].value_counts())
