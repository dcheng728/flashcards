# Contributing

Contributions from people and coding agents are welcome. Keep changes focused, follow the existing design, and edit source files rather than generated output.

## Before you start

For a small correction, open a pull request directly. For a new feature or substantial change, open an issue first so the approach can be agreed before implementation.

Never commit API keys, GitHub tokens, Gist credentials, or other secrets.

## Repository layout

- `src/` — application HTML, CSS, JavaScript, configuration, and assets
- `questions/` — flashcards, grouped by subject
- `pages/about.md` — source for the About page
- `docs/` — generated GitHub Pages output; do not edit directly
- `build.py` — builds `docs/` from the source files

## Adding or editing a flashcard

Choose the appropriate subject file in `questions/` and use this exact structure:

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

Every card must have:

1. A short, unique `###` name.
2. A difficulty of `basic`, `intermediate`, or `advanced`.
3. A comma-separated `labels:` line.
4. A blank line followed by the question.
5. An answer and explanation separated by `---` lines.
6. A final `===` line, including for the last card in a file.

The filename determines the subject. Do not add a `subject:` field to a card. If a new subject is needed, add its file to the `SUBJECTS` list in `build.py`.

### Card content standards

- Treat card names as persistent identifiers. Keep them unique and do not rename existing cards without considering saved and synchronized history.
- Make the question a complete, precise recall prompt.
- Prefer concrete calculations and physical intuition when they teach the concept as well as formalism.
- Keep the answer limited to what a learner should recall quickly.
- Use the explanation for reasoning, assumptions, and physical context.
- Reuse existing labels where possible; avoid synonyms that split one topic across several labels.
- Follow the unit and metric conventions in `src/config.js`.
- Use single backslashes in LaTeX commands, such as `\frac`, `\vec`, and `\hat`.
- Avoid LaTeX spacing commands such as `\,` and `\;` when a normal space or `\quad` is sufficient.
- Do not use standalone `---` or `===` lines inside card content.

Card text supports only:

- `$...$` and `$$...$$` LaTeX
- `- item` bullet lists
- `1. item` numbered lists
- `**bold**`
- Literal `<pre>...</pre>` blocks for ASCII diagrams

Other Markdown is not supported. Use simple HTML when necessary, and escape literal `<` and `>` characters as `&lt;` and `&gt;`.

## Code contributions

The app intentionally uses plain HTML, CSS, and JavaScript with no backend or frontend framework.

- Make the smallest change that solves the problem.
- Reuse existing components, classes, and patterns before adding new ones.
- Keep behavior in `src/app.js`, configuration in `src/config.js`, and styling in `src/style.css`.
- Preserve the existing visual language, spacing, colors, and responsive behavior.
- Check layouts at desktop and mobile widths.
- Preserve accessibility basics: semantic elements, keyboard behavior, labels, focus behavior, and meaningful link text.
- Do not add dependencies unless the existing platform cannot reasonably solve the problem.
- Keep `.github/ISSUE_TEMPLATE/card-error.yml` field IDs synchronized with the report URL built in `displayQuestion()`.

## Build and validation

Set up the build environment if needed:

```bash
conda env create -f environment.yml
conda activate flashcards
```

After changing `src/`, `pages/`, or `questions/`, regenerate `docs/`:

```bash
python build.py
```

Before submitting a pull request, run:

```bash
python build.py
python -m py_compile build.py
node --check src/app.js
git diff --check
```

Confirm that generated `docs/` changes are included. For interface or behavior changes, also test the affected flow in a browser.

## Pull requests

Keep each pull request focused on one change. In its description, explain what changed, why, and how it was checked. Do not include unrelated formatting or file changes.
