#Roadmap
#tkinter and messagebox import
#creation of basic functions and adding error handling
#initializing tkinter 
#building UI interface


import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry_task.get()
    if task:
        if task not in listbox_tasks.get(0, tk.END):
            listbox_tasks.insert(tk.END, task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Task already exists in the list!")
    else:
        messagebox.showerror("Error", "Task cannot be empty!")

def delete_task(event=None):
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        pass

def update_task(event=None):
    try:
        index = listbox_tasks.curselection()[0]
        task = entry_task.get()
        listbox_tasks.delete(index)
        listbox_tasks.insert(index, task)
    except IndexError:
        pass

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

def mark_done():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(index, {'bg': 'green'})
        task = listbox_tasks.get(index)
        messagebox.showinfo("Task Completed", f"The task '{task}' has been marked as done.")
    except IndexError:
        pass

# Initialize Tkinter
root = tk.Tk()
root.title("TO-DO-LIST")

# Task entry field
entry_task = tk.Entry(root, width=50)
entry_task.grid(row=0, column=0, padx=5, pady=5)

entry_task.bind("<Return>", add_task)


# Add Task button
btn_add_task = tk.Button(root, text="Add Task", width=10, command=add_task)
btn_add_task.grid(row=0, column=1, padx=5, pady=5)

# Update Task button
btn_update_task = tk.Button(root, text="Update Task", width=10, command=update_task)
btn_update_task.grid(row=1, column=0, padx=5, pady=5)

# Delete Task button
btn_delete_task = tk.Button(root, text="Delete Task", width=10, command=delete_task)
btn_delete_task.grid(row=1, column=1, padx=5, pady=5)

# Done button
btn_done = tk.Button(root, text="Done", width=10, command=mark_done)
btn_done.grid(row=1, column=2, padx=5, pady=5)

# Clear All Tasks button
btn_clear_tasks = tk.Button(root, text="Clear All Tasks", width=20, command=clear_tasks)
btn_clear_tasks.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# TO-DO-LIST
listbox_tasks = tk.Listbox(root, width=60)
listbox_tasks.grid(row=3, column=0, columnspan=3, padx=5, pady=5)


listbox_tasks.bind("<Delete>", delete_task)
listbox_tasks.bind("u", update_task)

root.mainloop()
