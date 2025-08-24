import random
import tkinter as tk
from tkinter import messagebox

# Create the main Tkinter window
root = tk.Tk()
root.title("Hangman Game")

# Ask for the user's name
name_var = tk.StringVar()

def get_name():
    global name
    name = name_var.get()
    name_label.config(text="Good luck! " + name)
    name_entry.config(state="disabled")
    submit_button.config(state="disabled")

tk.Label(root, text="What is your name?").pack()
name_entry = tk.Entry(root, textvariable=name_var)
name_entry.pack()
submit_button = tk.Button(root, text="Submit", command=get_name)
submit_button.pack()

# Original game setup
words = ['rainbow', 'computer', 'science', 'programming', 'python',
         'mathematics', 'player', 'condition', 'reverse', 'water',
         'board', 'geeks', 'poes', 'tottiekop']

word = random.choice(words)

guesses = ''
turns = 12

game_label = tk.Label(root, text="Guess the characters")
game_label.pack()

word_display = tk.Label(root, text="_ " * len(word), font=("Arial", 14))
word_display.pack()

guess_var = tk.StringVar()
guess_entry = tk.Entry(root, textvariable=guess_var)
guess_entry.pack()

def check_guess():
    global guesses, turns

    guess = guess_var.get().lower()
    guess_var.set("")  # Clear input field
    guesses += guess

    failed = 0
    display_text = ""

    for char in word:
        if char in guesses:
            display_text += char + " "
        else:
            display_text += "_ "
            failed += 1

    word_display.config(text=display_text)

    if failed == 0:
        messagebox.showinfo("You Win!", f"Congratulations! The word was '{word}'.")
        root.quit()

    if guess not in word:
        turns -= 1
        game_label.config(text=f"Wrong! You have {turns} more guesses.")

        if turns == 0:
            messagebox.showerror("Game Over", f"You lost! The word was '{word}'.")
            root.quit()

tk.Button(root, text="Submit Guess", command=check_guess).pack()

root.mainloop()
