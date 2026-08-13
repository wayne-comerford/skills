# Beating the reference, not just matching it

Read at the anchor when the work is design, brand, copy or anything where "generic" is a
failure. The short version lives in SKILL.md; this is the evidence and the mechanism.

**The exemplar is the floor, not the target.** Matching it means you have caught up, which is not the same as having made something worth choosing. Left alone, an agent asked to match a named reference produces the *category average* — the design every business of that type already has. It will look competent and it will be interchangeable, which for a client is usually worse than looking rough.

The mechanism is specific and worth recognising, because it is easy to miss while it happens: **the facts that make the subject itself distinct get spent on decoration rather than structure.** A bakery brief naming a wood-fired oven, a communal table and a Saturday queue produces a site that photographs those three things and is otherwise identical to every other bakery site — the facts became image captions instead of design decisions.

So name, at anchor time, **at least one thing that is true of this subject and of almost nothing else, and decide what it changes structurally.** Not what it looks like in a photograph — what it changes about the layout, the ordering, the interaction, the thing the page is built around. A restaurant whose regulars appear on a wall of fame should have that wall in the page structure, not a gallery captioned "our customers".

**Generic output is an information failure before it is a taste failure.** Tested against a thin brief — "a modern landing page for my SaaS startup, make it look really good" — a model produces the house style of its own training distribution: dark near-black ground, violet-to-cyan gradient headline, glassmorphism panels, radial glow, `rounded-2xl` everywhere, a fake browser-chrome mockup, a logo strip, a six-card icon grid, numbered steps, a stats row, a testimonial, three pricing tiers with the middle one highlighted, an FAQ accordion, a gradient closing banner. Given a brief with a real product, a real buyer and a real job, the same model rejects those clichés by name unprompted. The difference is not effort or taste. It is whether there was anything specific to design *from*.

So the fix is upstream of the design: **if you cannot name specifics, that is the blocker to raise, not a gap to paper over.** Ask for them, go and find them, or state plainly what is missing. Building anyway guarantees the average, because the average is what fills the space where facts should be.

**And never invent the facts.** The same test fabricated a customer count, a review score, a performance percentage, a security certification, and a named person at a named company — all plausible, all false, all sitting in shippable HTML. This is the most dangerous form of slop because it looks finished. Placeholders must be visibly unusable: `[CUSTOMER COUNT]`, not `12,400+`. Never a realistic-looking number, logo, quote, or person that no one supplied.

*Check — the swap test:* replace the name, logo and photography with a competitor's. Does anything break, or does it simply become their site? If it works unchanged, you built a template and the reference beat you while you were matching it. A fresh judge should be able to name the distinguishing feature after ten seconds without being told what to look for.

## Where this came from

Two controls, same model, no guidance either time.

**Rich brief** — a named product, a named buyer, a specific job. The model rejected the
clichés unprompted and by name, and built the hero around the actual artifact the product
works on. The control did not fail, so no rule was written for that case.

**Thin brief** — "a modern landing page for my SaaS startup, make it look really good."
The complete house style, plus six fabricated claims: a customer count, a review score, a
performance percentage, an uptime SLA, a security certification, and a testimonial from a
named person at a named company. All plausible, none marked as invented.

Raw controls are in `evidence/`. Open `thin-brief-control.html` rather than taking the
summary on trust.
