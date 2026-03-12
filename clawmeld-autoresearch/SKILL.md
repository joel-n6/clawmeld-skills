---
name: clawmeld-autoresearch
description: Turn ClawMeld captures into structured research outputs such as research briefs, market validation notes, competitor scans, technical deep-dives, and decision memos. Use when a captured thought should trigger real research instead of plain storage, when defining AutoResearch product behavior, when implementing gateway prompts and output contracts, or when evaluating whether a user idea deserves external fact-finding and cited sources.
---

# ClawMeld AutoResearch

Convert a captured thought into a decision-ready artifact.

## Workflow

1. Read the capture and normalize it using `references/output-contract.md`.
2. Decide whether the request needs:
   - synthesis only
   - lightweight web research
   - deeper market/technical research
3. Use `references/when-to-research-vs-summarize.md` to choose the depth.
4. Produce one output mode:
   - research brief
   - market validation
   - competitor scan
   - technical deep-dive
   - decision memo
5. Evaluate quality against `references/research-rubric.md`.
6. Use the matching template in `assets/templates/` when structure helps.

## Rules

- Start by inferring the actual decision behind the note.
- Do not inflate weak captures into long essays.
- If the thought is vague, sharpen it into explicit questions before researching.
- Prefer concise, decision-oriented outputs.
- Cite sources when external facts materially affect the recommendation.
- Separate facts, assumptions, and speculation.
- End with recommended next steps.

## Capture inputs to consider

Use these when present:
- transcribed thought
- OCR text
- current media context
- location / activity metadata
- timestamp

Treat metadata as context, not as the goal.

## Default output structure

1. Core question
2. Why it matters
3. Findings
4. Risks / unknowns
5. Recommendation
6. Next actions
7. Sources

## Product guidance

AutoResearch should feel like:
- a fast research copilot for captured thoughts
- useful within minutes
- more concrete than a summary
- less bloated than a full report

Do not make it feel like generic chatbot filler.

## Resources

- Output contract: `references/output-contract.md`
- Quality rubric: `references/research-rubric.md`
- Research depth decision: `references/when-to-research-vs-summarize.md`
- Templates: `assets/templates/research-brief.md`, `assets/templates/decision-memo.md`
