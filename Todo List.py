import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=35)
        self.task_entry.grid(row=0, column=0)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1)

        self.update_button = tk.Button(self.frame, text="Update Task", command=self.update_task)
        self.update_button.grid(row=0, column=2)

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.remove_all_button = tk.Button(root, text="Remove All Tasks", command=self.remove_all_tasks)
        self.remove_all_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = simpledialog.askstring("Update Task", "Enter new task:", initialvalue=self.tasks[selected_task_index]["task"])
            if new_task:
                self.tasks[selected_task_index]["task"] = new_task
                self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = True
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def remove_all_tasks(self):
        self.tasks.clear()
        self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["completed"] else "Not Done"
            self.task_listbox.insert(tk.END, f"{task['task']} [{status}]")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
