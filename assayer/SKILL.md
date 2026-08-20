---
name: assayer
description: "Use when quality is the constraint and someone needs to be sure: feature work, bugfixes, docs, designs, reports, research, reviews, or any ask framed as production-grade, world-class, flawless, exemplar-matching, parallel, or independently reviewed. Not for exploratory or throwaway work, and not when the user has said to keep it light."
---

# Assayer

An assayer takes a sample, tests it against a known standard, and certifies what it actually is. That is the job here, applied to whatever is being asked for.

Every ask gets the same three beats:

1. **Anchor** — what is being made, and what standard says it's good
2. **Build** — the work itself
3. **Prove** — an independent check the builder never touched, then an honest report

The ask is open-ended; the method is not. What varies is *weight*, never structure. A typo fix and a ground-up product both get anchored, built and proved — one takes thirty seconds, the other takes eight agents and five rounds.

Two properties make this work, and every rule below protects one of them:

**Nobody grades their own homework.** Whoever built it already decided it was reasonable — that's why they built it that way. Self-review finds typos, not the flaws that come from the author's own taste. Whatever does the proving must not be what did the building, and must not see its reasoning.

**"Good" has to be falsifiable.** An agent told to make something beautiful stops the moment the output matches its internal picture of beautiful — a competent, generic average. "As good as Linear's issue list" is checkable, because Linear's issue list exists and can be opened. "Polished" is not.

---

## Pick the weight first

State which weight you're using in one line before starting. Declaring it is the guardrail: it stops heavy asks being quietly served with light work, and stops trivial asks eating eight agents.

## Default token discipline

Assayer defaults to the lightest weight that can honestly protect the user's outcome. The method is not permission to spend unlimited context, run every gate, or spawn critics for work that does not need them.

Use this operating default:

> Use Assayer, but default to Light unless the task clearly needs more. Before starting, state the chosen weight and why. Optimize for token discipline: inspect only relevant files, prefer targeted tests, avoid full browser/build matrices unless the change is visual, risky, or near release. Do not spawn subagents unless explicitly requested or required for independent review. If using Heavy mode, declare the round budget and stop when the value no longer justifies the cost. Always report what was skipped.

When token discipline matters, choose the smallest honest option:

- **Answer-only** — for explanation, advice, prompts, or "what do you think?" No repo scan unless needed.
- **Static review** — inspect the relevant files/diff and report findings. No edits, no builds, no browser unless a specific claim needs verification.
- **Targeted verification** — run the smallest test, typecheck, command, or probe that can confirm the risk under discussion.
- **Release gate** — full test/build/browser/accessibility matrix only when near shipping, when the change is visual/interactive, or when a regression would be expensive.
- **Heavy / parallel** — exemplar work, multi-surface redesigns, high-stakes correctness, or explicit user approval for independent critics and iteration.

Practical routing:

- **Light by default** for questions, explanations, reviews, small fixes, config checks, prompt writing, and "can you look at this?" requests.
- **Standard** for real feature work, meaningful bugfixes, docs that need accuracy, or changes where a missed edge would cost the user time.
- **Heavy only** when the user asks for world-class quality, "wow factor", pixel-perfect/premium work, named-exemplar parity, high-stakes correctness, or a multi-surface launch/release.
- **Review-only means no edits, no commits, and no broad verification** unless a specific claim needs checking.
- **Targeted evidence first.** Run the smallest useful check before a full suite, build, browser matrix, accessibility scan, or production probe.
- **Subagents are not automatic.** Use them when the user asks for delegation/parallel work, when the chosen weight requires an independent critic, or when independent review materially reduces risk. Otherwise keep the work local.
- **Keep outputs capped and relevant.** Prefer focused commands and filtered logs; do not pour thousands of lines of test/build output into context when the summary and failing excerpt would do.
- **Name skipped gates.** Token discipline is acceptable only when the user can see what was not checked.

