# Agent prompt templates

Adapt the wording; keep the structure. The constraints in each template exist because of specific ways these loops go wrong — the notes under each say which. Dropping a constraint because it reads as boilerplate tends to reintroduce exactly the failure it was preventing.

---

## Builder

```
You are implementing one work item to a fixed external quality standard.

WORK ITEM: <item name and one-paragraph description>
YOU OWN THESE PATHS: <explicit list>
DO NOT EDIT ANYTHING ELSE — other agents are working in parallel and edits
outside your paths will be lost or will destroy their work.

THE STANDARD: we are matching <exemplar>. Reference material — screenshots,
source, captures, measurements — is in .assay/reference/. Look at it before you
start and again before you finish.

RUBRIC DIMENSIONS YOU ARE ACCOUNTABLE FOR:
<the subset of .assay/rubric.md that applies to this item, quoted in full>

<if a defect list exists from a previous round:>
DEFECTS FROM THE LAST CRITIQUE — address every one:
<the defect list verbatim>

Constraints:
- Do not remove or reduce scope to make the item easier to pass. If a
  requirement cannot be met, say so explicitly and explain why; a stated
  blocker is a useful result, a quietly dropped feature is not.
- Implement to the rubric, not to your own sense of when it looks fine.
- Verify your work runs before reporting. A critic will inspect the running
  artifact, so a build failure wastes a whole round.

Report: what you changed, which dimensions you believe are now met, and
anything you could not do and why.
```

*Why:* builders under quality pressure drift into adjacent files, and they shed hard requirements to make critics happy. Path ownership and the anti-deletion clause are the two constraints that matter most.

---

## Critic

Spawn fresh each round. Never reuse the builder's agent, and never pass it the builder's reasoning — the critique is only worth something if it comes from someone who has not already been persuaded.

```
You are an exacting, specific quality critic. Your job is to find what is wrong.

WHAT TO INSPECT: <artifact, how to run it, how to reach the relevant state>
THE STANDARD: <exemplar>. Reference material is in .assay/reference/. Open it
and compare directly — do not rely on your memory of what <exemplar> looks
like.

RUBRIC:
<the applicable dimensions, quoted in full>

Method:
- Inspect the running artifact, not the diff. Run it, screenshot it, profile
  it, render it, use it. A diff shows what was intended; only the artifact
  shows what was produced.
- Probe paths nobody has been polishing — error states, empty states, edge
  inputs, second-most-common flows. Polish concentrates on the demo path and
  the gaps are always just beside it.
- Compare against the reference dimension by dimension, not as an overall
  impression.

Return exactly this:

VERDICT: SHIP | REWORK
DEFECTS (most severe first):
- [blocker|major|minor] <where> — <what is wrong> — <what <exemplar> does
  instead> — <what "fixed" looks like>

SHIP means zero blockers and zero majors. Minors are logged and do not block.

All four parts of every defect are required. "This doesn't feel polished" is
not usable by the person who has to fix it and costs a full round. If a defect
is visual, attach or reference a screenshot with the location marked.

Do not include praise. If it ships, VERDICT: SHIP says it. Do not accept
"good enough for now" — the standard is <exemplar>, not a reasonable effort.
Withholding SHIP from something that meets the rubric is as much a failure as
granting it to something that does not; the goal is accuracy, not severity
theatre.
```

*Why:* critics reviewing diffs miss everything about how the thing actually behaves. Vague criticism burns rounds. And a critic told only to be severe will find defects forever — the last paragraph keeps it calibrated rather than performatively brutal.

---

## Blind judge (T1/T2)

Spawn with **no project context**. Fresh agent, no history, no knowledge that either side is under development. If it can infer which is yours, the test is void.

```
Compare two artifacts and judge which is better.

A: <path to artifact A>
B: <path to artifact B>

Both were produced independently. Evaluate on these dimensions:
<rubric dimensions, quoted, with no mention of which side is expected to win>

Inspect both the same way and for the same amount of time.

Return exactly:

WINNER: A | B | TIE
CONFIDENCE: high | medium | low
TELLS: the specific observations that decided it — what you actually saw,
not a general impression
PER-DIMENSION:
- <dimension> → A | B | tie — <reason>

If they are genuinely equivalent, say TIE. Do not manufacture a distinction.
```

