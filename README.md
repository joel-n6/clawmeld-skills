# ClawMeld Skills

Custom OpenClaw skills for the ClawMeld ecosystem.

These skills support ClawMeld's core workflows around capture processing, structured research, and revenue-focused product decision-making.

## Included skills

### `clawmeld`
Manage and process thoughts captured by the ClawMeld iOS app.

Use this skill when you want to:
- process a newly captured thought
- inspect capture artifacts in Google Docs or Notion
- configure the ClawMeld integration
- route a capture into the AutoResearch backend flow

### `clawmeld-autoresearch`
Turn ClawMeld captures into decision-ready research outputs.

Use this skill for:
- research briefs
- market validation notes
- competitor scans
- technical deep-dives
- decision memos

Core behavior:
- sharpens vague notes into explicit questions
- chooses the right research depth
- separates facts, assumptions, and speculation
- ends with recommendations and next actions

### `clawmeld-growth`
Evaluate ClawMeld and adjacent product ideas for revenue potential.

Use this skill when deciding:
- what to build next
- which ICP to target
- how to price or position a feature
- whether a feature supports a realistic path to $10k/month
- whether to ship, test, reframe, defer, or kill an idea

## Repository structure

```text
clawmeld/
  SKILL.md
clawmeld-autoresearch/
  SKILL.md
clawmeld-growth/
  SKILL.md
```

## Install

Clone or copy this repository into a location where your OpenClaw setup can access custom skills.

Typical local workflow:

```bash
git clone https://github.com/joel-n6/clawmeld-skills.git
```

Then install or symlink the desired skill folders into your OpenClaw skills directory according to your local setup.

## Intended use

These skills are designed to work together:
1. **Capture** a thought in ClawMeld
2. **Route** it through `clawmeld`
3. **Escalate** to `clawmeld-autoresearch` when deeper analysis is warranted
4. **Evaluate** commercial potential with `clawmeld-growth` when deciding what to build or sell

## Notes

- This repo focuses on skill definitions and workflow guidance.
- Supporting assets/references may live alongside skills in future revisions.
- ClawMeld is the product context; OpenClaw is the agent runtime.
