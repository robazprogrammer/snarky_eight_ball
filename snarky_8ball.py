import random
import tkinter as tk


RESPONSES = {
    "who": [
        "Probably someone barely qualified.",
        "Someone who should not be in charge, naturally.",
        "You already know who. You just do not like the answer.",
        "A guy named Steve. That is my final answer."
    ],
    "what": [
        "A mess, most likely.",
        "Something avoidable, yet here we are.",
        "Probably not what you were hoping for.",
        "A bad idea wearing a fake mustache."
    ],
    "where": [
        "Somewhere annoying.",
        "Exactly where you forgot to look.",
        "In a place that will waste your afternoon.",
        "Farther away than your motivation."
    ],
    "when": [
        "Later than you want.",
        "At the least convenient moment.",
        "Soon enough to cause stress.",
        "Not today, and maybe not tomorrow."
    ],
    "why": [
        "Because bad decisions travel in packs.",
        "Because the universe has a sense of humor.",
        "Because somebody ignored common sense.",
        "Because chaos needed a hobby."
    ],
    "how": [
        "With effort, confusion, and a little luck.",
        "Badly at first, then slightly less badly.",
        "One clumsy step at a time.",
        "With more struggle than you seem prepared for."
    ],
    "quantity": [
        "Fewer than you want, more than you deserve.",
        "Enough to keep things interesting.",
        "Somewhere between several and too many.",
        "Not as many as you are hoping for."
    ],
    "duration": [
        "Longer than this conversation should last.",
        "Not nearly as long as you think.",
        "Just long enough to become inconvenient.",
        "A while. Do not make it weird."
    ],
    "yes_no": [
        "No, and that is probably for the best.",
        "Yes, unfortunately.",
        "Technically yes, strategically no.",
        "The answer is yes. The wisdom is questionable.",
        "Not a chance."
    ],
    "general": [
        "Signs point to regret.",
        "I would lower your expectations.",
        "That seems unlikely, but entertaining.",
        "The outlook is messy.",
        "Proceed with caution and snacks."
    ],
    "blank": [
        "You forgot the question. Impressive.",
        "No question? Bold move.",
        "Silence is still not a usable input."
    ]
}


def detect_question_type(question: str) -> str:
    cleaned = question.strip().lower()

    if not cleaned:
        return "blank"

    cleaned = cleaned.replace("?", "")
    words = cleaned.split()

    if len(words) >= 2:
        first_two = f"{words[0]} {words[1]}"
        if first_two in {"how many", "how much"}:
            return "quantity"
        if first_two in {"how long", "how old"}:
            return "duration"

    first_word = words[0]

    if first_word in {
        "is", "are", "do", "does", "did", "will", "can",
        "could", "should", "would", "am", "was", "were",
        "have", "has"
    }:
        return "yes_no"

    if first_word in {"who", "what", "where", "when", "why", "how"}:
        return first_word

    for word in words:
        if word in {"who", "what", "where", "when", "why"}:
            return word

    return "general"


def get_response(question: str) -> tuple[str, str]:
    category = detect_question_type(question)
    response = random.choice(RESPONSES[category])
    return category, response


class Snarky8BallApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Snarky 8 Ball")
        self.root.geometry("700x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#d9d9d9")

        self.question_count = 0

        self.build_ui()

    def build_ui(self) -> None:
        title_label = tk.Label(
            self.root,
            text="Snarky 8 Ball",
            font=("Arial", 24, "bold"),
            bg="#d9d9d9"
        )
        title_label.pack(pady=(20, 10))

        subtitle_label = tk.Label(
            self.root,
            text="Ask your question and prepare for disappointment.\n(Type STOP to exit)",
            font=("Arial", 11),
            bg="#d9d9d9"
        )
        subtitle_label.pack(pady=(0, 10))

        self.canvas = tk.Canvas(
            self.root,
            width=320,
            height=320,
            bg="#d9d9d9",
            highlightthickness=0
        )
        self.canvas.pack(pady=10)

        self.draw_8ball()

        entry_frame = tk.Frame(self.root, bg="#d9d9d9")
        entry_frame.pack(pady=15)

        self.question_entry = tk.Entry(
            entry_frame,
            font=("Arial", 14),
            width=35
        )
        self.question_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.question_entry.bind("<Return>", self.ask_question)

        ask_button = tk.Button(
            entry_frame,
            text="Ask",
            font=("Arial", 12, "bold"),
            command=self.ask_question,
            padx=14,
            pady=4
        )
        ask_button.pack(side=tk.LEFT)

        self.answer_frame = tk.Frame(
            self.root,
            bg="white",
            bd=2,
            relief="solid"
        )
        self.answer_frame.pack(padx=40, pady=20, fill="both")

        self.answer_label = tk.Label(
            self.answer_frame,
            text="Your answer will appear here.",
            font=("Arial", 14),
            bg="white",
            wraplength=560,
            justify="center",
            padx=20,
            pady=20
        )
        self.answer_label.pack()

        self.type_label = tk.Label(
            self.root,
            text="Detected type: none",
            font=("Arial", 10, "italic"),
            bg="#d9d9d9"
        )
        self.type_label.pack(pady=(0, 10))

        self.counter_label = tk.Label(
            self.root,
            text="Questions asked: 0",
            font=("Arial", 10),
            bg="#d9d9d9"
        )
        self.counter_label.pack()

    def draw_8ball(self) -> None:
        self.canvas.create_oval(20, 20, 300, 300, fill="black", outline="gray20", width=3)
        self.canvas.create_oval(95, 95, 225, 225, fill="white", outline="white")
        self.canvas.create_text(
            160, 160,
            text="8",
            font=("Arial", 54, "bold"),
            fill="black"
        )

    def ask_question(self, event=None) -> None:
        question = self.question_entry.get().strip()

        # STOP command
        if question.lower() == "stop":
            self.answer_label.config(
                text="🎱 Finally. Try making better decisions than relying on this lousy app."
            )
            self.type_label.config(text="")
            self.counter_label.config(text=f"Questions asked: {self.question_count}")
            self.root.after(1800, self.root.destroy)
            return

        # Blank input
        if not question:
            self.answer_label.config(text="🎱 You did not even ask a question.")
            return

        category, response = get_response(question)

        self.question_count += 1
        self.answer_label.config(text=f"🎱 {response}")
        self.type_label.config(text=f"Detected type: {category}")
        self.counter_label.config(text=f"Questions asked: {self.question_count}")

        self.animate_ball()
        self.question_entry.delete(0, tk.END)

    def animate_ball(self) -> None:
        self.canvas.delete("all")
        self.canvas.create_oval(15, 15, 305, 305, fill="black", outline="gray30", width=3)
        self.canvas.create_oval(95, 95, 225, 225, fill="white", outline="white")
        self.canvas.create_text(
            160, 160,
            text="8",
            font=("Arial", 54, "bold"),
            fill="black"
        )
        self.root.after(120, self.draw_8ball)


def main() -> None:
    root = tk.Tk()
    app = Snarky8BallApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()