# AI ROI Review Prompt

Use this prompt after generating `outputs/workflow_roi_scorecard.csv`.

```text
You are helping a founder review an AI workflow ROI scorecard.

I will paste rows from a deterministic scorecard. Do not invent missing data. Do not recommend automation only because AI is possible. Focus on ROI, risk, payback period, customer impact, and founder operating leverage.

For each workflow, assess:
- Why this workflow is or is not a good AI candidate
- What assumption most affects ROI
- What risk could make automation a bad idea
- What evidence would increase confidence
- What the founder should do in the next 7 days

Then produce:
1. Top workflows to automate now
2. Workflows to pilot first
3. Workflows that should stay manual
4. Workflows that need a hire or owner
5. Risks the founder should review before approving AI use

Scorecard rows:
[paste rows here]
```
