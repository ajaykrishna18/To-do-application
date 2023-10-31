import tkinter as tk

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

def add_task():
    description = description_entry.get()
    due_date = due_date_entry.get()
    priority = priority_entry.get()
    task = Task(description, due_date, priority)
    tasks.append(task)
    update_task_list()
    clear_input_fields()

def complete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        tasks[index].completed = True
        update_task_list()

def remove_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        tasks.pop(index)
        update_task_list()

def update_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        task = tasks[index]
        new_description = description_entry.get()
        new_due_date = due_date_entry.get()
        new_priority = priority_entry.get()
        if new_description:
            task.description = new_description
        if new_due_date:
            task.due_date = new_due_date
        if new_priority:
            task.priority = new_priority
        update_task_list()
        clear_input_fields()

def clear_input_fields():
    description_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)

def update_task_list():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "Completed" if task.completed else "Incomplete"
        task_listbox.insert(tk.END, f"{i + 1}. {task.description} ({status})")

tasks = []
app = tk.Tk()
app.title("To-Do List Application")
description_label = tk.Label(app, text="Description:")
description_label.grid(row=0, column=0, padx=10, pady=5)
description_entry = tk.Entry(app, width=40)
description_entry.grid(row=0, column=1, padx=10, pady=5)
due_date_label = tk.Label(app, text="Due Date:")
due_date_label.grid(row=1, column=0, padx=10, pady=5)
due_date_entry = tk.Entry(app, width=40)
due_date_entry.grid(row=1, column=1, padx=10, pady=5)
priority_label = tk.Label(app, text="Priority:")
priority_label.grid(row=2, column=0, padx=10, pady=5)
priority_entry = tk.Entry(app, width=40)
priority_entry.grid(row=2, column=1, padx=10, pady=5)
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.grid(row=3, column=0, columnspan=2, pady=10)
update_button = tk.Button(app, text="Update Task", command=update_task)
update_button.grid(row=4, column=0, columnspan=2, pady=10)
task_listbox = tk.Listbox(app, width=50, height=10)
task_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
complete_button = tk.Button(app, text="Mark as Completed", command=complete_task)
complete_button.grid(row=6, column=0, padx=10, pady=5)
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.grid(row=6, column=1, padx=10, pady=5)
update_task_list()
app.mainloop()