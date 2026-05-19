# Founder AI Workflow ROI OS

Decision system for founders deciding which workflows deserve AI automation, which need a hire, which can be outsourced, and which should stay manual.

Use this before building an AI agent, buying another AI tool, or opening a role. It prevents random AI experimentation by ranking workflows by ROI, risk, payback period, and operating priority. It also helps founders stay lean without pretending every workflow should become automation.

This is an offline-first decision system. It does not require a paid API, does not require an LLM, and does not send your workflow data anywhere. Replace one CSV, edit one YAML file, run one command, and read the roadmap.

In 10 minutes, it turns a messy workflow list into:

- A ranked AI automation ROI scorecard
- A hire vs automate vs outsource decision table
- A founder-ready AI ROI memo
- A 7-day action list for what to automate, pilot, document, hire for, outsource, or leave manual

## Start here

| Reader | Open first | Why | CTA |
| --- | --- | --- | --- |
| Founder | `outputs/founder_ai_roi_memo.md` | See which workflows are worth automating, piloting, hiring for, outsourcing, or keeping manual. | Pick one workflow to validate this week. |
| Non-technical operator | `docs/workflow-inventory-template.md` | Map workflows before running any code. | Copy the template and list 5 to 10 recurring workflows. |
| Technical operator | `config/scoring_rules.yml` | Inspect the scoring and what not to automate. | Run `make demo`, then compare outputs with the rules. |
| AI-agent operator | `docs/ai-agent-workflow-visibility-map.md` | Inspect input, execution, failure, adoption, ROI, and weekly review layers for an agent workflow. | Map one agent workflow before scaling it. |
| Hiring manager | `outputs/hire_vs_automate_decisions.csv` | See the operating judgment behind hire-vs-automate decisions. | Review the decision table with the AI ROI memo. |

The savings and payback figures are estimates from sample or user-supplied inputs, not confirmed outcomes.

## Use this instead of adjacent repos when

| If the operating problem is... | Use this repo | Use the adjacent repo instead when... |
| --- | --- | --- |
| Choosing automate, hire, outsource, or keep manual | Yes | Use `founder-hiring-talent-pipeline-os` after the decision is clearly headcount. |
| Ranking AI workflow opportunities by ROI and risk | Yes | Use `founder-weekly-operating-review-agent` when the weekly operating packet is already the main problem. |
| Evaluating repetitive post-sale, sales, support, reporting, or finance work | Yes | Use the source workflow repo first if the process itself is not yet defined. |
| Reviewing whether an AI agent is trusted and visible | Yes | Use `docs/ai-agent-workflow-visibility-map.md` inside this repo. |

## The founder problem

Founders know they should use AI and stay lean, but the hard question is where AI actually creates leverage. Most teams have scattered workflows across sales, customer success, operations, finance, hiring, reporting, product feedback, and founder admin. Some workflows are worth automating. Some need a hire. Some should be outsourced. Some should stay manual.

This repo turns workflow chaos into a ranked automation roadmap.

## What this repo does

- Maps company workflows
- Calculates time spent
- Estimates monthly cost
- Estimates AI automation savings
- Calculates payback period
- Scores automation priority
- Recommends automate vs hire vs outsource vs keep manual
- Generates an AI implementation backlog
- Creates a founder-ready AI ROI memo
- Creates an AI operating policy

## What a founder gets in 10 minutes

- Ranked workflows to automate now
- Workflows to pilot with AI
- Workflows that need a hire
- Workflows to outsource
- Workflows to avoid automating
- Estimated monthly savings
- AI implementation roadmap
- Founder AI ROI memo

## Before and after

Before:

- Scattered workflows
- Random AI experiments
- No ROI clarity
- Manual work hidden across the team
- Hiring and automation decisions made by gut feel

After:

- Workflow inventory
- ROI scorecard
- Automation priority matrix
- Hire vs automate decisions
- AI implementation backlog
- Founder-ready AI roadmap

## Who this is for

- Early-stage founders
- Founder's Office teams
- BizOps operators
- RevOps operators
- Startup generalists
- Seed-stage teams
- AI-first teams trying to stay lean

## Quick start

The shortest path is to replace one CSV, edit one YAML file, and run one command.

| Step | File or command | What to do |
| --- | --- | --- |
| 1 | `data/sample_workflows.csv` | Replace the sample workflows with your company workflows. |
| 2 | `config/company_profile.yml` | Edit company stage, team size, risk tolerance, sensitive data, and priority functions. |
| 3 | `make run` | Generate the scorecard, decisions, backlog, memo, roadmap, and AI policy. |
| 4 | `outputs/founder_ai_roi_memo.md` | Read this first in the founder operating review. |

