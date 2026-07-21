# The 5-Element Prompt Framework & Loop Engineering Checklist

Keep this open during the exercises.

---

## 5-Element Prompt Framework

Use this structure to write your own prompts. Works identically in Copilot Chat,
Claude, Gemini CLI, Cursor, and every other AI coding tool.

| Element | The question it answers |
|---------|------------------------|
| **TASK** | What do you want to build? |
| **INPUT** | What data, columns, types, and format are you starting with? |
| **LOGIC** | What rules and calculations should the code apply? |
| **OUTPUT** | What should the result look like — file, variable, format? |
| **LIBRARIES** | Which libraries should it use? (pandas, openpyxl, datetime…) |

### Worked example — Exercise 4A, Issue 1

**Weak prompt** (missing 4 of the 5 elements):
> "Clean the amount column."

**Strong prompt** (all 5 elements):
```
TASK:      Strip currency symbols from the amount column
INPUT:     df['amount'] contains strings like "$1,250.00" and "$80.00"
LOGIC:     Strip the $ symbol and commas, then convert to float
OUTPUT:    Store the result back in df['amount']
LIBRARIES: pandas string methods
```

### Quick-reference card

```
TASK      → What do you want to build?
INPUT     → df with columns: date, customer_id, amount, ...
LOGIC     → Rules and calculations to apply
OUTPUT    → What the result should look like
LIBRARIES → pandas, openpyxl, datetime…
```

**Specificity beats brevity.** A longer prompt that names the exact variable,
column, and expected format produces far better code than a short vague one.

---

## Loop Engineering Checklist

Apply this loop for every task, every tier:

1. **Plan the Plan** — ask for the approach before any code (Card 0)
2. **Define the sensor** — write down the test that confirms success  
   _before_ generating any code  
   Examples: `df['amount'].dtype == 'float64'`, row count drops 515 → ~500
3. **Start a fresh chat for each task** — don't build up one long session;  
   long conversations drift as the AI summarises earlier detail away
4. **Run the sensor after each change** — verify before moving on

---

## The Twice Rule (Advanced tier)

> If code will run more than twice, every threshold and file path
> must be a configurable parameter — never hardcoded.

Examples:
- `threshold=10000` not `amount > 10000` buried in the function body
- `output_path='loan_decisions.csv'` as a parameter with a default value
- `sentinel=-9999` not `-9999` scattered through the cleaning logic

The Twice Rule is the difference between a script and a tool.
