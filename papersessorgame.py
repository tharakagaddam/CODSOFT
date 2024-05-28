import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.user_score = 0
        self.computer_score = 0

        # Set up the main window with a colorful background
        self.root.configure(bg="lightblue")

        # Create widgets
        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14), bg="lightblue")
        self.label.pack(pady=20)

        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play("rock"), font=("Helvetica", 12), bg="lightcoral", fg="white", width=10)
        self.rock_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play("paper"), font=("Helvetica", 12), bg="lightgreen", fg="white", width=10)
        self.paper_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play("scissors"), font=("Helvetica", 12), bg="lightsalmon", fg="white", width=10)
        self.scissors_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="lightblue")
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(root, text="Score - You: 0, Computer: 0", font=("Helvetica", 14), bg="lightblue")
        self.score_label.pack(pady=20)

        self.play_again_label = tk.Label(root, text="", font=("Helvetica", 14), bg="lightblue")
        self.play_again_label.pack(pady=20)

        self.yes_button = tk.Button(root, text="Yes", command=self.play_again_yes, font=("Helvetica", 12), bg="lightblue", fg="green", width=10)
        self.no_button = tk.Button(root, text="No", command=self.play_again_no, font=("Helvetica", 12), bg="lightblue", fg="red", width=10)

    def get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "user"
        else:
            return "computer"

    def play(self, user_choice):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)

        if winner == "tie":
            result_text = f"Both chose {user_choice}. It's a tie!"
        elif winner == "user":
            result_text = f"You chose {user_choice}, computer chose {computer_choice}. You win!"
            self.user_score += 1
        else:
            result_text = f"You chose {user_choice}, computer chose {computer_choice}. You lose!"
            self.computer_score += 1

        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")
        self.ask_play_again()

    def ask_play_again(self):
        self.play_again_label.config(text="Do you want to play again?")
        self.yes_button.pack(side=tk.LEFT, padx=20)
        self.no_button.pack(side=tk.RIGHT, padx=20)

    def play_again_yes(self):
        self.result_label.config(text="")
        self.play_again_label.config(text="")
        self.yes_button.pack_forget()
        self.no_button.pack_forget()

    def play_again_no(self):
        self.root.quit()

def main():
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main()
