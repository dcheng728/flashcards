# About

- This project is built with the help of Claude Opus, Sonnet and ChatGPT 5.6 Sol.
- The objective is to explore human-AI interactions aimed at human understanding.

This “physics flashcard” project began in March 2026, while I was working on my MSc dissertation in theoretical physics at Imperial College London.
I came to believe that the challenge in AI4physics is not the model's capability, but the human researcher's ability to keep up with and oversee the model's progress.
My view is that until some human can verify, understand, and be held accountable for a piece of work, however elegant or correct, it does not constitute knowledge.

With that being said, the best way I know to learn physics is to do problems: the best books make the readers think and work.
But my agent has never stopped to check my understanding, like a good lecturer would when sensing drowsiness or puzzlement in their audience.
Instead, my agent hands me long markdowns.

So I built this site to let AI quiz me.
The flashcards span many topics (classical, quantum, relativity, ...) and difficulty levels.
Each card is self-graded between *"Got it"*, *"Not sure"*, and *"Missed it"*.
The grades set a familiarity score that decays with a half-life of 133 hours.
These scores map the boundaries of my knowledge, giving an AI agent with access to them a sense of what I know.
The intended workflow is that after a seminar or an agentic research session, I can give the notes to a flashcard agent, which uses my past ratings to create new flashcards just outside my comfort zone.

The more ambitious goal (not realized yet) is to put the flashcards and familiarity scores into a research agent's context.
When given a research task, it could then recognize when it crosses the boundaries of my understanding and pause to ask me technical questions, keeping us in sync.

Ultimately, what I am interested in is how AI can allow me to understand more, not just achieve more in a pragmatic sense.