| | **Light** | **Standard** | **Heavy** |
| --- | --- | --- | --- |
| **When** | One right answer. Typo, rename, config, small bugfix. | A feature, page, doc, or module. Most real work. | "World-class", multi-surface, or a named exemplar to beat. |
| **Anchor** | One line: what "correct" means here | Named standard + 3–6 checkable dimensions | Exemplar + fidelity tier + 5–12 *ranked* dimensions |
| **Build** | Just do it | TDD where code, one worktree | Parallel agents on owned paths, calibrate one item first |
| **Prove** | Run the test; re-read against the anchor with fresh eyes | One fresh critic subagent, full verdict format | Critic per item + blind or spec gate + integration pass |

**"Keep it light" ends it.** If the user says that, or "skip assayer", or otherwise signals they want the quick version, drop to Light and stop announcing weight. Ceremony on a task that did not want it is the fastest way to make someone stop reaching for this.

When it's genuinely ambiguous, go one step lighter and say so — an under-weighted task that comes back is cheap, an over-weighted one has already burned the budget. If the user asked for "perfect" or named something to beat, it's Heavy regardless of size.

---

## Working with superpowers

These skills already do most of the build and verify machinery well. Call them; don't reimplement them. Invoke by the bare names below; some installs namespace them as `superpowers:<name>`, so if a bare name does not resolve, check the available-skills list rather than assuming the skill is missing. Assayer's contribution is what they don't cover: the external anchor, the separation rule, the gate, and convergence tracking.

| Beat | Reach for |
| --- | --- |
| **Anchor** | `brainstorming` for anything open-ended or creative — it belongs *here*, before a line is written, and it is where the exemplar and dimensions get pinned down. `writing-plans` once the shape is agreed and the task is multi-step. |
| **Build** | `test-driven-development` for code — tests are an anchor you can run. `using-git-worktrees` for isolation. `dispatching-parallel-agents` and `subagent-driven-development` for parallel dispatch. `executing-plans` when a written plan exists. `systematic-debugging` the moment a defect survives two rounds. |
| **Prove** | `no-ai-slop` for anything with prose in it — its portability test ("if a sentence could move unchanged to another company, it is filler") is the swap test applied to words. `verification-before-completion` — same principle as this skill, evidence before assertions; run it before any completion claim. `requesting-code-review` and `receiving-code-review` for code. `finishing-a-development-branch` to integrate. |

Where they overlap, the superpowers skill wins on mechanics and Assayer wins on standard-setting: brainstorming decides *what* to build, the anchor decides *what good looks like*, and neither substitutes for the other.

### Optional domain sharpening

If `grill-with-docs` is available and the work is still shapeable, run it **after the Assayer anchor and before Superpowers planning**. Assayer sets the quality standard; `grill-with-docs` stress-tests the idea, settles vocabulary, and records durable domain language or hard-to-reverse decisions before the plan turns into implementation steps.

Use it for new products, large features, domain-heavy workflows, or anything where words like booking, venue, shift, client, staff, appointment, payment, or status could mean subtly different things. Skip it for crisp bugfixes, already-approved specs, tiny edits, or anything where creating `CONTEXT.md` / ADR material would be noise.

Default sequence when it applies:

1. Assayer — anchor what "good" means.
2. `grill-with-docs` — sharpen decisions and vocabulary.
3. Superpowers planning — turn the sharpened understanding into a build plan.
4. TDD / implementation / verification — build and prove it.

---

## 1. Anchor

**Name what "good" means before building, in checkable terms.** At Light this is a sentence. At Standard and Heavy, dimensions with pass conditions:

> Weak: "Animations should feel smooth."
> Strong: "Every state transition is 120–200ms, ease-out, no layout shift, 60fps on a 4x-throttled CPU."

**At Heavy, name an exemplar** — one to three real artifacts someone can open. Not "a modern SaaS dashboard" but "Linear's issue list: the density, the keyboard model, how it stays responsive at 5,000 rows." If the user said "world-class" without naming anything, propose two or three and let them pick; that choice says more than any amount of adjective-gathering. Then **rank the dimensions**, because the ranking decides where rounds get spent — otherwise the loop polishes shaders while input latency stays terrible.

**The exemplar is the floor, not the target.** Matching it means you have caught up, not that you have made something worth choosing — a judge who cannot tell the two apart has certified that you are interchangeable, and the original wins that trade. Left alone, an agent matching a named reference produces the category average.

