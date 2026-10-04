# About

- This project is built with the help of Claude Opus 4.5–5 and ChatGPT 5.6 Sol.
- The objective is to explore human-AI interactions aimed at human understanding.

This “physics quiz” project began in March 2026, while I was working on my MSc dissertation in theoretical physics at Imperial College London.
Early into my dissertation, I came to believe that the challenge in AI4physics is not the model's capability, but the human researcher's ability to keep up with the breadth and depth of the model's progress.
My view is that until some human can understand, verify, and be held accountable for a piece of work, however elegant or correct, it does not constitute knowledge.

With that being said, the best way I know to learn physics is to do problems: the best books make their audience work.
But my agent has never stopped to check my understanding, like a good lecturer would when sensing drowsiness or puzzlement in the audience's eyes.
Instead, my agent hands me long markdown, and reading it feels like a chore.

So I built this site to let AI quiz me.
The flashcards span many topics (classical, quantum, relativity, ...) and difficulty levels.
Each card is self-graded from 1 to 3.
The grades set a familiarity score that decays with a half-life of 133 hours.
These ratings record what I know, so an AI agent with access to them knows it too.
The intended workflow is that after a seminar or an agent-assisted research session, I can give the notes to a flashcard agent, which uses my past ratings to create new flashcards just outside my comfort zone.

The more ambitious goal (not realized yet) is to put the flashcards into the research agent's context.
The agent can then look at my past performance to gauge my knowledge level, check as it does research whether it is stepping outside the boundary of my knowledge, and if so, stop to ask me technical questions to ensure I am following.

Ultimately, what I am interested in is how AI can allow me to understand more, not just achieve more in a pragmatic sense.
