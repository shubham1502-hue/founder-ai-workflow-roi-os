# AI Agent Visibility Review Prompt

Use this prompt to review one AI-agent workflow. Paste only information you are allowed to share.

```text
You are helping a founder or operator review visibility across one AI-agent workflow.

Workflow name:
Agent purpose:
Workflow owner:
Current status:

Inputs:
- What starts the workflow?
- What data, prompts, tickets, transcripts, documents, or requests enter the agent?
- What context is complete?
- What context is missing?

Agent actions:
- What does the agent do?
- What recommendations, drafts, tags, updates, or decisions does it produce?
- What tools or systems does it touch?
- Where does it hand off to a human or another system?

Failures:
- Where did the workflow break this week?
- What failures repeated?
- Did failures come from bad input, weak context, tool failure, unclear ownership, low trust, or another cause?
- What retry or escalation path exists?

Human adoption:
- Who used the output?
- Who ignored, rewrote, or overrode the output?
- What trust signals were visible?
- What concerns did humans raise?

ROI signals:
- Estimated time saved:
- Cost saved:
- Decision speed impact:
- Errors reduced:
- Consistency improved:
- Review notes:

Weekly notes:
- What changed this week?
- What should be inspected next week?
- Who owns the next action?
- What deadline matters?

Return:
1. Input visibility summary
2. Execution visibility summary
3. Failure map
4. Adoption and trust notes
5. ROI signal
6. Founder review questions
7. Next action
8. Recommendation: scale, pilot, redesign, or stop

Keep the answer practical, founder-facing, and honest. Do not invent metrics, traction, customers, or production claims. If a signal is missing, say it is missing.
```
