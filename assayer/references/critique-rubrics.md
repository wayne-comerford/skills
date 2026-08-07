# Domain rubrics and inspection techniques

Starting points, not finished rubrics. In part 1 you study the actual exemplar and write dimensions from what you see there; this file exists so you know where to look and what "inspect it properly" means in each domain. Pick your section, take the dimensions that apply, delete the rest, add what the exemplar reveals.

Every dimension below is phrased so a critic could run a test and reach a verdict someone might disagree with. Keep that property when you adapt them — a dimension nobody could fail is decoration.

## Contents

- [Real-time 3D and games](#real-time-3d-and-games)
- [Web application UI](#web-application-ui)
- [Marketing and landing pages](#marketing-and-landing-pages)
- [API and library design](#api-and-library-design)
- [Developer documentation](#developer-documentation)
- [CLI and TUI](#cli-and-tui)
- [Data pipelines and analytics](#data-pipelines-and-analytics)
- [Written reports and decks](#written-reports-and-decks)
- [Performance work](#performance-work)

---

## Real-time 3D and games

**Dimensions.** Frame time stability under load, not average FPS — a locked 60 beats a jittery 90. Lighting coherence: shadow softness matching light size, believable bounce, no light leaking through geometry. Material response: does metal read as metal at grazing angles, does roughness vary across a surface the way real wear does. Silhouette readability at gameplay distance and at low contrast. Animation weight — anticipation, follow-through, and a settle rather than a snap-stop. Input-to-photon latency. Audio-visual sync on impacts. Camera behaviour during fast motion. Level-of-detail transitions that do not pop. Post-processing that serves readability rather than hiding flat lighting behind bloom.

**How to inspect.** Capture from the same camera position and time-of-day as the reference — comparison is meaningless from different angles. Screenshot with Playwright for browser-based work. Record 5–10 second clips for anything involving motion; stills flatter bad animation enormously. Log frame times and read the 99th percentile, not the mean. View at both full resolution and thumbnail size — thumbnails reveal composition and silhouette problems that full-size viewing hides.

**Tells that it is not there yet.** Uniform surface roughness across a whole material. Shadows all the same softness regardless of light size. Everything lit at the same intensity with no focal hierarchy. Bloom compensating for flat lighting. Animation that starts and stops instantly. Repeating texture tiling visible at gameplay distance. Colours that are individually fine but share no palette discipline.

## Web application UI

**Dimensions.** Optical alignment rather than merely numeric alignment. A spacing scale that is actually adhered to, not approximated. Type hierarchy carried by size, weight, and colour together. Every interactive element having hover, focus-visible, active, disabled, and loading states. All four data states designed — empty, loading, error, populated — with empty and error given real attention rather than a centred grey sentence. Keyboard operability of every action, with visible focus. Contrast passing WCAG AA in both themes. Layout holding from 320px to ultrawide without horizontal body scroll. Perceived latency: optimistic updates and skeletons rather than spinners. Content-driven density rather than uniform generous padding.

**How to inspect.** Screenshot the same routes in the exemplar and yours at identical viewports. Tab through the entire interface without touching the mouse and record where focus disappears. Throttle the network and watch what the loading path actually looks like. Force error and empty states deliberately — they are where polish gaps hide, since nobody demos them. Zoom the browser to 200%. Check both colour themes.

**Tells.** Spinners where skeletons belong. Empty states that are one line of grey text. Focus rings removed rather than restyled. Every card carrying the same shadow at the same elevation. Placeholder text substituting for labels. Disabled buttons with no explanation of what would enable them. Dark mode that is the light palette inverted rather than designed.

## Marketing and landing pages

**Dimensions.** The value proposition legible in under five seconds without scrolling. Typographic scale with real contrast between levels rather than a timid ramp. Imagery that carries information rather than filling space. Whitespace deployed as rhythm, not as uniform padding. One dominant call to action per viewport. Above-the-fold weight under a stated budget. Fonts loaded without visible reflow. Scroll behaviour that stays at 60fps.

**How to inspect.** Squint test at 25% zoom — visual hierarchy either survives or it does not. Read only the headings top to bottom and check the story still makes sense. Measure real load on a throttled connection, not a warm local cache. Compare the fold against the exemplar's fold at the same viewport.

**Tells.** Three competing calls to action in one section. Stock imagery with no informational content. A heading scale where h1 and h2 differ by two pixels. Animation that delays reading rather than directing it.

## API and library design

**Dimensions.** Time from install to first successful call. Naming consistency across the surface — the same concept never wearing two names. Errors that state what went wrong, which input caused it, and what to do next. Argument order and optionality following one predictable rule. Types precise enough that wrong usage fails at compile time rather than at runtime. Defaults safe for the common case. Escape hatches for the uncommon one. Breaking changes gated behind versioning. Sensible behaviour under concurrent use.

**How to inspect.** Write a fresh integration against your own API and against the exemplar's, and count steps, lines, and moments of hesitation. Deliberately misuse both and compare the error messages side by side — this single test discriminates more than any other. Read the type signatures alone and see whether usage is inferable without prose.

**Tells.** Errors that surface an internal exception verbatim. Boolean parameters that change what a function does. `options` objects that accept anything. Two ways to do the same thing with no stated preference. Required arguments that could have had defaults.

## Developer documentation

**Dimensions.** Quickstart to a working result inside a stated time budget. Every code sample runnable exactly as printed, with imports and setup included. Conceptual explanation separated from reference material rather than interleaved. Task-oriented navigation ("how do I…") alongside structural navigation. Errors and troubleshooting documented, not just happy paths. Version-accurate to the shipped code. Searchable headings that use the words a reader would search for.

**How to inspect.** Follow your own quickstart on a clean machine, timing it, and copy-pasting rather than fixing samples as you go. Every place you had to fix something is a defect. Run every code block. Read the reference section for a function you did not write and see whether you could use it.

**Tells.** Samples with elided imports or `...`. "Simply" and "just" in front of multi-step procedures. Screenshots of a version that no longer ships. No error documentation. Prose that explains what a function is named rather than when to reach for it.

## CLI and TUI

**Dimensions.** `--help` sufficient to use the tool without the web. Consistent flag naming and short-form conventions. Progress feedback for anything over a second. Errors on stderr, data on stdout, with exit codes that mean something. Machine-readable output available (`--json`) alongside human-readable. Colour that degrades cleanly when piped or when `NO_COLOR` is set. Destructive operations confirmed or requiring an explicit flag. Ctrl-C leaving no corrupt state.

**How to inspect.** Pipe everything and check the output is still parseable. Run in a 40-column terminal. Run with `NO_COLOR=1` and with output redirected to a file. Interrupt mid-operation and inspect what is left behind. Compare `--help` against the exemplar's for the same task.

**Tells.** Progress bars written to stdout. Errors with exit code 0. Colour escape codes in piped output. Help text that lists flags without saying what they do. Silence during long operations.

## Data pipelines and analytics

**Dimensions.** Idempotent reruns. Explicit schema with validation at boundaries. Null and malformed input handled deliberately rather than incidentally. Lineage traceable from output back to source. Failures partial and resumable rather than all-or-nothing. Row counts and distributions checked between stages. Runtime scaling predictably with input size. Numbers reconciling against a known-good source.

**How to inspect.** Run twice and diff the outputs — anything that differs is non-determinism you did not intend. Feed deliberately corrupt input and see whether it fails loudly or writes something wrong quietly. Kill it mid-run and restart. Reconcile a sample of outputs by hand against source data.

**Tells.** Silent coercion of bad values. `except: pass` around parsing. No row-count assertions between stages. Reruns that duplicate rows. Timestamps without timezones.

## Written reports and decks

**Dimensions.** Conclusion stated before the evidence for it. Each claim traceable to a source. Charts that answer the question in their own title. Consistent terminology throughout. Structure legible from headings alone. Length matched to the decision being supported. Caveats stated where they matter rather than pooled in a footnote.

**How to inspect.** Read only the headings and check the argument holds. Read only the chart titles and check they make claims rather than label axes. Give it to someone with no context and ask what the recommendation was. Check every number against its source.

**Tells.** An executive summary that summarises structure rather than findings. Charts titled with the variable name. Recommendations without owners or dates. Hedging on every claim, which reads as having no findings at all.

## Performance work

**Dimensions.** Stated budgets per operation, measured rather than felt. Tail latency tracked, since p99 is what users report. Load-dependent behaviour characterised, not just single-request numbers. Memory stable over a long run. Cold start distinguished from warm. Regression detection in CI.

**How to inspect.** Measure before optimising and keep the baseline. Profile rather than guessing at hot paths. Test on hardware resembling the target, not on a fast dev machine. Run long enough to expose leaks. Compare against the exemplar on the identical workload, not on your favourable one.

**Tells.** Optimisation with no before-measurement. Averages reported without percentiles. Benchmarks that run entirely warm. "It feels faster" as the evidence. Micro-optimisations while an N+1 query stays in place.