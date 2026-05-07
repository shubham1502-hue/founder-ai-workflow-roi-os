# Workflow Mapping Prompt

Use this prompt with any AI assistant if you want help creating your workflow inventory manually. Do not include private customer data, secrets, or sensitive financial details.

```text
You are helping an early-stage founder map company workflows for an AI automation ROI review.

Company context:
- Stage:
- Team size:
- Business model:
- Functions:
- Current tools:
- Sensitive data categories:

Task:
Create a workflow inventory with at least 20 workflows across sales, customer success, operations, finance, reporting, hiring, founder admin, RevOps, support, and product feedback.

For each workflow, fill these fields:
- workflow_id
- function
- workflow_name
- owner_role
- current_tooling
- workflow_description
- frequency_per_month
- avg_time_minutes_per_run
- people_involved
- error_rate_percent
- monthly_volume
- business_impact, 1 to 5
- customer_impact, 1 to 5
- data_sensitivity, low medium or high
- process_variability, low medium or high
- current_pain, low medium or high
- current_cost_signal, low medium or high
- automation_idea
- requires_human_judgment, yes or no
- current_status

Return the result as a CSV-ready table. Keep the data fictionalized if you are using examples.
```
