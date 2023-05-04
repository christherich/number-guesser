import random
import tkinter as tk
from tkinter import ttk

number = random.randint(1, 100)
guess = 0


def check_guess():
    global guess
    guess = int(entry.get())
    if guess > number:
        label.config(text="Too high", foreground="red")
    elif guess < number:
        label.config(text="Too low", foreground="blue")
    else:
        label.config(text="Correct", foreground="green")


window = tk.Tk()
window.title("Guessing Game")
window.geometry("300x200")
window.configure(background="#F0F0F0")

style = ttk.Style()
style.configure("TLabel", font=("Tahoma", 14,
                "normal"), background="#F0F0F0")
style.configure("TButton", font=("Tahoma", 14), background="#F0F0F0")

label = ttk.Label(window, text="Guess a number: ")
label.pack(pady=30)

entry = ttk.Entry(window)
entry.pack(pady=10)
entry.bind('<Return>', lambda e: check_guess())

button = ttk.Button(window, text="Check", command=check_guess)
button.pack(pady=10)

window.mainloop()
