# Test record — "the exemplar is the floor" rule

RED-GREEN per `writing-skills`. Same model (Sonnet), same brief, fresh context each.

**Scenario:** design direction for Hearth, an independent Kilkenny bakery — communal
table, wood-fired oven visible from the counter, Saturday queue, regulars known by name.
Brief says "match the quality bar of Aesop's website".

## RED — baseline, no rule

Produced the category average for artisan food:

- Bone `#F5F1EA` background, "no pure black, no pure white"
- Serif display + grotesk body (Tiempos/GT Sectra + Söhne/Inter)
- Muted terracotta accent "used sparingly"
- Full-bleed hero photo with one line of copy bottom-left
- Centred philosophy statement in serif
- "Generous whitespace", "generous vertical rhythm"

All four distinguishing facts appeared **only as photo subjects**. Nothing in the layout,
ordering or interaction depended on any of them. Swap the name and images and it is any
bakery in any city.

## GREEN — with the rule

Same brief, rule prepended:

- Found the distinguishing fact: **a wood-fired oven bakes in batches, so stock is finite
  and time-boxed** — untrue of an electric kitchen that replenishes on demand
- Made it structural: a **live bake board** (item, oven-in time, baking/ready/sold out)
  replaces the hero as the top of the page, and is visibly longer on Saturdays
- Typography followed from the structure: grotesk with tabular numerals so the board reads
  as data; serif explicitly rejected as fighting that
- Colour explicitly rejected "the usual cream-and-terracotta bakery palette"
- Answered the swap test unprompted: "a competitor's oven doesn't sell out on this
  schedule, so the bake board would have to be faked or deleted"

## Result

The rule changed the output from category-average to subject-specific, and the
distinguishing fact reorganised the page rather than decorating it. Two baseline slop
markers were rejected by name.

**Not yet tested:** whether it holds under pressure (deadline, an insistent client, a
strong house style), and whether it survives at Light weight where there is no anchor step.

---

# Second test — where the slop actually lives

Two controls, same model, no guidance either time.

**Rich brief** (Ledgerline: invoice-vs-docket reconciliation for food wholesalers, sold to
finance teams at €5–50m turnover). Output was subject-led and rejected the clichés by name:
"explicitly avoid the two reflex traps: fintech navy-and-gold, and generic SaaS
cream-with-violet-accent". No feature-card grid. Hero showed the actual artifact — an
invoice and a docket with matching lines locked together. **Control did not fail.**

**Thin brief** ("a modern landing page for my SaaS startup, make it look really good").
Produced the complete AI-website dialect: `#05050a` ground, violet-to-cyan gradient
headline, glassmorphism nav, radial glow blobs, grid background, Inter, `rounded-2xl`,
fake browser-chrome dashboard, "Trusted by" strip, six-card icon grid, 01/02/03 steps,
stats row, testimonial, three pricing tiers with the middle highlighted, FAQ accordion,
gradient CTA banner. **Control failed completely.**

## What this changes

The failure is not taste, it is information. Slop fills a vacuum. The same model that
produces clichés on a thin brief rejects them on a rich one, unprompted and without being
told to. So the intervention belongs upstream, at the anchor: missing specifics are a
blocker to raise, not a gap to design around.

## The more serious finding

The thin-brief run **fabricated facts**: 12,400+ teams, 4.9/5 average rating, 38% faster
delivery, 99.98% uptime SLA, SOC 2 Type II, and a testimonial from "Maya Okonkwo, Head of
Product, Fluxion". All invented, all plausible, all in shippable HTML with no marker
distinguishing them from real data.

This is worse than generic. Generic looks bland; fabricated looks finished. Someone
skimming that file would have no way to tell which numbers came from the business and
which the model made up.
