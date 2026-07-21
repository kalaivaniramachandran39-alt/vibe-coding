# Instructor reference solution — Exercise 4C, Option A: Loan Eligibility Checker
import pandas as pd

# Configurable thresholds
INCOME_MULTIPLIER = 3
CREDIT_SCORE_THRESHOLD = 650
LTV_THRESHOLD = 0.80

df = pd.read_csv('../data/loan_applicants.csv')


def decide(row):
    income_ok = row['annual_income'] / 12 >= INCOME_MULTIPLIER * row['monthly_repayment']
    ltv_ok = row['loan_amount'] / row['property_value'] <= LTV_THRESHOLD
    credit_ok = row['credit_score'] >= CREDIT_SCORE_THRESHOLD

    if not income_ok or not ltv_ok:
        reasons = []
        if not income_ok:
            reasons.append('insufficient income')
        if not ltv_ok:
            reasons.append('LTV too high')
        return 'DECLINED', ', '.join(reasons)
    if not credit_ok:
        return 'REFERRED', 'credit score below threshold'
    return 'APPROVED', 'all checks passed'


df[['decision', 'reason']] = df.apply(decide, axis=1, result_type='expand')

df[['applicant_id', 'name', 'decision', 'reason']].to_csv('loan_decisions.csv', index=False)

print(df['decision'].value_counts())
