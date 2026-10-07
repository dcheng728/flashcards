# Contributing

People and coding agents are welcome to contribute. Open a pull request for small fixes; discuss substantial changes in an issue first. Keep changes focused and never commit credentials or secrets.

## Source files

- `questions/` — flashcards grouped by subject
- `src/` — application HTML, CSS, JavaScript, configuration, and assets
- `pages/about.md` — About page content
- `build.py` — generates the site
- `docs/` — generated GitHub Pages output; do not edit directly

## Flashcards

Add a card to the appropriate `questions/{subject}.md` file using this exact structure:

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

Use `basic`, `intermediate`, or `advanced` difficulty. End every card, including the last in a file, with `===`. The filename supplies the subject; do not add a `subject:` field. Add new subjects to `SUBJECTS` in `build.py`.

### Metadata

- Names are persistent identifiers used by history, sync, and search. Keep them short and unique; avoid renaming existing cards.
- Reuse existing labels instead of creating synonyms.

### Writing

Be clear, clean, and succinct.

- Ask one complete, precise recall question.
- Prefer concrete calculations and physical intuition when they teach the concept as well as formalism.
- Keep the answer to what should be recalled quickly; put reasoning, assumptions, and context in the explanation.
- Define nonstandard symbols and remove filler, repetition, and unnecessary notation.
- Write mathematics as a physicist would use it unless the formalism itself is the subject.

### Typesetting and notation

- Follow the unit and metric conventions in `src/config.js`.
- Keep notation consistent across the question, answer, and explanation.
- Use `$...$` for inline math and `$$...$$` for display math.
- Use standard LaTeX commands with single backslashes, such as `\frac`, `\vec`, and `\hat`.
- Avoid `\,` and `\;` when a normal space or `\quad` is sufficient.
- Reserve standalone `---` and `===` lines for the card structure.

The renderer supports LaTeX, `**bold**`, whole-line bullet and numbered lists, and literal `<pre>...</pre>` blocks. Other Markdown is unsupported; use simple HTML when needed and escape literal `<` and `>` as `&lt;` and `&gt;`.

## Code

The app intentionally uses plain HTML, CSS, and JavaScript with no backend or frontend framework.

- Make the smallest complete change and reuse existing patterns.
- Edit behavior in `src/app.js`, configuration in `src/config.js`, and styles in `src/style.css`.
- Preserve the visual language, responsive layout, keyboard support, semantic markup, labels, and focus behavior.
- Avoid new dependencies unless the platform cannot reasonably solve the problem.
- Keep the field IDs in `.github/ISSUE_TEMPLATE/card-error.yml` synchronized with the report URL in `displayQuestion()`.

## Build and checks

If needed, create the environment with `conda env create -f environment.yml` and activate it with `conda activate flashcards`.

After changing `src/`, `pages/`, or `questions/`, run:

```bash
python build.py
python -m py_compile build.py
node --check src/app.js
git diff --check
```

Commit the generated `docs/` changes. Test affected interface behavior at desktop and mobile widths.

## Pull requests

Explain what changed, why, and how it was checked. Exclude unrelated formatting and file changes.
