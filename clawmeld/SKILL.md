---
name: clawmeld
description: "Manage and process thoughts captured by the ClawMeld iOS app. Use when the user wants to: (1) Process a recently captured thought, (2) inspect capture artifacts in Google Docs or Notion, (3) configure the ClawMeld integration, or (4) route a capture into the AutoResearch backend flow."
---

# ClawMeld Skill

This skill helps you integrate and process thoughts from the **ClawMeld** iOS app.

## Workflow

1. **Capture**: The user captures a thought on their iPhone using ClawMeld.
2. **Dispatch**: The app saves the thought to Google Docs, Notion, or the OpenClaw Gateway.
3. **Process**: You (the agent) use this skill to find the latest captures, route research work to `clawmeld-autoresearch` when appropriate, and integrate the result into user-facing artifacts or memory.

## Tools & Commands

### Process Latest Thought
Use the `process_thought.py` script only for legacy plain-text capture files. For the current Google Docs flow, prefer reading the capture contract from the saved artifact metadata and routing research work through `clawmeld-autoresearch`.

### Configuration
ClawMeld is configured in the app's Settings.
- **Gateway URL**: Your OpenClaw Gateway URL.
- **API Key**: Your Gateway Token.
- **Agent ID**: Usually `main` or `ios-expert`.
- **Direct-save provider**: Exactly one provider at a time, typically Google Docs first.

## Implementation Details

Current Google-first behavior:
- capture artifacts are created as Google Docs inside `ClawMeld/Captures`
- research artifacts should be created as Google Docs inside `ClawMeld/Research`
- the backend should preserve links between source capture docs and research result docs

Legacy behavior:
- older flows may still use text files or gateway-only captures

### Processing Pattern
When processing a thought:
1. Extract the captured thought, context, media details, and metadata.
2. Determine whether this is plain capture handling or an AutoResearch candidate.
3. If research is needed, switch to `clawmeld-autoresearch` and follow its output contract.
4. If no research is needed, determine if it is a **Todo**, **Fact**, **Decision**, or **Idea**.
5. Update the appropriate memory file or user-facing artifact.
