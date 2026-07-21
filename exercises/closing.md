# Closing Activity — 5 minutes

## Add one line to AGENTS.md

`AGENTS.md` is a convention file that AI coding tools read automatically at the
start of every session. It was generated during the setup of this workshop —
you've been working inside it all day.

Open `AGENTS.md` in the file explorer. Read the **Data handling** and
**Pandas rules** sections. Then add one line that captures something you
discovered during today's exercises — a rule, a gotcha, or a pattern that
you'd want an AI assistant to know before working with this kind of data.

### Examples of good additions

```markdown
- Always check for mixed date formats before arithmetic on date columns.
- `pd.to_datetime(errors='coerce')` silently converts unparseable dates to NaT — validate after.
- Strip whitespace from string columns before groupby, or group keys won't match.
- A -9999 sentinel is not the same as NaN — check for both before computing averages.
```

### How to do it

1. Open `AGENTS.md` (file explorer, repo root)
2. Find the section your rule belongs under
3. Add your line — write it as a rule the AI should follow, not as a note to yourself
4. Save the file

You can use Copilot to help you phrase it:
> "I want to add a coding rule to a conventions file. The rule is about [your observation].
> Write it as a single bullet point, phrased as an instruction to an AI assistant."

---

> **Why this matters**: every AI session that opens this repo will now apply
> your rule without being told. This is how good context compounds — the team's
> collective knowledge gets encoded once and benefits every future session.
