import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x450")
window.config(bg="#f0f0f0")

choices = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}

user_score = 0
computer_score = 0

# Labels
title = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

user_label = tk.Label(window, text="Your Choice:", font=("Arial", 12), bg="#f0f0f0")
user_label.pack()

user_choice_label = tk.Label(window, text="", font=("Arial", 40), bg="#f0f0f0")
user_choice_label.pack()

computer_label = tk.Label(window, text="Computer's Choice:", font=("Arial", 12), bg="#f0f0f0")
computer_label.pack()

computer_choice_label = tk.Label(window, text="", font=("Arial", 40), bg="#f0f0f0")
computer_choice_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(window, text="You: 0    |   Computer: 0", font=("Arial", 12), bg="#f0f0f0")
score_label.pack()


# Game Logic
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(list(choices.keys()))

    user_choice_label.config(text=choices[user_choice])
    computer_choice_label.config(text=choices[computer_choice])

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"You: {user_score}    |   Computer: {computer_score}")

    play_again = messagebox.askyesno("Play Again?", "Do you want to play another round?")
    if not play_again:
        window.destroy()


button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="✊ Rock", font=("Arial", 12), width=10,
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="✋ Paper", font=("Arial", 12), width=10,
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="✌️ Scissors", font=("Arial", 12), width=10,
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

window.mainloop()
