import tkinter as tk
from tkinter import ttk, messagebox
import random

random_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry_guess.get())
        attempts += 1
        
        if guess < random_number:
            result.set("Too low! Try again.")
        elif guess > random_number:
            result.set("Too high! Try again.")
        else:
            result.set(f"Congratulations! You guessed it in {attempts} attempts.")
            messagebox.showinfo("Game Over","You guessed the number {random_number} correctly in {attempts} attempts!")
            reset_game()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

# Function to reset the game
def reset_game():
    global random_number, attempts
    random_number = random.randint(1, 100)
    attempts = 0
    entry_guess.delete(0, tk.END)
    result.set("")


root = tk.Tk()
root.title("Guess the Number Game")

# Input Section
frame_input = ttk.Frame(root, padding="10")
frame_input.grid(row=0, column=0, padx=10, pady=10)

ttk.Label(frame_input, text="Guess the number (1-100):").grid(row=0, column=0, padx=5, pady=5)
entry_guess = ttk.Entry(frame_input, width=20)
entry_guess.grid(row=0, column=1, padx=5, pady=5)

frame_buttons = ttk.Frame(root, padding="10")
frame_buttons.grid(row=1, column=0, padx=10, pady=10)

button_check = ttk.Button(frame_buttons, text="Check", command=check_guess)
button_check.grid(row=0, column=0, padx=5, pady=5)

button_reset = ttk.Button(frame_buttons, text="Reset Game", command=reset_game)
button_reset.grid(row=0, column=1, padx=5, pady=5)

# Output Section
frame_output = ttk.Frame(root, padding="10")
frame_output.grid(row=2, column=0, padx=10, pady=10)

result = tk.StringVar()
label_result = ttk.Label(frame_output, textvariable=result, background="white", relief="solid", width=40)
label_result.grid(row=0, column=0, padx=5, pady=5)

root.mainloop()