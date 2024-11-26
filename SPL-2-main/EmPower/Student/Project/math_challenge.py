import tkinter as tk
import random


class MathChallenge:
    def __init__(self, root):
        self.game_window = tk.Toplevel(root)
        self.game_window.title("Math Challenge")
        self.game_window.geometry("500x400")
        self.game_window.configure(bg="#ffeb3b")

        tk.Label(self.game_window, text="Solve the math problem!", font=("Arial", 18), bg="#ffeb3b").pack(pady=20)

        self.problem_label = tk.Label(self.game_window, text="", font=("Arial", 18), bg="#ffeb3b")
        self.problem_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.game_window, font=("Arial", 18))
        self.answer_entry.pack(pady=10)

        self.result_label = tk.Label(self.game_window, text="", font=("Arial", 14), bg="#ffeb3b")
        self.result_label.pack(pady=10)

        self.generate_problem()

        tk.Button(
            self.game_window, text="Check Answer", font=("Arial", 14), command=self.check_answer, bg="#cddc39"
        ).pack(pady=10)

        tk.Button(
            self.game_window, text="Close", font=("Arial", 14), command=self.game_window.destroy, bg="#f44336"
        ).pack(pady=10)

    def generate_problem(self):
        self.num1 = random.randint(1, 20)
        self.num2 = random.randint(1, 20)
        self.operator = random.choice(["+", "-", "*"])
        self.solution = eval(f"{self.num1} {self.operator} {self.num2}")
        self.problem_label.config(text=f"{self.num1} {self.operator} {self.num2}")

    def check_answer(self):
        user_input = self.answer_entry.get()
        try:
            if int(user_input) == self.solution:
                self.result_label.config(text="Correct!", fg="green")
            else:
                self.result_label.config(text="Wrong! Try Again.", fg="red")
        except ValueError:
            self.result_label.config(text="Invalid Input. Please enter a number.", fg="red")
