#!/usr/bin/env python3
"""Read-only sanity checks for a couple memory book project."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_STATE_KEYS = {
    "schema_version", "project", "sources", "consent", "story_facts",
    "open_questions", "page_plan", "style_variants", "runs", "outputs",
    "qa", "next_actions",
}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python scripts/validate_project.py <project-root>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).resolve()
    if not root.is_dir():
        print(f"ERROR: project root does not exist: {root}", file=sys.stderr)
        return 2
    state_path = root / "project-state.json"
    if not state_path.exists():
        print(f"ERROR: missing {state_path}", file=sys.stderr)
        return 1
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read project state: {exc}", file=sys.stderr)
        return 1
    missing = sorted(REQUIRED_STATE_KEYS - set(state))
    if missing:
        print("ERROR: missing state keys: " + ", ".join(missing), file=sys.stderr)
        return 1
    errors = []
    for index, source in enumerate(state["sources"]):
        if not isinstance(source, dict) or "path" not in source:
            errors.append(f"sources[{index}] must contain path")
            continue
        if not (root / source["path"]).exists():
            errors.append(f"missing source: {source['path']}")
    for index, output in enumerate(state["outputs"]):
        if not isinstance(output, dict) or "path" not in output:
            errors.append(f"outputs[{index}] must contain path")
            continue
        if not (root / output["path"]).exists():
            errors.append(f"missing output: {output['path']}")
    if errors:
        for error in errors:
            print("ERROR: " + error, file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "ok",
        "project": state["project"],
        "sources": len(state["sources"]),
        "outputs": len(state["outputs"]),
        "qa_status": state["qa"].get("status"),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
