# Hang In There! 🎉
### A Hangman Game — CIP2026 Final Project
*by Mhmd Ch*

---

My final project for CIP2026 — a Hangman game built fully in Python using Pygame. I wanted to make something that actually looks good, not just a bare-bones console game, so I put a lot of effort into the UI, the colors, and making it feel polished.

---

## What it is

It's Hangman. You know the game. You try to guess a hidden word one letter at a time, and every wrong guess adds another body part to the hanging figure. Guess all the letters before the hangman is complete and you win. Run out of attempts and... well, you know.

What makes this one a bit different is the categories system and the visual style. I went with a warm pastel palette, creams, peaches, soft browns, because I wanted it to feel cozy rather than clinical.

---

## How to run it

You'll need Python and Pygame installed. If you don't have Pygame yet:

```
pip install pygame
```

Then just run:

```
python main.py
```

That's it. No setup, no config files, nothing complicated.

---

## How to play

- Launch the game and hit **Start Game** from the main menu
- A random word will be chosen from one of the categories
- The category is shown as a hint on screen so you're not completely in the dark
- Click the letter buttons to make your guesses
- You get **10 attempts** before the hangman is fully drawn
- If you guess the word in time — you win. If not, the word is revealed at the end

---

## Word Categories

I put together 5 categories with over 120 words total:

- **Animals** — ELEPHANT, FLAMINGO, HEDGEHOG, and more
- **Food** — fruits, veggies, things you'd actually eat
- **Countries** — from LEBANON to AUSTRALIA
- **Objects** — everyday items like HEADPHONES or REFRIGERATOR
- **General / Concepts** — broader words like FRIENDSHIP, MYSTERY, JOURNEY

Each round picks a random category and a random word from it, so it stays fresh.

---

## Features

- Main menu with Start, Instructions, and Quit
- Animated hangman that builds step by step with 10 stages
- On-screen letter buttons with hover effects — no keyboard needed
- Word display updates in real time as you guess
- Win and lose screens that reveal the word
- Gradient background and pastel color scheme throughout

---

## Built with

- **Python 3**
- **Pygame** — for the window, drawing, events, everything

No game engine. No templates. Every line of the drawing, the game logic, the UI — all written from scratch.

---

## Notes

This was built as a final project for CIP2026. It started as a simple idea and ended up being a lot more work than expected (especially getting the hangman figure to look right). If you find any bugs or have suggestions, feel free to reach out.

Hope you enjoy playing it as much as I enjoyed building it.
