# Skills

Claude Code skills. Each directory is one skill: a `SKILL.md` with YAML frontmatter, plus any references and scripts it needs.

## Install

Clone anywhere and symlink the skills you want into `~/.claude/skills/`, which makes them available in every project:

```bash
git clone https://github.com/wayne-comerford/skills.git ~/projects/skills
ln -s ~/projects/skills/assayer ~/.claude/skills/assayer
```

Symlinking rather than copying means `git pull` updates the installed skill in place. For a single project instead of globally, symlink into that project's `.claude/skills/`.

## Skills

### [assayer](assayer/)

**The short version.** Say you want to bake a cake as good as the one from the bakery. Most people bake one, taste it, and decide it's lovely — but they baked it, so of course they like it. Assayer makes you do it the other way round: put the bakery cake on the table *first* and write down what makes it good (very lemony, squishy not dry, thin icing). Then bake. Then cut a slice of each, hide which is which, and hand both to someone who didn't bake either one. If they pick the bakery cake, ask why — "yours is dry" is your list. Bake again. You're done when they can't tell which is which.

Writing the standard down first is the part people skip, and it's the part that matters: a standard written afterwards just describes whatever you happened to produce.

The thing you measure against doesn't have to be another product. It's often a rule book — a spec, a performance budget, an accessibility standard, a set of tests. Anything with a number in it that someone else could check.

Two more rules. **Sometimes you can't get the bakery cake** — it's behind a login, it's a competitor's, the sandbox blocks the internet. Then write down everything you know about it before you build, and say plainly that you never tasted it. **Sometimes stop** — if three rounds are wrong in the same way, a fourth won't help; the recipe is wrong, not the baking.

---

An assayer takes a sample, tests it against a known standard, and certifies what it actually is. This is that, as a default working method for any request.

Every ask gets the same three beats — **anchor** what "good" means in checkable terms, **build**, then **prove** with an independent check the builder never touched. The ask is open-ended; the method isn't. What varies is weight, never structure: a typo fix and a ground-up product both get anchored, built and proved, one in thirty seconds and one across eight agents and five rounds.

Two properties do the real work, and every rule in the skill protects one of them:

- **Nobody grades their own homework.** Whoever built it already decided it was reasonable. Whatever proves it must not be what built it, and must not see its reasoning.
- **"Good" has to be falsifiable.** "As good as Linear's issue list" is checkable, because Linear's issue list exists and can be opened. "Polished" is not.

Most of the skill is the machinery that keeps a quality loop from either running forever or stopping too early: dimensions ranked so effort lands where it matters, exclusive file ownership so parallel agents stop overwriting each other, one calibration pass before going parallel, a defined bar for what "done" means, convergence tracking that tells improvement apart from churn, and an exit test that degrades honestly when the thing you're measuring against turns out to be unreachable.

Composes with the superpowers skills rather than replacing them — brainstorming and planning at the anchor, TDD and worktrees and parallel dispatch at the build, verification and code review at the proof. Its own contribution is the external anchor, the separation rule, the gate, and knowing when to stop.

Includes rubric dimensions and inspection technique for nine domains, prompt templates for each agent role, and `blind_compare.py`, which builds a randomised head-to-head and writes the answer key outside the directory the judge is given.

## Writing a skill

The `description` in the frontmatter is the whole triggering mechanism — Claude decides whether to consult a skill from the name and description alone, so it needs to say both what the skill does and when to reach for it. Keep `SKILL.md` under ~500 lines and push detail into `references/`, which get read only when relevant.

## Licence

MIT.