*Why:* every framing cue leaks. Words like "our version", "the new one", "the improved implementation", or even file names like `ours.png` tip the judge and produce agreeable nonsense. Use `scripts/blind_compare.py` to randomize and neutralize the names rather than doing it by hand, where the ordering habit gives it away.

*Availability:* this needs a matched capture of the exemplar, so it only exists at T1/T2. At T3/T4 use the spec-gate judge below — and do not substitute a mockup of the exemplar for the real thing, since judging against your own reconstruction is an internal opinion wearing the costume of an external test.

---

## Spec-gate judge (T3/T4)

For when you never got direct access to the exemplar. Spawn with no build context; it sees the spec and the artifact, nothing else.

```
Score an artifact against a written specification.

ARTIFACT: <how to run, open, or read it>
SPECIFICATION: <the frozen spec, quoted in full>

For every line of the spec, return one of:
  MET          — with the specific observation that shows it
  NOT MET      — with what you found instead
  UNVERIFIABLE — with what you would have needed in order to check

Method:
- Inspect the artifact directly. Run it, render it, measure it. Do not infer
  compliance from code that looks like it would comply.
- Judge only against the spec as written. If a line is ambiguous, say so and
  mark it UNVERIFIABLE rather than picking the reading the artifact satisfies.
- Do not soften a NOT MET into a MET because the gap looks small. Severity is
  someone else's decision; yours is whether the line is met.

Return:
SCORE: <met>/<total> met, <n> not met, <n> unverifiable
NOT MET:
- <spec line> — <what you found instead>
UNVERIFIABLE:
- <spec line> — <what was missing>
```

*Why:* the ambiguity clause is the load-bearing one. A judge allowed to resolve vague spec lines will resolve them in the artifact's favour every time — not from bias, but because the artifact is the only concrete reading available to it. Pushing ambiguity into `UNVERIFIABLE` turns a soft pass into a visible gap in the spec, which is information you can act on. A high `UNVERIFIABLE` count is not a bad result; it is an accurate measurement of how much your fidelity tier left unsettled, and the honest thing to report alongside the score.

---

## Integration critic

Run after every item ships individually. This one looks between the parts, not inside them.

```
You are reviewing a complete artifact for coherence. Individual components
have already been reviewed and passed. Your job is to find where they fail
to work as one thing.

ARTIFACT: <how to run and explore the whole thing>
THE STANDARD: <exemplar>. Reference material is in .assay/reference/.
RUBRIC: <full rubric>

Look specifically for:
- Inconsistency between components — spacing, type, colour, tone, naming,
  error handling, interaction patterns that differ across parts.
- Seams: transitions between components, handoffs, shared state.
- Anything that reads as assembled rather than designed.
- Regressions where one component's changes degraded another.
- Whole-artifact properties no single component owned: overall performance,
  navigation coherence, the arc of the first-run experience.

Return the same VERDICT / DEFECTS format as a component critique.
```

*Why:* per-item critics were never shown the seams, so seam defects survive every round of component review and are usually the first thing an outsider notices.

---

## Defect record

Keep `.assay/progress.md` as the loop's memory. Without it there is no way to tell converging from oscillating, and the loop runs until someone gets tired.

```markdown
## <item name>

### Round 1 — 2 blockers, 5 majors, 3 minors
- [blocker] <defect> → fixed round 2
- [major] <defect> → recurring, round 3
...
### Round 2 — 0 blockers, 3 majors, 4 minors
...
### Gate — round 3
WINNER: B (reference), confidence medium
TELLS: <what gave it away>
→ 2 new defects logged
```

Severity-weighted totals falling each round means the loop is working. Flat means the design is wrong and more rounds will not help. Rising, or the same defect appearing three times, means stop and change the evidence you are giving the builder — an annotated screenshot, a trace, a direct diff — rather than rewording the same critique again.