## Advanced Analytica Governance Principles

### Repo Naming Protocol

Every Advanced Analytica repository MUST follow this naming pattern:

```text
{client-prefix}-{product-or-domain}-{function}
```

Rules:

- Use lowercase letters only.
- Separate words with hyphens only; underscores are not allowed.
- `{client-prefix}` is a short client identifier such as `pwc`, `disney`, or `aa` for internal work.
- `{product-or-domain}` is the product line or domain area such as `brand-oracle`, `disambiguation`, `risko`, or `adverse-news`.
- `{function}` identifies what the repository does, such as `pipeline`, `mcp`, `spec`, or `frontend`.
- Internal tooling that is not client-specific uses the `aa-` prefix.
- The naming workflow MUST run before `specify init` so the repository name is validated before project scaffolding begins.

Jonny must replace the example client prefixes and product/domain vocabulary above with the production-approved list once it is finalized.

### Repo Labelling Taxonomy

Every Advanced Analytica repository MUST carry a standard GitHub label set after task generation is complete. Labels use `dimension:value` format across these dimensions:

- Domain: `domain:brand-governance`, `domain:risk-intelligence`, `domain:disambiguation`, `domain:adverse-news`
- Client: `client:pwc`, `client:disney`, `client:internal`
- Product: `product:brand-oracle`, `product:risko`, `product:atomiser`, `product:signal-harvester`
- Status: `status:speccing`, `status:building`, `status:testing`, `status:deployed`, `status:paused`

Rules:

- Every repository gets at least one `Domain`, one `Client`, and one `Status` label.
- `Product` labels are optional when the repository does not map to a named product.
- Labels are proposed after `spec.md`, `plan.md`, and `tasks.md` exist so classification is based on evidence rather than guesswork.
- Proposed labels MUST be reviewed before they are applied to GitHub.

Jonny must replace the example taxonomy values above with the production-approved label set once it is finalized.
