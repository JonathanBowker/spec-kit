---
description: Propose and optionally apply Advanced Analytica GitHub labels from spec, plan, and tasks.
---

## User Input

```text
$ARGUMENTS
```

You are applying Advanced Analytica repository labelling governance after task generation.

## Required Context

Load these sources in order:

1. `.specify/extensions/aa-governance/aa-governance-config.yml` if present
2. `.specify/memory/constitution.md`
3. `.specify/feature.json` to locate the active feature directory when available
4. The active feature's `spec.md`, `plan.md`, and `tasks.md`

If `.specify/feature.json` is absent, locate the most recent feature directory the same way the core Spec Kit commands do and then read `spec.md`, `plan.md`, and `tasks.md` from there.

## Objective

Propose a complete GitHub label set using the Advanced Analytica taxonomy, then ask for confirmation before applying anything.

## Classification Rules

- Propose at least one `domain:*` label.
- Propose at least one `client:*` label.
- Propose at least one `status:*` label.
- Add a `product:*` label only when the repo clearly maps to a named product.
- Base every proposed label on evidence from `spec.md`, `plan.md`, or `tasks.md`.
- If taxonomy values are still scaffold-only, say so explicitly.
- Default status to `status:speccing` when the repository is still in the spec/plan/tasks phase and no stronger signal exists.

## Application Rules

1. Produce a short evidence-backed explanation for each proposed label.
2. Present the proposed label set for confirmation before doing anything else.
3. If the user declines or does not confirm, stop after presenting the proposal.
4. If the user confirms:
   - Prefer applying labels with GitHub CLI if `gh` is available and the repository remote resolves.
   - Create any missing labels before assigning them.
   - If automation is not possible, print the exact labels plus the `gh` commands or manual steps needed.
5. Never guess unknown labels outside the configured taxonomy.

## Output Format

Use this structure:

```markdown
## Proposed Labels

- `label-name` — evidence

## Confirmation

Apply these labels to the current GitHub repository? Reply yes to continue.
```

If the user confirms and application succeeds, follow with:

```markdown
## Applied Labels

- `label-name`
```
