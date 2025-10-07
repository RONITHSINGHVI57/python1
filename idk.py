import tkinter as tk
import random

def play_game(user_choice):
    """Plays a round of Rock-Paper-Scissors and updates the GUI."""
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    result_text = f"You chose: {user_choice.capitalize()}\nRONITH SINGHVI chose: {computer_choice.capitalize()}\n"

    if user_choice == computer_choice:
        result_text += "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result_text += "You win!"
    else:
        result_text += "RONITH SINGHVI wins!"

    result_label.config(text=result_text)

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x300")

# Instruction Label
instruction_label = tk.Label(root, text="Choose your move:", font=("Arial", 14))
instruction_label.pack(pady=10)

# Buttons for user choices
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_game('rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_game('paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_game('scissors'))
scissors_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