Full setup:

1. Fork the repo.
2. Clone the repo.

```bash
git clone https://github.com/shubham1502-hue/founder-ai-workflow-roi-os.git
cd founder-ai-workflow-roi-os
```

3. Install dependencies.

```bash
make install
```

4. Edit `config/company_profile.yml`.
5. Replace `data/sample_workflows.csv` with your own workflow inventory.
6. Run the system.

```bash
make run
```

7. Review `outputs/`.

If you only want to see the demo outputs, run:

```bash
make demo
```

## Sample demo result

The bundled synthetic data produces a founder-ready recommendation set:

- Automate now: sales call summaries, CRM lifecycle cleanup, and support ticket routing.
- Pilot first: weekly metrics, customer onboarding, founder weekly review notes, and lead routing.
- Hire: judgment-heavy customer success, sales follow-up, and product feedback work.
- Outsource: repetitive project tracker updates.
- Keep manual or document first: sensitive finance, hiring, investor, and undefined competitor research workflows.

This is the intended shape of the system: not every workflow becomes an AI project.

## AI Agent Workflow Visibility Map

If a workflow already has an AI agent or automation layer, use the AI Agent Workflow Visibility Map to track what enters the agent, what the agent does, where it fails, whether humans trust it, and whether it creates operating leverage.

Open:

- `docs/ai-agent-workflow-visibility-map.md`
- `templates/ai_agent_workflow_visibility_map.csv`
- `examples/ai_agent_workflow_visibility_example.md`

This is useful for teams evaluating AI agents, piloting agent workflows, or trying to connect AI usage to time saved, decision speed, error reduction, and trust.

## How to fork and use this for your company

1. Click Fork on GitHub.
2. Rename the repo if needed.
3. Replace `data/sample_workflows.csv` with your company workflow inventory.
4. Edit `config/company_profile.yml`.
5. Edit `config/scoring_rules.yml` if your cost, risk, or priority assumptions differ.
6. Run `make run`.
7. Review `outputs/founder_ai_roi_memo.md` first.
8. Review `outputs/workflow_roi_scorecard.csv` second.
9. Optional: connect outputs to Google Sheets, Notion, Airtable, Linear, Asana, ClickUp, HubSpot, or your internal ops tracker.

Non-technical path:

- Replace one CSV
- Edit one YAML file
- Run one command
- Read one memo

## Standalone or integrated

Standalone:
Use this repo by itself if you only need to decide which workflows to automate, hire for, outsource, or keep manual. Fork it, replace the sample input, run the workflow or copy the templates, and use the main output in your next founder review.

Integrated:
Use this repo with the Founder OS ecosystem if you want to connect it to adjacent operating workflows.

