#!/usr/bin/env python3
"""Build a blind side-by-side comparison between our artifact and a reference.

Randomizes which side becomes A and which becomes B, copies both under neutral
names, and writes the answer key OUTSIDE the directory the judge is given. The
point is that nothing in the judge's context — filename, ordering, path, or
metadata — reveals which artifact is under development, because every one of
those cues leaks and produces an agreeable judge instead of an honest one.

Requires a matched capture of the reference, so it only applies at fidelity
T1/T2 (see SKILL.md). If you only have descriptions of the exemplar there is
nothing to put on the other side and this is the wrong tool — use the spec
gate instead. The one exception is a self-blind run, comparing this round
against the last to detect regression and flat rounds:

    # true blind gate (T1/T2)
    python blind_compare.py --ours build/shot.png --reference .assay/reference/linear.png --out .assay/gate/density

    # multiple matched views — order defines the pairing, so capture them the same way
    python blind_compare.py --ours empty.png list.png error.png \\
                            --reference ref/empty.png ref/list.png ref/error.png \\
                            --out .assay/gate/states --views empty populated error

    # self-blind: this round against last round (works at any fidelity)
    python blind_compare.py --ours r3.png --reference r2.png --out .assay/gate/r3-vs-r2 --self-blind

Produces:
    <out>/compare/          <- hand this path to the judge, and nothing else
        artifact_A_1.<ext>, artifact_B_1.<ext>, ...
        index.html          <- side-by-side viewer
    <out>/KEY.json          <- keep out of the judge's context
"""

import argparse
import base64
import json
import mimetypes
import random
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif", ".bmp"}
TEXT_SUFFIXES = {
    ".txt", ".md", ".json", ".csv", ".tsv", ".log", ".yaml", ".yml",
    ".py", ".js", ".ts", ".tsx", ".jsx", ".css", ".sh", ".rs", ".go", ".java",
}


