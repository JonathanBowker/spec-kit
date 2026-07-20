---
description: Validate or propose an Advanced Analytica repository name before running specify init.
---

## User Input

```text
$ARGUMENTS
```

You are validating or proposing a repository name for Advanced Analytica.

## Required Context

Load these sources if they exist:

1. `.specify/extensions/aa-governance/aa-governance-config.yml`
2. `.specify/memory/constitution.md`
3. `AGENTS.md`

Prefer the extension config for concrete vocabulary. If it is missing, fall back to the constitution. If neither source provides finalized values, use the scaffold values and clearly say they are placeholders.

## Goal

Return a single validated repository name string that matches:

```text
{client-prefix}-{product-or-domain}-{function}
```

## Rules

- Lowercase only.
- Hyphens only; no underscores or spaces.
- The first segment is the client prefix.
- The second segment is the product or domain.
- The third segment is the repo function.
- Internal repositories should use the internal prefix from config, or `aa` if no config exists.

## Behaviour

1. If the user provided a repository name:
   - Validate it against the pattern and the configured vocabulary.
   - If it is valid, return it and explain why it passes.
   - If it is invalid, return a corrected proposal and explain the mismatch briefly.
2. If the user did not provide a repository name:
   - Ask only for the minimum missing inputs needed to produce one: client, product/domain, and function.
   - If enough context is already available, do not ask questions; propose the name directly.
3. If the vocabulary is still scaffold-only:
   - State that the proposal is structurally valid but still uses placeholder taxonomy until Jonny finalizes the production list.
4. Remind the user that GitHub repository renames are generally safe because GitHub redirects old URLs, but local remotes and hardcoded CI or docs references may still need updates.

## Output Format

Use this exact structure:

```text
Validated name: <repo-name>
Reason: <one short paragraph>
```
