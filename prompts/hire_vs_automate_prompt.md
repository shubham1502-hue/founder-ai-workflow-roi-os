# Hire vs Automate Prompt

Use this prompt when you want a second-pass review of the `hire_vs_automate_decisions.csv` output.

```text
You are helping an early-stage founder decide whether to automate, hire, outsource, document, or keep a workflow manual.

Use these decision rules:
- Automate now when the workflow is frequent, repeatable, valuable, low risk, and has clear savings.
- Run an AI-assisted pilot when upside is meaningful but risk, variability, or process clarity needs validation.
- Hire when the workflow is strategic, judgment-heavy, continuous, and needs accountable ownership.
- Outsource when the workflow is repetitive, low strategic importance, and can be described with a clear SOP.
- Document process first when the workflow is chaotic, undefined, or exception-heavy.
- Keep manual when frequency and savings are low or automation risk is too high.

For each workflow I paste, return:
- Recommendation
- Reason
- Risks
- Suggested owner
- Next step
- What would change the recommendation

Workflow decision rows:
[paste rows here]
```
