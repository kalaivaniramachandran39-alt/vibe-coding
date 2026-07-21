# Instructor reference solution — Exercise 4A
import re

import pandas as pd


def clean_transactions(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    report = {}
    df = df.copy()

    # 1. Strip $ and commas from amount, convert to float
    df['amount'] = (
        df['amount'].astype(str).str.replace(r'[$,]', '', regex=True)
    )
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # 2. Standardise mixed date formats
    df['date'] = pd.to_datetime(df['date'], format='mixed', errors='coerce')

    # 3. Standardise category to uppercase, strip stray punctuation/whitespace
    df['category'] = (
        df['category'].astype(str).str.strip().str.upper().str.replace('.', '', regex=False)
    )

    # 4. Remove fully duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    report['duplicates_removed'] = before - len(df)

    # 5. Flag and fill missing amounts
    df['flag_missing'] = df['amount'].isna()
    report['missing_amount_filled'] = int(df['flag_missing'].sum())
    df['amount'] = df['amount'].fillna(0)

    # 6. Remove sentinel -9999 rows
    before = len(df)
    df = df[df['amount'] != -9999]
    report['sentinel_rows_removed'] = before - len(df)

    # 7. Strip whitespace from branch
    df['branch'] = df['branch'].astype(str).str.strip()

    # 8. Flag invalid customer_id format
    df['flag_bad_id'] = ~df['customer_id'].astype(str).str.match(r'^CUST_\d{6}$')
    report['bad_customer_ids_flagged'] = int(df['flag_bad_id'].sum())

    report['final_row_count'] = len(df)
    return df, report


if __name__ == '__main__':
    raw = pd.read_csv('../data/transactions_messy.csv')
    cleaned, quality_report = clean_transactions(raw)
    cleaned.to_csv('../data/transactions_clean.csv', index=False)
    print('Quality report:', quality_report)
    print(cleaned.info())
