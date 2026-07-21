# Banking Analytics Scripts — Agent Conventions

This file is read automatically by GitHub Copilot, Claude Code, Gemini CLI, Cursor,
and other AI coding tools. It encodes the coding standards for this workshop so that
all AI assistants apply them consistently without needing to be told in every prompt.

---

## Language & style

- Python 3.11. snake_case for all variable and function names.
- No camelCase. No abbreviations (`amount` not `amt`, `customer_id` not `cust`).
- Type hints required on all function signatures.
- Docstrings: Google style, public functions only.
- Formatter: black (line length 88). Linter: ruff.

## Naming conventions

- DataFrames: `df_` prefix (`df_transactions`, `df_clean`, `df_summary`).
- Output files: lowercase with underscores (`summary_report.csv`).
- Functions: verb_noun pattern (`clean_transactions`, `flag_high_value`).

## Pandas rules

- Never use `pd.iterrows()` — use vectorised operations.
- Always validate data types before arithmetic operations.
- Use `pd.to_datetime(errors='coerce')` for date parsing.

## What the agent must never do

- Never print `customer_id` or `amount` values in debug output.
- Never hard-code file paths — accept as function parameters.
- Never write bare `except:` clauses.

## Data handling

- Missing amounts: `fillna(0)` and add a `flag_missing` boolean column.
- Sentinel values (e.g. `-9999`): remove, do not fill.
- Category columns: strip whitespace and uppercase before any comparison.

## Workshop context

- All data in this repo is **synthetic**. No real bank customer data.
- The primary dataset is `data/transactions_messy.csv` (500 rows, 8 deliberate issues).
- Clean output goes to `data/transactions_clean.csv`.
- Exercise scripts live in `exercises/exercise_4a/`, `4b/`, `4c/`.
