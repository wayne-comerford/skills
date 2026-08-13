# assayer

> **You can't mark your own homework — so this gets someone else to.**

You just built something and it looks fine to you. It looks fine *because* you built it: every choice in there is one you already decided was reasonable. That isn't a character flaw, it's how building works — and it's why you can't proofread your own writing either.

Assayer hands the finished thing to a fresh agent that never saw your reasoning, and has it **open the thing and use it** — click it, run it, measure it, at every screen size — rather than read the diff and agree with you. Before that, it makes you write down what "good" means here, in terms someone else could check.

That's the whole method: **anchor, build, prove.**

## What it found on its first two real runs

| | |
| --- | --- |
| **2.72:1** | Four call-to-action buttons at barely half the legally required contrast |
| **0×0** | The main food photograph rendering at zero pixels on mobile |
| **11,000ms** | A hero image taking eleven seconds to paint on a phone connection |
| **1.01:1** | Focus rings invisible against the photograph behind them |

All four were missed by the person who built them, who had already declared the work clean. That person was Claude, working without this skill.

## Install

```bash
ln -s "$PWD/assayer" ~/.claude/skills/assayer
```

Then just work. It loads itself when quality is the constraint. Or type `/assayer`.

**Say "keep it light" and it stops.** A typo fix gets the same three steps in about ten seconds — not eight agents. It announces which weight it picked before spending anything, so you can push back early.

## What's in here

| Path | What it is |
| --- | --- |
| `SKILL.md` | The method. Written for the model, not for you — the pitch is this file |
| `references/distinctiveness.md` | How to beat a reference rather than match it, and why matching produces the category average |
| `references/critique-rubrics.md` | What to measure and how, across nine domains — 3D, web UI, APIs, docs, CLIs, data, reports, performance |
| `references/agent-prompts.md` | Prompts for the builder, critic, blind judge and integration roles |
| `scripts/blind_compare.py` | Builds a shuffled side-by-side and writes the answer key outside the judge's directory. No dependencies |
| `evidence/` | The controls behind the rules, kept whole rather than summarised |

## Where it doesn't help

Anything with no checkable standard. *"Write me something creative"* has nothing to measure against, so it's ordinary work with extra ceremony.

## Known limits

**The checker is also an AI, and it shares the builder's taste.** Separation defeats self-review bias — it does nothing about shared priors. Across two independent passes on real work, the checkers found every measurable defect and not one aesthetic one. Those were all caught by the human reading the page.

**Two rules are RED/GREEN tested; the rest are grounded in observed failures but not verified to change behaviour.** The distinction is recorded in `evidence/` rather than smoothed over.

MIT.