- Use when GTM, sales, onboarding, support, finance, reporting, or weekly review work becomes repetitive or ops-heavy.
- Feed AI leverage priorities into [founder-weekly-operating-review-agent](https://github.com/shubham1502-hue/founder-weekly-operating-review-agent).
- Use after [founder-customer-onboarding-os](https://github.com/shubham1502-hue/founder-customer-onboarding-os) if onboarding summaries, SLA alerts, training reminders, or activation reporting need automation decisions.
- Use after [founder-retention-expansion-os](https://github.com/shubham1502-hue/founder-retention-expansion-os) if renewal alerts, expansion scoring, churn driver tagging, customer proof workflows, support summaries, or executive touch reminders need automation decisions.
- Use after [founder-product-feedback-roadmap-os](https://github.com/shubham1502-hue/founder-product-feedback-roadmap-os) if feedback tagging, product signal summaries, roadmap reporting, customer interview synthesis, support issue routing, or roadmap update workflows need automation decisions.
- Use after [founder-led-sales-call-os](https://github.com/shubham1502-hue/founder-led-sales-call-os) if call summaries, CRM updates, or objection tagging become repetitive.
- Use before [founder-hiring-talent-pipeline-os](https://github.com/shubham1502-hue/founder-hiring-talent-pipeline-os) when a workflow should become headcount instead of automation, outsourcing, or manual ownership.

## Lifecycle handoff

Before:

- [founder-os](https://github.com/shubham1502-hue/founder-os) for choosing the first operating module.
- A workflow inventory from any function.
- Pain signals from GTM, sales, onboarding, support, finance, or reporting.

This repo produces:

- AI ROI memo
- ROI scorecard
- Hire-vs-automate decisions
- AI implementation backlog
- Operating policy

After:

- [founder-weekly-operating-review-agent](https://github.com/shubham1502-hue/founder-weekly-operating-review-agent) for prioritizing AI work in the weekly review.
- [founder-hiring-talent-pipeline-os](https://github.com/shubham1502-hue/founder-hiring-talent-pipeline-os) when the decision is to hire.
- The relevant workflow owner for implementation, hiring, outsourcing, or manual documentation.

## Hiring decision handoff

Founder AI Workflow ROI OS helps decide whether a workflow should be automated, hired for, outsourced, or kept manual. If the decision is to hire, use [Founder Hiring Talent Pipeline OS](https://github.com/shubham1502-hue/founder-hiring-talent-pipeline-os) to define the role, score candidates, structure interviews, recommend trial projects, run reference checks, and create founder-ready hiring decisions.

## Where this fits in the Founder OS

Use `founder-ai-workflow-roi-os` to decide where AI should create leverage across the company.

- Use `founder-weekly-operating-review-agent` to roll AI leverage work into the weekly operating review.
- Use `founder-os-revenue-engine` to connect automation work to revenue bottlenecks.
- Use `founder-led-sales-call-os` for post-call sales intelligence.
- Use `ai-gtm-command-center` for pre-call GTM workflows.
- Use [founder-customer-onboarding-os](https://github.com/shubham1502-hue/founder-customer-onboarding-os) to track post-sale onboarding health, activation risk, owner gaps, and founder attention accounts.
- Use [founder-retention-expansion-os](https://github.com/shubham1502-hue/founder-retention-expansion-os) to track post-activation health, renewal risk, expansion readiness, churn drivers, and customer proof opportunities.
- Use [founder-product-feedback-roadmap-os](https://github.com/shubham1502-hue/founder-product-feedback-roadmap-os) to turn customer signals into roadmap decisions.
- Use [founder-hiring-talent-pipeline-os](https://github.com/shubham1502-hue/founder-hiring-talent-pipeline-os) when a workflow ROI decision becomes a hiring decision.
- Use `founder-os` as the umbrella operating system.

Related repos:

- [founder-os](https://github.com/shubham1502-hue/founder-os)
- [founder-customer-onboarding-os](https://github.com/shubham1502-hue/founder-customer-onboarding-os)
- [founder-retention-expansion-os](https://github.com/shubham1502-hue/founder-retention-expansion-os)
- [founder-product-feedback-roadmap-os](https://github.com/shubham1502-hue/founder-product-feedback-roadmap-os)
- [founder-hiring-talent-pipeline-os](https://github.com/shubham1502-hue/founder-hiring-talent-pipeline-os)
- [founder-weekly-operating-review-agent](https://github.com/shubham1502-hue/founder-weekly-operating-review-agent)
- [founder-os-revenue-engine](https://github.com/shubham1502-hue/founder-os-revenue-engine)
- [founder-led-sales-call-os](https://github.com/shubham1502-hue/founder-led-sales-call-os)
- [ai-gtm-command-center](https://github.com/shubham1502-hue/ai-gtm-command-center)

If onboarding work becomes repetitive or ops-heavy, use Founder AI Workflow ROI OS to decide whether onboarding summaries, SLA alerts, CRM updates, support tagging, training reminders, or activation reporting should be automated, piloted, hired for, outsourced, or kept manual. Use [Founder Customer Onboarding OS](https://github.com/shubham1502-hue/founder-customer-onboarding-os) as the source workflow when the problem is post-sale onboarding and activation.

If retention work becomes repetitive or ops-heavy, use Founder AI Workflow ROI OS to decide whether renewal alerts, expansion scoring, churn driver tagging, customer proof workflows, support summaries, or executive touch reminders should be automated, piloted, hired for, outsourced, or kept manual. Use [Founder Retention Expansion OS](https://github.com/shubham1502-hue/founder-retention-expansion-os) as the source workflow when the problem is post-activation retention, renewal, expansion, or customer proof.

If product operations become repetitive or ops-heavy, use Founder AI Workflow ROI OS to decide whether feedback tagging, product signal summaries, roadmap reporting, customer interview synthesis, support issue routing, or roadmap update workflows should be automated, piloted, hired for, outsourced, or kept manual. Use [Founder Product Feedback Roadmap OS](https://github.com/shubham1502-hue/founder-product-feedback-roadmap-os) as the source workflow when the problem is customer-signal-to-roadmap prioritization.

## Input format

The input CSV must include every column below.

| Column | Description |
| --- | --- |
| `workflow_id` | Stable ID such as `WF-001`. |
| `function` | Function that owns the workflow, such as Sales, Finance, or RevOps. |
| `workflow_name` | Short human-readable workflow name. |
| `owner_role` | Role accountable for the workflow today. |
| `current_tooling` | Tools currently used to complete the workflow. |
| `workflow_description` | Plain-language description of the work. |
| `frequency_per_month` | Number of times this workflow runs each month. |
| `avg_time_minutes_per_run` | Average minutes spent each time it runs. |
| `people_involved` | Number of people typically involved per run. |
| `error_rate_percent` | Estimated percent of runs with errors, rework, or misses. |
| `monthly_volume` | Count of units processed each month, such as tickets, calls, leads, or invoices. |
| `business_impact` | 1 to 5 score for company impact. |
| `customer_impact` | 1 to 5 score for customer impact. |
| `data_sensitivity` | Low, medium, or high sensitivity. |
| `process_variability` | Low, medium, or high variability. |
| `current_pain` | Low, medium, or high pain today. |
| `current_cost_signal` | Low, medium, or high cost signal. |
| `automation_idea` | Practical idea for AI assistance or automation. |
| `requires_human_judgment` | Yes or no. |
| `current_status` | Documented, partially_documented, ad_hoc, chaotic, or similar status. |

## Output files

- `outputs/workflow_roi_scorecard.csv`: ROI math, savings, payback period, priority score, score band, and recommendation.
- `outputs/automation_priority_matrix.csv`: Impact, effort, risk, quadrant, and recommended timing.
- `outputs/hire_vs_automate_decisions.csv`: Recommendation, reason, risks, owner, next step, and confidence.
- `outputs/ai_implementation_backlog.csv`: Action backlog grouped into implementation phases.
- `outputs/founder_ai_roi_memo.md`: Founder-ready memo for deciding what to do next.
- `outputs/ai_workflow_roadmap.md`: Phased roadmap for quick wins, pilots, deeper automation, and hiring or outsourcing decisions.
- `outputs/ai_operating_policy.md`: Guardrails for AI use, human approval, data sensitivity, review cadence, and owner responsibilities.

## How to trust the recommendations

The system is deterministic and explainable:

- ROI assumptions live in `config/scoring_rules.yml`.
- Scoring weights live in `config/scoring_rules.yml`.
- Risk tolerance and sensitive data categories live in `config/company_profile.yml`.
- Each decision includes a recommendation, reason, risks, suggested owner, next step, and confidence.
- The base workflow does not call an LLM or send data to external tools.

Default ROI assumptions include:

- Blended hourly cost
- Setup cost for low, medium, and high complexity workflows
- Monthly maintenance cost percent
- Automation coverage by complexity
- Normalization thresholds for time saved, frequency, and error rate

## Example founder workflow

- Friday: list workflows causing drag.
- Monday: run the system.
- Tuesday: review quick wins.
- Wednesday: assign AI pilots.
- Thursday: review risks and human approval rules.
- Friday: update the weekly operating review.

## Customization guide

Customize `config/company_profile.yml` to change:

- Risk tolerance
- Sensitive data categories
- Functions to prioritize
- Functions to avoid for now
- Founder operating goals
- Preferred tools

Customize `config/scoring_rules.yml` to change:

- Hourly cost assumptions
- Scoring weights
- Normalization thresholds
- Automation cost assumptions
- Automation coverage by complexity
- Score bands
- Decision notes

Customize the code if you need deeper changes to:

- Workflow functions
- Decision logic
- Backlog generation
- Policy language
- Reporting format

## Why this matters

This is not an AI demo. It is a decision system for founders trying to use AI without wasting time, creating risk, or automating the wrong work.

## Roadmap

- Google Sheets export
- Notion export
- Streamlit dashboard
- AI-assisted workflow mapping
- Zapier and Make.com automation templates
- Slack workflow intake
- Linear and Jira backlog sync
- ROI tracking over time
- AI tool registry

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License. See [LICENSE](LICENSE).

## Built by

Built by Shubham Singh, a founder-facing operator focused on RevOps, GTM systems, startup metrics, and AI workflows for early-stage teams.

## Use this in your company

Fork it when AI work is being chosen by instinct, hype, or tool demos. Replace `data/sample_workflows.csv`, edit `config/company_profile.yml`, run `make run`, and start with `outputs/founder_ai_roi_memo.md`. Keep private workflow, customer, employee, finance, and vendor data out of public forks.

## If you are a Founder's Office candidate

Use this repo to show operator judgment around AI adoption: workflow triage, risk control, ROI math, human approval, and knowing when the right answer is hiring or documentation instead of automation.
