# Card 0 — Plan the Plan
**Universal — use this FIRST, before every exercise, regardless of tier**

---

Before writing any code, ask Copilot Chat:

```
"Before writing any code, tell me your step-by-step plan for
solving this problem. What will you do, in what order?
Don't write any code yet."
```

**After you receive the plan:**

✓ Read it. Does it address every issue listed in this exercise?  
✓ Correct any wrong assumptions before asking for code.  
✓ **Define your sensor** — write down the test or check that confirms success *before* generating any code.  
  Examples: `df['amount'].dtype == 'float64'`, or row count drops from 515 → ~500.  
✓ Then say: **"Execute step 1 only."** Work one step at a time.  
✓ **Start a fresh Copilot Chat for each issue** — don't build up one long session.  
  Long conversations drift as the AI summarises earlier detail away.

---

**Why this works:** AI without a plan takes shortcuts and misses edge cases. Defining the sensor before generating code means you know exactly what "done" looks like. Short sessions per task prevent context drift.

> **If Copilot Chat runs out:** open claude.ai or chatgpt.com in a new tab. Same loop, different chat window.
