# explore.py — run this first: python explore.py
# This script profiles the workshop dataset so you can see what needs cleaning.

import pandas as pd

print("=" * 60)
print("Bank Transaction Data — Initial Profile")
print("=" * 60)

df = pd.read_csv('data/transactions_messy.csv')

print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns")
print("\nColumn types:")
print(df.dtypes)
print("\nFirst 5 rows:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())
print("\nDescriptive statistics:")
print(df.describe(include='all'))
print("\n" + "=" * 60)
print("What do you notice? Discuss with your partner before starting Exercise 4A.")
print("=" * 60)
