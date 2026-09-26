# Output and QA Contract

Before handoff, confirm the requested output type and record evidence in `project-state.json`.

## Image set

- Every page has a stable filename and expected dimensions.
- Cover, clean scene art, and typeset variant are distinguishable.
- No accidental model-generated text, duplicate dates, watermarks, or unrelated people.
- Character identity, relative height, clothing continuity, and emotional tone are consistent for the selected style.

## PDF

- Page count matches the page plan.
- Page size and orientation match the request.
- All pages render successfully to PNG previews.
- Text is inside safe margins with sufficient contrast.
- Titles, dates, page numbers, and body text are legible at normal viewing size.
- Source assets and final PDF remain separately recoverable.

## Handoff record

Record:

```json
{
  "status": "complete",
  "output_paths": ["output/book.pdf"],
  "page_count": 8,
  "dimensions": "A4 portrait",
  "qa": {"status": "passed", "checks": ["rendered_all_pages", "no_clipped_text", "cover_verified"]},
  "remaining_risk": [],
  "next_actions": ["optional: create retro-scrapbook variant"]
}
```
