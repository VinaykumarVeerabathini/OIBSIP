import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(entry_length.get())
    strength = strength_var.get()

    if strength == 'Low':
        characters = string.ascii_lowercase
    elif strength == 'Medium':
        characters = string.ascii_letters + string.digits
    else:  
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

strength_var = tk.StringVar(value='Low')
tk.Radiobutton(root, text="Low", variable=strength_var, value='Low').grid(row=1, column=0, padx=10, pady=5)
tk.Radiobutton(root, text="Medium", variable=strength_var, value='Medium').grid(row=1, column=1, padx=10, pady=5)
tk.Radiobutton(root, text="Strong", variable=strength_var, value='Strong').grid(row=1, column=2, padx=10, pady=5)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=2, column=0, columnspan=3, padx=10, pady=10)

tk.Label(root, text="Generated Password:").grid(row=3, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, width=30)
entry_password.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=4, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
