import tkinter as tk
from math_challenge import MathChallenge
from typing_speed_test import TypingSpeedTest
from memory_challenge import MemoryChallenge  # Make sure this is imported
from trivia_quiz import TriviaQuiz


class GameLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Productivity Challenge Hub")
        self.root.geometry("800x400")
        self.root.configure(bg="#e0f7fa")

        # Title
        self.title_label = tk.Label(
            root, text="🎮 AutismX 🎮", font=("Arial", 24, "bold"), bg="#00796b", fg="white"
        )
        self.title_label.pack(fill="x", pady=10)

        # Instruction Label
        self.instruction_label = tk.Label(
            root,
            text="Choose a game below to boost your productivity and have fun!",
            font=("Arial", 14),
            bg="#e0f7fa",
            fg="#004d40",
        )
        self.instruction_label.pack(pady=20)

        # Buttons for Games
        self.button_frame = tk.Frame(root, bg="#e0f7fa")
        self.button_frame.pack(pady=20)

        # Horizontal Button Layout
        tk.Button(
            self.button_frame,
            text="Math Challenge",
            font=("Arial", 16),
            bg="#80deea",
            command=lambda: MathChallenge(self.root),
            width=15,
        ).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(
            self.button_frame,
            text="Typing Speed Test",
            font=("Arial", 16),
            bg="#80cbc4",
            command=lambda: TypingSpeedTest(self.root),
            width=15,
        ).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(
            self.button_frame,
            text="Memory Challenge",  # Added button for Memory Challenge
            font=("Arial", 16),
            bg="#b2dfdb",
            command=self.open_memory_challenge,  # Updated this line to open Memory Challenge
            width=15,
        ).grid(row=0, column=2, padx=10, pady=10)

        tk.Button(
            self.button_frame,
            text="Trivia Quiz",
            font=("Arial", 16),
            bg="#aed581",
            command=self.open_trivia_quiz,
            width=15,
        ).grid(row=0, column=3, padx=10, pady=10)

        # Exit Button
        tk.Button(
            root,
            text="Exit",
            font=("Arial", 16),
            bg="#ff8a80",
            command=root.quit,
            width=15,
        ).pack(pady=20)

    def open_memory_challenge(self):
        # Create a new window for Memory Challenge
        memory_window = tk.Toplevel(self.root)
        memory_window.title("Memory Challenge")
        memory_window.geometry("900x600")
        MemoryChallenge(memory_window)  # Pass the new window to the MemoryChallenge class

    def open_trivia_quiz(self):
        # Create a new window for Trivia Quiz
        quiz_window = tk.Toplevel(self.root)
        quiz_window.title("Trivia Quiz")
        quiz_window.geometry("500x400")
        TriviaQuiz(quiz_window)  # Pass the new window to the TriviaQuiz class


if __name__ == "__main__":
    root = tk.Tk()
    app = GameLauncher(root)
    root.mainloop()
