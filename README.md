# 🎱 Snarky 8 Ball

A GUI-based Magic 8 Ball built with Python and Tkinter that delivers sarcastic, context-aware responses based on the type of question asked.

This project is part of **AAEL Labs (AI-Augmented Exploratory Learning)** and demonstrates how beginners can progress from simple scripting to interactive applications.

---

## 🚀 Features

- 🎯 Classifies questions into types:
  - who, what, where, when, why, how
  - yes/no questions
  - quantity (how many / how much)
  - duration (how long / how old)
- 😏 Snarky, category-based responses
- 🖥️ Tkinter GUI with visual 8-ball
- ⌨️ Press Enter or click "Ask"
- 🔚 Type `STOP` to exit with a final message
- 🔢 Tracks number of questions asked

---

## 🧠 How It Works

The app uses simple natural language rules to detect the structure of a question:

- `"How many..."` → quantity
- `"Do / Is / Are..."` → yes/no
- `"Why..."` → explanation-based response
- fallback → general sarcasm

This is a lightweight introduction to **rule-based NLP**.

---

## 🛠️ Tech Stack

- Python 3.x
- Tkinter (built-in GUI library)
- Random module

No external dependencies required.

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/snarky_eight_ball.git
cd snarky_eight_ball

```bash
git clone https://github.com/YOUR_USERNAME/snarky_eight_ball.git
cd snarky_eight_ball
