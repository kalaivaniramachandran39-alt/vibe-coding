# Exercise 4C — Option A: Loan Eligibility Checker
#
# STEP 0 — PLAN THE PLAN (do this before anything else):
# Open Copilot Chat and send this prompt:
# "Before writing any code, tell me your step-by-step plan for applying
#  the lending rules below to each applicant. Don't write code yet."
#
import pandas as pd

df = pd.read_csv('../../data/loan_applicants.csv')

# Lending rules:
#   Income sufficiency: annual_income / 12 >= 3 * monthly_repayment   -> else DECLINED
#   Credit score:        credit_score >= 650                          -> else REFERRED
#   Loan-to-Value:       loan_amount / property_value <= 0.80         -> else DECLINED

# TODO 1: Write a function that takes a row and returns (decision, reason)

# TODO 2: Apply the function to every row to create 'decision' and 'reason' columns

# TODO 3: Export applicant_id, name, decision, reason to loan_decisions.csv

# --- EXTENSION ---
# TODO 4: Move the thresholds (650, 0.80, the "3x" multiplier) into variables at the top
# TODO 5: Print a summary count of APPROVED / REFERRED / DECLINED
