import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime

def add_task():
    task = entry.get()
    if task:
        current_time = datetime.now().strftime("%Y-%m-%d")
        task_with_time = f"{current_time} - {task}"
        listbox.insert(tk.END, task_with_time)
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

root.geometry("600x600")
  
bg = PhotoImage( file = "9111374.png")
  
label1 = Label( root, image = bg)
label1.place(x = -10,y = 0)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg='white', width=40, height=20, borderwidth=2, relief=tk.SOLID)
listbox.pack(padx=80, pady=40)

entry = tk.Entry(root)
entry.pack(padx=90, pady=45)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(padx=10, pady=5, side=tk.LEFT)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(padx=10, pady=5, side=tk.RIGHT)

mark_button = tk.Button(root, text="Mark Completed", command=mark_completed)
mark_button.pack(padx=10, pady=5, side=tk.RIGHT, anchor=tk.CENTER)

root.mainloop()