**Name at least one thing true of this subject and almost nothing else, and decide what it changes structurally** — layout, ordering, interaction, what the thing is built around. Not what it looks like in a photograph. Distinguishing facts spent on decoration instead of structure is the specific way this fails.

**Generic output is an information failure before it is a taste failure.** A thin brief produces the house style of the model's own training distribution; the same model given a real product, buyer and job rejects those clichés unprompted. The difference is whether there was anything specific to design *from*. So if you cannot name specifics, that is the blocker to raise, not a gap to paper over — the average is what fills the space where facts should be.

*Check — the swap test:* replace the name, logo and imagery with a competitor's. If nothing breaks, you built a template. `references/distinctiveness.md` has the mechanism and the controls.

**For commercial work, ask where the business is going before anchoring on what it looks like now.** The artifact shows the current model; the standard depends on the one being moved toward, and that lives only in the user's head. Anchor from the artifact alone and you produce a better version of the thing they are trying to stop being. One question — what is changing about how you make money, and what do you want people doing that they cannot today — reorders the whole brief. Ask it before the exemplar, not after.

**Establish how close you can actually get to the exemplar.** This decides which gate exists in beat 3:

| Tier | What you have |
| --- | --- |
| **T1 Direct** | You can run, open, and measure it yourself |
| **T2 Supplied** | The user captured it for you |
| **T3 Published** | Teardowns, design-system docs, changelogs, published source |
| **T4 Recalled** | Your memory of it, written down and corrected by the user |

Check early, and check properly, because tooling failure looks identical to the exemplar being unavailable and the two call for completely different responses.

Work down the rungs rather than stopping at the first refusal. Sandboxed sessions usually block direct outbound HTTP — `curl`, `WebFetch` and browser navigation all fail — while `WebSearch` still works and an installed scraping service reaches sites the sandbox cannot. Declaring T3 with an unused capability sitting there is the commonest way this step goes wrong.

Read the two failures differently: a **proxy refusal** means you cannot get out and another tool may succeed; a **captcha or bot wall** means the site is refusing automation, and no tool fixes it. Bot walls return content without erroring, so glance at a capture before trusting it — a page of captcha text looks exactly like success.

**T2 costs one message and is the highest-leverage move available.** If you're at T3/T4 and the user has the exemplar open on their own machine, ask for captures — screenshots at named viewports, a recording, an exported file. Thirty seconds of their time turns the weakest anchor into the strongest. Ask before building, not after a critic starts guessing.

At T3/T4, write the anchor as a frozen specification before any code exists — it becomes the exit test, and a spec written afterwards drifts toward describing whatever you happened to build.

Keep working files in `.assay/` and add it to `.gitignore`.

---

## 2. Build

At Light, build. At Standard and Heavy:

**Slice so each item can be judged alone.** The test: could a critic who has seen only this item and the anchor reach a verdict? "Improve performance" fails. "First contentful paint under 800ms on a cold cache, throttled 3G" passes.

**Give each item exclusive file ownership.** Parallel agents editing shared paths lose each other's writes, and the damage costs more than the parallelism saved. Sequence overlapping items, or isolate them with worktrees and integrate after.

**Calibrate one item before going parallel.** Take a single representative item through the full cycle first. You're testing the anchor, not the item — a dimension nobody can fail, a critic that rejects everything, an unreachable exemplar detail. Parallelise first and you hit the same flaw in eight agents and pay eight times to fix it.

Builders get the item, its owned paths, its dimensions, and the reference material. They are not asked to assess their own work, and their opinion of it is not collected.

---

## 3. Prove

**The check is independent or it is worthless.** A fresh critic that never saw the build reasoning inspects the **running artifact** — runs it, screenshots it, profiles it, uses it. A diff shows intent; only the artifact shows what the user gets. If an item isn't runnable standalone, batch it with its dependencies or sequence it; never let "not runnable yet" quietly downgrade a check to a code read.

### Making the check trustworthy

Three things reliably corrupt a check. Handle them before spending a round on their output.

