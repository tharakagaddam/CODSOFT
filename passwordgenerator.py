import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    username = username_entry.get().strip()
    if not username:
        messagebox.showerror("Invalid Input", "Username cannot be empty.")
        return
    
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    
    password_entry.config(state=tk.NORMAL)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state=tk.DISABLED)
    
    
    result_label.config(text=f"Username: {username}\nPassword: {password}")

root = tk.Tk()
root.title("Password Generator")

username_label = tk.Label(root, text="Enter your username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

length_label = tk.Label(root, text="Enter the desired length for the password:")
length_label.pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, state=tk.DISABLED)
password_entry.pack(pady=5)


result_label = tk.Label(root, text="")
result_label.pack(pady=10)
root.mainloop()
