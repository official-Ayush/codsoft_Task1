import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def mark_completed():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task = listbox.get(selected_task_index)
        listbox.itemconfig(selected_task_index, {'bg': 'light green'})
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")


root = tk.Tk()
root.title("To-Do List")


listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg='white')
listbox.pack(padx=10, pady=10)


entry = tk.Entry(root)
entry.pack(padx=10, pady=5)


add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(padx=10, pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(padx=10, pady=5)

mark_button = tk.Button(root, text="Mark Completed", command=mark_completed)
mark_button.pack(padx=10, pady=5)


root.mainloop()
