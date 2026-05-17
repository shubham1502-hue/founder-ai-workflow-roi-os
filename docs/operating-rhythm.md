# Operating Rhythm

Use this repo as a weekly AI leverage review system.

## Weekly cadence

### Friday: collect workflow drag

Ask each function to add workflows that caused delay, rework, customer friction, or founder time drain.

### Monday: run the system

Update the CSV and run:

```bash
make run
```

### Tuesday: review quick wins

Open `outputs/automation_priority_matrix.csv` and filter for `Quick wins`.

Assign one or two workflows that can be improved this week.

### Wednesday: assign pilots

Open `outputs/ai_implementation_backlog.csv`.

For each AI-assisted pilot, define:

- Owner
- Sample inputs
- Output quality checklist
- Human approval rule
- Success metric

### Weekly AI agent review cadence

If a workflow already has an AI agent or automation layer, review one agent workflow per week.

- Inspect input quality.
- Inspect execution and handoffs.
- Review failures and escalations.
- Check human adoption and trust.
- Estimate time saved, speed improved, or errors reduced.
- Decide scale, continue pilot, redesign, add human review, or stop.

### Thursday: review risk

Open `outputs/ai_operating_policy.md`.

Confirm:

- What data can be used
- What data should not be used
- Which workflows need approval
- Which workflows should stay manual

### Friday: update the weekly operating review

Bring these items into the weekly operating review:

- Hours saved
- Errors reduced
- Pilots completed
- Workflows blocked by missing process
- Hire vs automate decisions
- Workflows to revisit next week

## Monthly review

Once per month, revisit:

- Blended hourly cost
- Risk tolerance
- Setup cost assumptions
- Maintenance cost assumptions
- Actual hours saved
- Whether a pilot should become automation
- Whether manual work now needs a hire or contractor
