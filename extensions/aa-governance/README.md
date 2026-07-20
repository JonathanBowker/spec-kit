# Advanced Analytica Governance Extension

This bundled extension adds two governance commands for the Advanced Analytica fork:

- `speckit.aa-governance.name-repo`
- `speckit.aa-governance.label-repo`

It is designed to keep AA-specific policy in separate files so upstream Spec Kit merges stay low-friction.

## What It Does

### `speckit.aa-governance.name-repo`

Validates or proposes a repository name using the AA pattern:

```text
{client-prefix}-{product-or-domain}-{function}
```

Use this before `specify init`. The command is intentionally manual because Spec Kit does not register project extension commands until a project exists.

### `speckit.aa-governance.label-repo`

Reads `spec.md`, `plan.md`, and `tasks.md`, proposes GitHub labels from the AA taxonomy, asks for confirmation, and then either:

- applies labels via `gh` if the GitHub CLI is available and the repo remote resolves cleanly, or
- prints the exact label set and follow-up commands if automated application is not possible

The extension also registers an optional `after_tasks` hook so the labelling review appears at the end of step three.

## Install

```bash
specify extension add aa-governance
```

Optional configuration lives at `.specify/extensions/aa-governance/aa-governance-config.yml`.

## Suggested AA Flow

1. Run the naming command before `specify init`.
2. Run `specify init ...`.
3. Install the AA governance preset so `constitution.md` carries the fork policy.
4. Install this extension so label proposals are offered after task generation.

## Fork Maintenance

The fork should keep these remotes:

```bash
git remote add upstream https://github.com/spec-kit/spec-kit.git
git remote set-url --push upstream DISABLE
```

Recommended update cycle:

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

After each upstream merge, run `specify check` and fix any inconsistencies at the source artifact level.
