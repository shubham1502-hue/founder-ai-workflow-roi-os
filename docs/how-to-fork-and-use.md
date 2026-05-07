# How to Fork and Use

This guide is for founders and operators who want the simplest path.

## Step 1: Fork the repo

Open the GitHub repo and click Fork. Keep the name or rename it for your company.

## Step 2: Clone your fork

```bash
git clone https://github.com/YOUR-USERNAME/founder-ai-workflow-roi-os.git
cd founder-ai-workflow-roi-os
```

## Step 3: Install dependencies

```bash
make install
```

The project uses Python, pandas, PyYAML, and pytest. It does not require an API key.

## Step 4: Replace the sample data

Open `data/sample_workflows.csv`.

Replace the synthetic rows with your own workflows. Keep the column names exactly the same.

If you are not ready to fill every field perfectly, use reasonable estimates. The goal is to support a founder decision, not create an accounting system.

## Step 5: Edit the company profile

Open `config/company_profile.yml`.

Update:

- Company name
- Stage
- Team size
- Business model
- AI maturity
- Burn sensitivity
- Hiring constraints
- Preferred tools
- Risk tolerance
- Sensitive data categories
- Functions to prioritize
- Functions to avoid for now
- Founder operating goals

## Step 6: Optionally edit scoring rules

Open `config/scoring_rules.yml`.

Change this file if your company has different assumptions for:

- Blended hourly cost
- Setup cost by complexity
- Maintenance cost
- Automation coverage
- Scoring weights
- Decision notes

## Step 7: Run the system

```bash
make run
```

You can also run the CLI directly:

```bash
python -m founder_ai_workflow_roi.cli run \
  --input data/sample_workflows.csv \
  --company-config config/company_profile.yml \
  --scoring-config config/scoring_rules.yml \
  --output-dir outputs
```

## Step 8: Interpret the outputs

Read these first:

1. `outputs/founder_ai_roi_memo.md`
2. `outputs/workflow_roi_scorecard.csv`
3. `outputs/hire_vs_automate_decisions.csv`
4. `outputs/ai_implementation_backlog.csv`

Use the memo in your weekly operating review. Use the backlog to assign owners.

## Non-technical path

If you only want the simplest path:

1. Replace one CSV.
2. Edit one YAML file.
3. Run one command.
4. Read one memo.
