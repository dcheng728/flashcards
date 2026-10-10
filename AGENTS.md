# Physics Flashcards: Agent Instructions

## Project overview

This repository contains a static flashcard app for reviewing theoretical physics and mathematics. It has no backend and is deployed to GitHub Pages from `docs/`.

The app opens directly on a question. Users reveal the answer, self-grade with Got it, Not sure, or Missed it, and continue through a filtered queue. Progress is stored in browser `localStorage` and can optionally be synchronized through a GitHub Gist.

## Sources of truth

- Edit application source files in `src/`.
- Edit question content in `questions/`.
- Edit the About page text in `pages/about.md` (rendered into `src/about.html` by `build.py`; plain Markdown, no KaTeX).
- Treat `docs/` as generated output. Do not edit it directly.
- Run `python build.py` after changing `src/`, `pages/`, or `questions/` and commit the resulting `docs/` changes.
- Optional git hooks live in `.githooks/`; enable them once per clone with `git config core.hooksPath .githooks`. `pre-commit` rebuilds and stages `docs/` whenever a commit touches `questions/`, `src/`, `pages/` or `build.py`, and aborts the commit if the build fails. `pre-push` refuses to push a stale `docs/`, which also covers merges, rebases, cherry-picks and `git commit --no-verify`.

## Repository structure

```text
src/
  index.html        Flashcards page structure
  about.html        About page
  style.css         Application styles
  favicon.svg       Tab icon (card stack with a pendulum)
  app.js            Cards, filters, queue, history, and sync logic
  config.js         Familiarity scores and conventions
pages/              Markdown source for the About page
questions/          Markdown question files, one per subject
docs/               Generated GitHub Pages output
build.py            Generates docs/ from src/ and questions/
environment.yml     Python environment for the build
```

## Application behavior

- Subject filters use union logic: a question matches when its subject is selected.
- Label filters use intersection logic: a question must have every selected label.
- The available queue orders are most unfamiliar, random, most familiar, and least seen.
- Random ordering gives recently missed or uncertain questions a greater chance of appearing earlier. Each question still appears at most once in a queue.
- Familiarity is a recency-weighted average of previous grade scores. Older grades lose influence relative to newer grades; an isolated grade does not decrease solely as time passes because the result is normalized by total weight.
- Question names are persistent identifiers used by history, Gist synchronization, and search. Keep every name unique and avoid renaming existing questions without considering history migration.
- KaTeX is loaded from a CDN and renders `$...$` and `$$...$$` expressions.
- Each card has a "Report an issue" link that opens a pre-filled GitHub issue form (`.github/ISSUE_TEMPLATE/card-error.yml`, label `card-feedback`). Its field ids (`card`, `subject`) are the URL parameters set in `displayQuestion`; keep them in sync, and keep `CONFIG.repoUrl` pointing at the repo. The GitHub icon in the header of `index.html` and `about.html` points there too.
- Each card has a Share button that shares (native share sheet where supported, otherwise copies) `<page url>#<slug>`. The slug is `slugify(name)` from `build.py` (for example `Gaussian integral` becomes `gaussian-integral`), emitted as `slug` in `docs/questions.js`; the build fails if two names give the same slug. The address bar always shows the current card's `#<slug>` (via `replaceState`, so no history entries, written 150 ms after the last card change because browsers throttle or drop rapid calls); opening such a link (a new visit, a bookmark, or pasting it into an open tab) puts that card first in the queue, but a reload ignores the hash and starts a fresh queue, since the hash is only the last card shown. An unknown slug just opens the normal queue. Renaming a card changes its link.
- API keys and Gist credentials are stored locally in the browser. Never commit credentials to the repository.

## Question format

Questions live in `questions/{subject}.md`. The filename determines the subject; question blocks do not contain a `subject:` field.

```text
### short unique name
difficulty: basic
labels: tag1, tag2

Full question text with $\LaTeX$?

---

Answer text.

---

Explanation text.

===
```

Each block must contain:

1. A unique `###` name.
2. A difficulty of `basic`, `intermediate`, or `advanced`.
3. A comma-separated `labels:` line.
4. A blank line followed by the question.
5. Two `---` separators dividing the question, answer, and explanation.
6. A final `===` separator, including after the last question in a file.

Use single backslashes in LaTeX commands, such as `\frac`, `\vec`, and `\hat`. Do not place standalone `---` or `===` lines inside the question, answer, or explanation. Avoid `\,` and `\;` spacing commands where a plain space or `\quad` reads fine.

### Formatting

`app.js` renders question/answer/explanation text with `formatCardText`: standard Markdown (CommonMark plus GitHub tables and strikethrough, parsed by `marked` from a CDN), with `$...$` and `$$...$$` math rendered by KaTeX. What renders in a standard Markdown editor renders here.

- A single newline is a soft break (it joins the lines with a space). A blank line starts a new paragraph. Two trailing spaces (or a trailing backslash) force a line break.
- Math is lifted out before Markdown runs, so `_`, `*`, `\` and newlines inside it are safe, a `$$ ... $$` block may span lines, and a bare `<` or `>` inside math (`\sum_{i<j}`) is fine. Write a literal dollar sign as `\$`.
- Lists, `**bold**`, `*italic*`, `` `code` ``, links, blockquotes and tables work as usual. A literal `<pre>...</pre>` block (for ASCII diagrams) passes through untouched.
- Raw HTML in the `.md` source is passed through unsanitized, so escape a literal `<` or `>` outside math as `&lt;`/`&gt;`.
- If the CDN script fails to load, the raw text is shown instead.

## Writing questions

- Make the name the shortest unambiguous index entry for the topic.
- Make the question a complete and precise recall prompt.
- Frame mathematical questions in the way a physicist would use the concept.
- Prefer concrete calculations and physical intuition over formalism when either approach teaches the same point.
- Keep the answer focused on the result a student should recall quickly.
- Use the explanation to show reasoning, clarify assumptions, or connect the result to physics.
- Follow the metric and unit conventions in `src/config.js`.

Examples:

| Name | Question |
| --- | --- |
| `derivative of $\sin(x)$` | What is $\frac{d}{dx}\sin(x)$? |
| `Gaussian integral` | Evaluate $\int_{-\infty}^{\infty}e^{-x^2}\,dx$. |
| `formula for variance and STD` | Express $\operatorname{Var}[X]$ in terms of expectations. What is the standard deviation? |

## Validation

After making changes, run the relevant checks:

```bash
python build.py
python -m py_compile build.py
node --check src/app.js
git diff --check
```

Confirm that `docs/` was regenerated when source or question files changed. There is currently no automated test suite, so exercise affected behavior in a browser when changing application logic.

## Shorthand

- **SGMM**: "stage and give me message" — stage the pending changes (`git add`) and propose a commit message; do not commit until approved.