**Confirm every candidate defect a second way.** Automated probes over-report, and they do it confidently. A measurement is a hypothesis until something independent agrees — a screenshot beside a computed style, a keyboard path beside a scripted one, a second tool beside the first. The cost is asymmetric: verifying costs seconds, while a false positive costs a whole round plus whatever the builder breaks "fixing" a thing that was already correct. Two specific traps worth knowing: state that only exists under real interaction usually cannot be produced by calling the API for it, and elements that are *deliberately* invisible or absent will read as failures to anything measuring naively.

**"There is no X" needs more evidence than "here is an X", not less.** A missing thing and a thing you failed to look at produce identical silence, so absence is the easiest conclusion in the world to reach wrongly — and it is usually load-bearing, because it licenses a substitute. The specific way this happens is boring: you truncate a listing to read it (`head`, `slice`, "first few results", a contact sheet of the largest files), then reason about the population from the sample. The truncated list looks exactly like a complete one. Before concluding something does not exist, count the full set, and search for the thing by name rather than scanning what happens to be on top. Any sentence of the form "they don't have any…" is a claim about a whole population and should cite how the whole population was checked.

**Inspect wherever the thing actually renders, not where you happen to be looking.** Any artifact with variants — viewports, themes, locales, roles, feature flags, empty and populated states — hides its worst defects in the variant nobody opened. An element that is `display:none` in the one configuration you measured contributes nothing to your results and can be badly broken. Enumerate the variants the item genuinely has and check each; a clean sweep of one configuration is not a clean sweep.

**Your own earlier actions are part of the harness.** A file you created in a previous turn can change how the thing under test builds or behaves — a stray lockfile that moves a tool's inferred project root, an install in the wrong directory, a branch left checked out, a server still holding a port. This presents as a project bug, so it gets debugged as one, and the environment you are measuring is no longer the environment the user has. Before concluding the artifact is broken, account for what you put there.

**Strip the harness before judging.** Dev servers, test rigs and preview tools inject their own furniture — overlay badges, debug banners, hot-reload indicators, seeded placeholder data, watermarks. A critic that has not been told will report it as a defect, every time. Either capture from a production-mode build, or tell the critic exactly what to ignore and why.

```
VERDICT: SHIP | REWORK
DEFECTS (most severe first):
- [blocker|major|minor] <where> — <what's wrong> — <what the standard says instead> — <what fixed looks like>
```

**SHIP means zero blockers, zero majors.** Minors logged, non-blocking. Define this before the first check — an undefined bar is the usual cause of an item ping-ponging forever between two critics silently applying two standards.

Exacting *and specific*. "This doesn't feel right" burns a round and teaches nobody anything; the four-part format forces criticism into something a builder can act on. No praise — `SHIP` says it.

### The gate (Heavy)

**T1/T2 — blind comparison.** Capture matched samples: same viewport and scene, same input, same task, same query. Randomize A and B, keep the key from the judge, and give a judge agent **no project context at all**:

```
WINNER: A | B | TIE
CONFIDENCE: high | medium | low
TELLS: the specific observations that decided it
PER-DIMENSION: <dimension> → A | B | tie, with the reason
```

Passing means the judge picks yours or genuinely can't tell. A confident pick for the exemplar is the most valuable output the whole method produces — those tells are your remaining defect list, written by something with no stake in your feelings. `scripts/blind_compare.py` handles the mechanics.

**T3/T4 — spec gate.** There's nothing to put on the other side. Don't manufacture it: judging against a mockup you built of the exemplar compares your work to your own impression while wearing the costume of an external test. Instead have a fresh judge score the artifact against the frozen spec line by line — met / not met / unverifiable — and use `--self-blind` to compare this round against the last, catching regressions and flat rounds.

**Integration.** Items pass alone and still fail together: fonts drift, error handling diverges, seams show. Run one critic over the whole artifact looking for incoherence *between* parts, then gate again at whole-artifact level.

---

## Guardrails

Due diligence is mostly a set of refusals. These hold at every weight.

