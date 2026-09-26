# Project State Contract

Keep one UTF-8 `project-state.json` at the project root. Use project-relative paths in the portable state file.

```json
{
  "schema_version": "1.0",
  "project": {"title": "Example memory book", "subtitle": "A story told in pages", "status": "in_progress", "updated_at": "2026-09-26T00:00:00+08:00"},
  "sources": [{"path": "materials/story.md", "kind": "facts", "status": "read"}],
  "consent": {"photo_upload": "authorized|not_authorized|needs_confirmation", "destinations": [], "files": []},
  "story_facts": [], "open_questions": [], "page_plan": [], "style_variants": [], "accepted_baseline": null, "runs": [], "outputs": [],
  "qa": {"status": "not_run", "checks": []}, "next_actions": []
}
```

## Status values

- `planned`: inputs are known but production has not started.
- `in_progress`: a generation or layout run is active.
- `needs_user_choice`: a material choice is unresolved.
- `blocked`: a required file, authorization, provider, or dependency is unavailable.
- `complete`: requested outputs exist and final QA passes.

## Update rules

- Append a new run record instead of rewriting history.
- Keep `accepted_baseline` pointing to the exact style test and scene set used by later variants.
- Use stable page IDs such as `p01-cover` and stable scene IDs in manifests.
- Keep failures and skipped items visible.
- After each meaningful decision, update `updated_at`, `next_actions`, and the relevant status.
