# AI Agent Workflow Visibility Example

Company: SignalDesk AI
Stage: Seed
Workflow: Sales call follow-up agent
Context: The team uses an AI agent to summarize sales calls, tag objections, draft follow-ups, and update CRM fields.

This is a synthetic example. It does not describe a real company, customer, or production workflow.

## Workflow snapshot

| Field | Entry |
| --- | --- |
| Workflow owner | Founder / RevOps |
| Current status | Pilot |
| Human review required | Yes |
| Main operating question | Does the agent make follow-up faster without lowering quality or trust? |

## Input layer

| Signal | Finding |
| --- | --- |
| Input trigger | Sales call transcript added after a prospect call |
| Input quality | Transcript is complete, but CRM fields are often missing |
| Context gaps | Deal stage, persona, pain point, and recent activity are not always attached |
| Founder question | Is the agent receiving enough context to draft a useful next step? |

## Execution layer

| Signal | Finding |
| --- | --- |
| Agent actions | Summarizes the call, tags objections, drafts a follow-up, suggests CRM updates |
| Tools touched | CRM record, Gmail draft, Slack alert |
| Handoffs | Founder reviews the draft before sending |
| Founder question | Is the agent doing the right work, or is it creating another review queue? |

## Failure layer

| Signal | Finding |
| --- | --- |
| Common failure mode | Weak next step when CRM context is thin |
| Repeated issue | Urgency is overstated when budget is mentioned without timing |
| Escalation path | Send unclear follow-ups to the RevOps owner before founder review |
| Founder question | Is the failure caused by agent quality, missing input, or unclear workflow ownership? |

## Adoption layer

| Signal | Finding |
| --- | --- |
| Usage | Founder reads most summaries |
| Overrides | Founder edits around 20 percent of follow-up drafts |
| Trust level | Medium |
| Trust note | Summaries are trusted more than urgency tags |
| Founder question | Are humans using the output because it is useful, or because review is required? |

## ROI layer

| Signal | Finding |
| --- | --- |
| Time saved | Around 3 hours per week |
| Decision speed | Same-day follow-up is more consistent |
| Error reduction | Fewer missed CRM updates |
| ROI signal | Strong enough to continue the pilot, but not strong enough to scale without better CRM context |

## Weekly review layer

Review these items every week:

- Which recommendations were ignored?
- Which follow-up drafts required heavy edits?
- Which CRM fields were missing before the agent ran?
- Which urgency tags were wrong?
- Did the workflow save time after human review time was included?
- Should human review remain required?

## Founder memo

Workflow: Sales call follow-up agent
Owner: Founder / RevOps
Current status: Pilot

Input signal: Transcript quality is good, but CRM context is incomplete.
Execution signal: The agent handles summaries and draft follow-ups, then hands off to the founder.
Failure signal: Weak next steps appear when deal stage, persona, or recent activity is missing.
Adoption signal: Founder uses the summaries and edits a minority of drafts. Trust is medium.
ROI signal: The workflow saves about 3 hours per week and improves same-day follow-up.
Founder review question: Which recommendations were ignored, and did missing CRM context cause the miss?
Next action: Keep piloting with stronger CRM context and required human review.
Owner: RevOps owner
Due date: Friday

## Decision

Decision options:

- Scale
- Keep piloting
- Add human review
- Redesign workflow
- Stop workflow

Chosen decision:

Keep piloting with stronger CRM context and required human review.
