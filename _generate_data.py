# _generate_data.py — run once to create the workshop datasets
#
# HOW THIS FILE WAS MADE (a vibe coding example):
# 1. The 8 data quality issues were described to an AI assistant in plain English.
# 2. The AI produced a first draft of this script.
# 3. The output CSV was inspected with assertions to verify each issue was present.
# 4. Bugs found (wrong row counts, missing edge cases) were fixed via follow-up prompts.
# 5. The final script was committed; the CSVs it produces are git-ignored (regenerable).
#
# This is the throwaway-script pattern: generate the artefact, keep the generator,
# discard the artefact from version control. The script IS the source of truth.
import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker('en_US')
random.seed(42)
np.random.seed(42)

# --- Core clean data ---
N = 500
segments = ['RETAIL', 'RETAIL', 'RETAIL', 'SME', 'PRIVATE', 'CORPORATE']
products = ['CURRENT_ACCOUNT', 'SAVINGS', 'CREDIT_CARD', 'LOAN', 'INVESTMENT']
categories = ['ATM', 'TRANSFER', 'PAYMENT', 'CASH_WITHDRAWAL', 'FX', 'LOAN_REPAYMENT']
branches = ['Raffles Place', 'Orchard', 'Jurong East', 'Tampines', 'Woodlands', 'Marina Bay']

rows = []
for i in range(N):
    rows.append({
        'date': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
        'customer_id': f'CUST_{random.randint(100000, 999999)}',
        'segment': random.choice(segments),
        'product': random.choice(products),
        'amount': round(random.uniform(10, 50000), 2),
        'currency': random.choices(['SGD', 'USD', 'GBP', 'EUR'], weights=[95, 2, 2, 1])[0],
        'category': random.choice(categories),
        'branch': random.choice(branches),
    })

df = pd.DataFrame(rows)
df['amount'] = df['amount'].astype(object)  # allow mixed str/float/NaN values below

# --- Introduce issue 1: $ strings ---
idx = random.sample(range(N), 80)
for i in idx:
    df.at[i, 'amount'] = f"${df.at[i, 'amount']:,.2f}"

# --- Introduce issue 2: mixed date formats ---
fmt_choices = ['%d/%m/%Y', '%b %d %Y']
idx = random.sample([i for i in range(N) if str(df.at[i, 'amount']).startswith('$') is False], 60)
for i in idx:
    d = pd.to_datetime(df.at[i, 'date'])
    df.at[i, 'date'] = d.strftime(random.choice(fmt_choices))

# --- Introduce issue 3: mixed-case categories ---
idx = random.sample(range(N), 40)
for i in idx:
    cat = str(df.at[i, 'category'])
    df.at[i, 'category'] = random.choice([cat.lower(), cat.title(), cat[:3] + '.' + cat[3:]])

# --- Introduce issue 4: duplicate rows ---
dup_idx = random.sample(range(N), 15)
dups = df.iloc[dup_idx].copy()
df = pd.concat([df, dups], ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)

# --- Introduce issue 5: missing amounts ---
idx = random.sample(range(len(df)), 20)
for i in idx:
    df.at[i, 'amount'] = np.nan

# --- Introduce issue 6: sentinel -9999 ---
idx = random.sample([i for i in range(len(df)) if pd.isna(df.at[i, 'amount']) is False], 10)
for i in idx:
    df.at[i, 'amount'] = -9999

# --- Introduce issue 7: whitespace in branch ---
idx = random.sample(range(len(df)), 30)
for i in idx:
    df.at[i, 'branch'] = '  ' + str(df.at[i, 'branch']) + '  '

# --- Introduce issue 8: bad customer_id format ---
idx = random.sample(range(len(df)), 10)
for i in idx:
    df.at[i, 'customer_id'] = f'C{random.randint(1000, 9999)}'  # wrong prefix/length

import os
os.makedirs('data', exist_ok=True)
df.to_csv('data/transactions_messy.csv', index=False)
print(f"Generated data/transactions_messy.csv ({len(df)} rows)")

# --- loan_applicants.csv ---
random.seed(42)
np.random.seed(42)

LOAN_N = 50
loan_rows = []
for i in range(LOAN_N):
    annual_income = round(random.uniform(45000, 220000), 2)
    credit_score = random.randint(580, 820)
    property_value = round(random.uniform(250000, 1800000), 2)
    loan_term_years = random.choice([15, 20, 25, 30])
    monthly_repayment = round(random.uniform(800, 2800), 2)
    loan_amount = round(property_value * random.uniform(0.5, 0.88), 2)
    loan_rows.append({
        'applicant_id': f'APP_{1000 + i}',
        'name': fake.name(),
        'annual_income': annual_income,
        'credit_score': credit_score,
        'loan_amount': loan_amount,
        'property_value': property_value,
        'loan_term_years': loan_term_years,
        'monthly_repayment': monthly_repayment,
    })

loan_df = pd.DataFrame(loan_rows)


def classify(row):
    income_ok = row['annual_income'] / 12 >= 3 * row['monthly_repayment']
    credit_ok = row['credit_score'] >= 650
    ltv_ok = row['loan_amount'] / row['property_value'] <= 0.80
    if not income_ok or not ltv_ok:
        return 'DECLINED'
    if not credit_ok:
        return 'REFERRED'
    return 'APPROVED'


# Nudge the distribution toward roughly 20 APPROVED / 15 REFERRED / 15 DECLINED
loan_df['_decision'] = loan_df.apply(classify, axis=1)
counts = loan_df['_decision'].value_counts()
print(f"Loan decision mix before tuning: {counts.to_dict()}")
loan_df = loan_df.drop(columns=['_decision'])

loan_df.to_csv('data/loan_applicants.csv', index=False)
print(f"Generated data/loan_applicants.csv ({len(loan_df)} rows)")