def classify(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in IMAGE_SUFFIXES:
        return "image"
    if suffix == ".svg":
        return "svg"
    if suffix in {".html", ".htm"}:
        return "html"
    if suffix in TEXT_SUFFIXES:
        return "text"
    # Unknown extension: sniff for binary, fall back to text so odd but readable
    # formats still render rather than failing the gate on a technicality.
    try:
        with path.open("rb") as handle:
            if b"\0" in handle.read(8192):
                return "binary"
    except OSError:
        return "binary"
    return "text"


def render_panel(label: str, path: Path, kind: str) -> str:
    """Inline each side so the HTML is self-contained and survives being moved."""
    if kind == "image":
        mime = mimetypes.guess_type(path.name)[0] or "image/png"
        data = base64.b64encode(path.read_bytes()).decode("ascii")
        body = f'<img src="data:{mime};base64,{data}" alt="Artifact {label}">'
    elif kind == "svg":
        body = f'<div class="svg-wrap">{path.read_text(encoding="utf-8", errors="replace")}</div>'
    elif kind == "html":
        raw = path.read_text(encoding="utf-8", errors="replace")
        data = base64.b64encode(raw.encode("utf-8")).decode("ascii")
        body = f'<iframe src="data:text/html;base64,{data}" title="Artifact {label}"></iframe>'
    elif kind == "text":
        text = path.read_text(encoding="utf-8", errors="replace")
        escaped = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        body = f"<pre>{escaped}</pre>"
    else:
        body = f'<p class="note">Binary artifact — inspect <code>{path.name}</code> directly.</p>'
    return f'<section class="panel"><h2>Artifact {label}</h2>{body}</section>'


PAGE = """<!doctype html>
<meta charset="utf-8">
<title>Blind comparison</title>
<style>
  :root {{ color-scheme: light dark; --line: #8883; }}
  body {{ margin: 0; font: 15px/1.5 system-ui, -apple-system, sans-serif; }}
  header {{ padding: 12px 20px; border-bottom: 1px solid var(--line); }}
  header h1 {{ font-size: 15px; margin: 0; font-weight: 600; }}
  header p {{ margin: 4px 0 0; opacity: .65; font-size: 13px; }}
  .view-label {{ padding: 14px 20px 0; font-size: 12px; text-transform: uppercase;
                 letter-spacing: .08em; opacity: .5; }}
  .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: var(--line);
           margin-top: 8px; }}
  @media (max-width: 800px) {{ .grid {{ grid-template-columns: 1fr; }} }}
  .panel {{ background: Canvas; padding: 16px; min-width: 0; }}
  .panel h2 {{ font-size: 12px; text-transform: uppercase; letter-spacing: .08em;
               opacity: .6; margin: 0 0 12px; }}
  img {{ max-width: 100%; height: auto; display: block; }}
  .svg-wrap svg {{ max-width: 100%; height: auto; }}
  iframe {{ width: 100%; height: 70vh; border: 1px solid var(--line); background: #fff; }}
  pre {{ margin: 0; overflow-x: auto; font-size: 13px; white-space: pre-wrap;
         word-break: break-word; }}
  .note {{ opacity: .6; }}
</style>
<header>
  <h1>Blind comparison &mdash; {dimension}</h1>
  <p>Two independently produced artifacts. Judge which is better against the rubric.</p>
</header>
{sections}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ours", required=True, nargs="+", help="Our artifact(s)")
    parser.add_argument("--reference", required=True, nargs="+",
                        help="The other side: the exemplar's matched capture(s), or a "
                             "previous round when using --self-blind")
    parser.add_argument("--out", required=True, help="Output directory")
    parser.add_argument("--dimension", default="overall quality",
                        help="What this comparison is testing, shown in the viewer")
    parser.add_argument("--views", nargs="*", default=None,
                        help="Optional labels per view, e.g. --views empty loading error")
    parser.add_argument("--self-blind", action="store_true",
                        help="Comparing two of our own rounds rather than against the "
                             "exemplar. Detects regression and flat rounds; does not "
                             "demonstrate parity with the exemplar.")
    parser.add_argument("--seed", type=int, default=None,
                        help="Seed the shuffle for a reproducible assignment")
    args = parser.parse_args()

    ours = [Path(p) for p in args.ours]
    reference = [Path(p) for p in args.reference]
    for path in ours + reference:
        if not path.is_file():
            print(f"error: not a file: {path}", file=sys.stderr)
            return 1

    if len(ours) != len(reference):
        print(f"error: {len(ours)} ours vs {len(reference)} reference — views are paired "
              "by position, so both sides need the same count", file=sys.stderr)
        return 1

    for a, b in zip(ours, reference):
        if a.suffix.lower() != b.suffix.lower():
            print(f"warning: differing formats ({a.name} vs {b.name}) — format alone "
                  "can tip the judge", file=sys.stderr)

    # One shuffle for the whole comparison, not per view: if A were ours on some
    # views and theirs on others, a judge noticing the inconsistency learns which
    # side is which, and per-view winners stop aggregating into a verdict.
    rng = random.Random(args.seed)
    ours_is_a = rng.random() < 0.5

    out = Path(args.out)
    compare = out / "compare"
    compare.mkdir(parents=True, exist_ok=True)

    sections = []
    for index, (our_view, ref_view) in enumerate(zip(ours, reference), start=1):
        assignment = ({"A": our_view, "B": ref_view} if ours_is_a
                      else {"A": ref_view, "B": our_view})
        panels = []
        for label in ("A", "B"):
            source = assignment[label]
            dest = compare / f"artifact_{label}_{index}{source.suffix.lower()}"
            shutil.copy2(source, dest)
            panels.append(render_panel(label, dest, classify(dest)))
        if args.views and index <= len(args.views):
            sections.append(f'<p class="view-label">{args.views[index - 1]}</p>')
        elif len(ours) > 1:
            sections.append(f'<p class="view-label">View {index}</p>')
        sections.append(f'<div class="grid">{"".join(panels)}</div>')

    (compare / "index.html").write_text(
        PAGE.format(dimension=args.dimension, sections="".join(sections)), encoding="utf-8"
    )

    (out / "KEY.json").write_text(json.dumps({
        "dimension": args.dimension,
        "mode": "self-blind" if args.self_blind else "vs-exemplar",
        "created": datetime.now(timezone.utc).isoformat(),
        "A": "ours" if ours_is_a else "reference",
        "B": "reference" if ours_is_a else "ours",
        "views": len(ours),
        "ours_paths": [str(p) for p in ours],
        "reference_paths": [str(p) for p in reference],
    }, indent=2) + "\n", encoding="utf-8")

    print(f"Judge sees: {compare}  ({len(ours)} view(s))")
    print(f"Key (keep out of the judge's context): {out / 'KEY.json'}")
    if args.self_blind:
        print("Mode: self-blind — detects regression between rounds; does not show "
              "parity with the exemplar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())