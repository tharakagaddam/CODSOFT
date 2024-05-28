import tkinter as tk
from tkinter import messagebox

def click_button(item):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(item))
def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=2, bg="powder blue", justify='right')
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    if button == 'C':
        btn = tk.Button(root, text=button, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18),
                        command=clear_entry)
    elif button == '=':
        btn = tk.Button(root, text=button, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18),
                        command=calculate)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18),
                        command=lambda b=button: click_button(b))
    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


root.mainloop()
