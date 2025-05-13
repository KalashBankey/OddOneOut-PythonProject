from random import randint
import tkinter as tk
from tkinter import messagebox
from time import sleep

def check_guess():
    guess = int(entry.get())
    if guess == odd:
        messagebox.showinfo("Result", "Congratulations! You found the odd one out!")
    else:
        messagebox.showinfo("Result", f"Sorry, that's not correct. The odd one was: {odd}")
    root.destroy()

root = tk.Tk()
root.title("Odd One Out Game")

t = randint(1,10)
table = [[t for _ in range(10)] for _ in range(10)]
odd = randint(1,10)
a, b = randint(0,9), randint(0,9)
table[a][b] = odd if odd!=t else t+1

label = tk.Label(root, text="Find the odd one out in the table:", pady=10)
label.pack()

table_text = tk.Text(root, height=10, width=30)
table_text.pack(pady=10)
for row in table:
    table_text.insert(tk.END, " ".join(str(x) for x in row) + "\n")
table_text.config(state='disabled')

entry_label = tk.Label(root, text="Enter your guess:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=check_guess)
submit_button.pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import messagebox
from time import sleep
t=randint(1,10)
print("Welcome to the Odd One Out Game!")
table = [[t for _ in range(10)] for _ in range(10)]
print("The table is being generated...")
sleep(2)
odd=randint(1,10)
a=randint(0,9)
b=randint(0,9)
table[a][b]=odd if odd!=t else t+1
print("Find the odd one out!") 
print("The table is:")
for row in table:
    print(" ".join(str(row)),end="\n")
guess = int(input("Enter your guess: "))
if guess == odd:
    print("Congratulations! You found the odd one out!")
else:
    print("Sorry, that's not correct. Better luck next time!")
print(f"The odd one is: {odd}")