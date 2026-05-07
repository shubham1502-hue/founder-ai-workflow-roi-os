# Implementation Roadmap Prompt

Use this prompt after generating `outputs/ai_implementation_backlog.csv`.

```text
You are helping a founder turn an AI implementation backlog into a practical operating roadmap.

Constraints:
- Keep the plan lean.
- Do not require paid APIs.
- Do not automate sensitive workflows without human approval.
- Focus on the next 30 days first.
- Avoid generic AI recommendations.

Inputs:
- Company stage:
- Team size:
- Current tools:
- Risk tolerance:
- Backlog rows:
[paste backlog rows here]

Create a roadmap with:
1. Workflows to improve this week
2. AI-assisted pilots to run in the next 14 to 30 days
3. Workflows that need process documentation before automation
4. Workflows that need hiring or outsourcing decisions
5. Human approval rules
6. Metrics to track
7. What not to automate yet
```
