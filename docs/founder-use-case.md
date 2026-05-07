# Founder Use Case

## Scenario

A seed-stage B2B SaaS founder has a 14-person team and keeps hearing that the company should use more AI. The problem is that the team already has too many manual workflows, and it is not obvious which ones are worth automating.

The founder lists 20 workflows across sales, customer success, operations, finance, reporting, hiring, support, product feedback, RevOps, and founder admin.

Examples include:

- Cleaning CRM data
- Summarizing sales calls
- Drafting customer success check-ins
- Tagging support tickets
- Preparing investor update drafts
- Compiling weekly metrics
- Reconciling contractor invoices
- Preparing hiring scorecards
- Analyzing churn reasons
- Updating project trackers

## What the founder does

1. Replaces `data/sample_workflows.csv` with the company's workflow inventory.
2. Edits `config/company_profile.yml` to match stage, team size, risk tolerance, preferred tools, and sensitive data categories.
3. Runs `make run`.
4. Opens `outputs/founder_ai_roi_memo.md`.
5. Uses `outputs/ai_implementation_backlog.csv` to assign owners and timing.

## What the system shows

The system separates workflows into practical operating decisions:

- Automate now
- Run AI-assisted pilot
- Hire
- Outsource
- Document process first
- Keep manual for now

The founder can now avoid random AI experiments and focus the team on the highest-leverage work.

## Example decision pattern

A high-frequency support ticket routing workflow with low process variability and low human judgment gets ranked as a quick win. It is likely worth automating now.

A customer onboarding workflow with high customer impact, many exceptions, and human judgment gets routed toward a pilot or process documentation first.

A hiring scorecard workflow with sensitive data and high judgment gets treated as human-owned work, with AI limited to preparation and formatting.

## Meeting outcome

Instead of debating whether the company should use AI, the founder can run a focused operating review:

- Which workflows save the most time?
- Which have short payback periods?
- Which are too risky to automate?
- Which should become AI pilots this week?
- Which need a hire or contractor?
- Which should be ignored until volume grows?
