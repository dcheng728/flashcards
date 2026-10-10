"""Build docs/ from src/, pages/about.md and questions/*.md files."""

import os
import json
import re
import shutil

import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT, 'src')
QUESTIONS_DIR = os.path.join(ROOT, 'questions')
DOCS_DIR = os.path.join(ROOT, 'docs')
PAGES_DIR = os.path.join(ROOT, 'pages')

SUBJECTS = [
    'math-calculus', 'math-linear-algebra', 'math-differential-equations',
    'math-complex-analysis', 'math-discrete', 'math-probability',
    'math-trigonometry', 'math-special-functions', 'math-group-theory',
    'classical-mechanics', 'electromagnetism', 'quantum-mechanics',
    'statistical-mechanics', 'relativity', 'quantum-field-theory',
    'astro-observational-methods', 'astro-cosmology', 'astro-dark-matter',
    'astro-stellar-astrophysics', 'optics',
]


def slugify(name):
    """URL-safe form of a card name: \\sin -> sin, other runs of non-alphanumerics -> '-'."""
    s = re.sub(r'\\([a-zA-Z]+)', r'\1', name)
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def parse_questions(text, subject):
    text = re.sub(r'^<!--.*?-->\s*\n+', '', text, flags=re.DOTALL)
    questions = []
    for block in re.split(r'^===$', text, flags=re.MULTILINE):
        block = block.strip()
        if not block:
            continue
        sections = re.split(r'^---$', block, flags=re.MULTILINE)
        if len(sections) < 3:
            continue

        header_and_question = sections[0]
        answer = sections[1].strip()
        explanation = sections[2].strip()

        lines = header_and_question.strip().split('\n')
        name = re.sub(r'^###\s*', '', lines[0]).strip()

        difficulty = ''
        labels = []
        question_lines = []
        past_meta = False
        for line in lines[1:]:
            if not past_meta:
                if line.startswith('difficulty:'):
                    difficulty = line[11:].strip()
                elif line.startswith('labels:'):
                    labels = [l.strip() for l in line[7:].split(',') if l.strip()]
                elif line.strip() == '':
                    past_meta = True
            else:
                question_lines.append(line)

        questions.append({
            'name': name,
            'question': '\n'.join(question_lines).strip(),
            'answer': answer,
            'explanation': explanation,
            'subject': subject,
            'difficulty': difficulty,
            'labels': labels,
        })
    return questions


def build_questions():
    all_questions = []
    for subject in SUBJECTS:
        path = os.path.join(QUESTIONS_DIR, f'{subject}.md')
        if not os.path.exists(path):
            print(f'  warning: {subject}.md not found, skipping')
            continue
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        questions = parse_questions(text, subject)
        print(f'  {subject}: {len(questions)} questions')
        all_questions.extend(questions)

    # Share links use slugify(name), so the name -> slug mapping must be one-to-one.
    by_slug = {}
    for q in all_questions:
        q['slug'] = slugify(q['name'])
        if not q['slug']:
            raise SystemExit(f"error: card name '{q['name']}' has no letters or digits to make a link from")
        if q['slug'] in by_slug:
            raise SystemExit(f"error: '{q['name']}' and '{by_slug[q['slug']]}' give the same link '{q['slug']}'")
        by_slug[q['slug']] = q['name']

    js = 'const ALL_QUESTIONS = ' + json.dumps(all_questions, ensure_ascii=False, indent=2) + ';\n'
    out = os.path.join(DOCS_DIR, 'questions.js')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f'  -> {len(all_questions)} questions written')
    return len(all_questions)


def copy_src():
    for name in os.listdir(SRC_DIR):
        src = os.path.join(SRC_DIR, name)
        dst = os.path.join(DOCS_DIR, name)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
            print(f'  {name}')


def build_about():
    """Render pages/about.md into the src/about.html template."""
    with open(os.path.join(PAGES_DIR, 'about.md'), encoding='utf-8') as f:
        body = markdown.markdown(f.read())
    with open(os.path.join(SRC_DIR, 'about.html'), encoding='utf-8') as f:
        template = f.read()
    with open(os.path.join(DOCS_DIR, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(template.replace('{{content}}', body))


def main():
    os.makedirs(DOCS_DIR, exist_ok=True)

    print('Copying src/ -> docs/')
    copy_src()

    print('Building pages/about.md')
    build_about()

    print('Building questions/')
    build_questions()

    print('\nDone.')


if __name__ == '__main__':
    main()
