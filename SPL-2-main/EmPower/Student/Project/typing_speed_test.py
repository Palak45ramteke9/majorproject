import tkinter as tk
import random


class TypingSpeedTest:
    def __init__(self, root):
        self.game_window = tk.Toplevel(root)
        self.game_window.title("Typing Speed Test")
        self.game_window.geometry("500x400")
        self.game_window.configure(bg="#ffccbc")

        tk.Label(self.game_window, text="Type the sentence below:", font=("Arial", 18), bg="#ffccbc").pack(pady=20)

        self.target_text = random.choice(
            [
                "The quick brown fox jumps over the lazy dog.",
                "Practice makes perfect.",
                "Typing speed is an art.",
                "Code is poetry.",
            ]
        )

        tk.Label(self.game_window, text=self.target_text, font=("Arial", 14), bg="#ffccbc", wraplength=450).pack(pady=10)

        self.input_entry = tk.Entry(self.game_window, font=("Arial", 14), width=50)
        self.input_entry.pack(pady=10)

        self.result_label = tk.Label(self.game_window, text="", font=("Arial", 14), bg="#ffccbc")
        self.result_label.pack(pady=10)

        tk.Button(
            self.game_window, text="Check", font=("Arial", 14), command=self.check_typing, bg="#ff7043"
        ).pack(pady=10)

        tk.Button(
            self.game_window, text="Close", font=("Arial", 14), command=self.game_window.destroy, bg="#d32f2f"
        ).pack(pady=10)

    def check_typing(self):
        user_text = self.input_entry.get()
        if user_text == self.target_text:
            self.result_label.config(text="Correct! Good job!", fg="green")
        else:
            self.result_label.config(text="Incorrect! Try again.", fg="red")