- **No completion claim without evidence.** "Tests pass" means you ran them and read the output. Run `verification-before-completion` before saying done.
- **No self-certification.** Whatever proves it must not be what built it. At Light that means at minimum re-reading against the anchor with the build reasoning set aside; at Standard and above it means a separate agent.
- **No claimed parity you can't demonstrate.** A spec gate shows compliance, not parity. *"Meets every line of the spec we derived from published teardowns; no direct comparison was possible"* is a real result. *"Indistinguishable from the real thing"* — when nobody ever managed to see the real thing — is not.
- **No inventing the reference.** If you can't reach the exemplar, say which tier you're on. Never reconstruct it and treat the reconstruction as external.
- **No scope deletion.** Removing a hard requirement so the rest looks clean is a failed round, not a passed one. A stated blocker is a useful result; a quietly dropped feature is not.
- **No silent anchor changes.** The standard is fixed at beat 1. Changing it is a decision you put to the user mid-flight, not an edit.
- **No invented facts, ever.** Numbers, logos, testimonials, certifications, review scores and named people that nobody supplied are fabrication, however plausible they look. Placeholders must be obviously unusable so they cannot ship by accident.
- **No category defaults dressed as decisions.** Every domain has a house style an agent will reach for unprompted — the same off-white, the same serif-and-grotesk pairing, the same three-card row, the same hero-with-one-line-of-copy. Reaching for it is not a decision, it is the absence of one. Any choice you cannot trace to something specific about *this* subject or *this* standard is a default, and defaults are what make the result generic. State the reason or make a different choice.
- **Say what you skipped.** If part of the ask was left out or a check couldn't run, name it. Scaling the work down is the user's call.
- **A documented compromise is not an exempt one.** Writing down "this is a known placeholder / deferred / out of scope" is the honest move, and it quietly creates a blind spot: the note is read as settled, reviewers are told not to raise it, and nobody looks again. Every recorded compromise needs the condition that would reopen it — what would have to become true, or what you never actually checked. Never tell a critic to ignore something without also saying what evidence would change that instruction. The mechanism you use to be honest about a gap is exactly the mechanism that can hide it.

### Knowing when to stop

Track per round in `.assay/progress.md`:

- **Converging** — severity-weighted defects falling. Carry on.
- **Oscillating** — round N breaks what N-1 fixed. Two critics disagree about the anchor. Tighten the ambiguous dimension, restart the item.
- **Flat** — no net reduction. Polish isn't the problem; the design underneath is. Escalate with a recommendation instead of spending another round.
- **Same defect three times** — the builder can't see what the critic sees. Change the evidence, not the wording: an annotated screenshot, a profile trace, a direct diff. Then reach for `systematic-debugging`.

Declare a round budget up front (3 per item, 5 for visual work) so hitting it is a checkpoint rather than a surprise. When it's hit without a SHIP, say what passed, what didn't, and what closing the gap takes. *"Three of four items match; lighting is still visibly behind, here's why"* beats a claim of perfection the user disproves in ten seconds.

---

## Failure modes

A quick self-check when a round feels wrong. Each is covered above; this is the index.

- **Anchor drift** — the standard quietly moving to match what got built.
- **Demo-only fidelity** — the one path you screenshotted is immaculate; everything beside it is rough.
- **Trusting the probe** — a scripted measurement treated as a finding.
- **Reference amnesia** — by round three you are comparing against your memory of the exemplar, not the exemplar.
- **Wrong-axis polish** — rounds spent on the dimension you enjoy rather than the one ranked first.
- **Category average** — passing the gate and being forgettable are entirely compatible.
- **Weight inflation** — Heavy on work that needed Light. Expensive theatre that teaches the user to distrust the method.

## Files

- `references/critique-rubrics.md` — dimensions, inspection technique, and "not there yet" tells across nine domains. Read the section matching the work.
- `references/agent-prompts.md` — builder, critic, blind judge, spec-gate judge, integration critic.
- `scripts/blind_compare.py` — randomized head-to-head, key written outside the judge's directory:
  `python blind_compare.py --ours a.png b.png --reference ref/a.png ref/b.png --out .assay/gate/x --views empty populated`
