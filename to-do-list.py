#We import our gui module tkinter and our date verifier module
import tkinter as tk
from datetime import datetime

tasks = {}
tasks_visible = False


def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def is_past_deadline(date_text):
    current_date = datetime.now().date()
    due_date = datetime.strptime(date_text, '%Y-%m-%d').date()
    return due_date < current_date


def add_task():
    task_name = entry_task_name.get()
    task_due_date = entry_due_date.get()
    if is_valid_date(task_due_date):
        if is_past_deadline(task_due_date):
            label_status.config(
                text="You are past the deadline.\nPlease choose a future date.", fg="red")
        else:
            tasks[task_name.lower()] = task_due_date
            if tasks_visible:
                update_task_list()
            label_status.config(
                text=f"Task '{task_name}' with due date '{task_due_date}' added successfully.", fg="green")
    else:
        label_status.config(
            text="Invalid date format!\nPlease enter the date in YYYY-MM-DD format.", fg="red")


def remove_task():
    task_name = entry_remove_task.get().lower()
    if task_name in tasks:
        del tasks[task_name]
        if tasks_visible:
            update_task_list()
        label_status.config(
            text=f"Task '{task_name.capitalize()}' removed successfully.", fg="green")
    else:
        label_status.config(
            text=f"Task '{task_name.capitalize()}' not found in the list.", fg="red")


def toggle_tasks():
    global tasks_visible
    tasks_visible = not tasks_visible
    if tasks_visible:
        update_task_list()
    else:
        listbox_tasks.delete(0, tk.END)


def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for name, due_date in tasks.items():
        listbox_tasks.insert(
            tk.END, f"{name.capitalize()} - Due Date: {due_date}")


root = tk.Tk()
root.title("To-Do List")

frame_add_task = tk.Frame(root)
frame_add_task.pack(padx=10, pady=10)
label_task_name = tk.Label(frame_add_task, text="Task Name:")
label_task_name.grid(row=0, column=0, padx=5, pady=5)

entry_task_name = tk.Entry(frame_add_task)
entry_task_name.grid(row=0, column=1, padx=5, pady=5)

label_due_date = tk.Label(frame_add_task, text="Due Date (YYYY-MM-DD):")
label_due_date.grid(row=1, column=0, padx=5, pady=5)

entry_due_date = tk.Entry(frame_add_task)
entry_due_date.grid(row=1, column=1, padx=5, pady=5)

button_add_task = tk.Button(frame_add_task, text="Add Task", command=add_task)
button_add_task.grid(row=2, columnspan=2, padx=5, pady=10)

frame_remove_task = tk.Frame(root)
frame_remove_task.pack(padx=10, pady=10)

label_remove_task = tk.Label(frame_remove_task, text="Task Name to Remove:")
label_remove_task.grid(row=0, column=0, padx=5, pady=5)

entry_remove_task = tk.Entry(frame_remove_task)
entry_remove_task.grid(row=0, column=1, padx=5, pady=5)

button_remove_task = tk.Button(
    frame_remove_task, text="Remove Task", command=remove_task)
button_remove_task.grid(row=1, columnspan=2, padx=5, pady=10)


button_display_tasks = tk.Button(
    root, text="Display/Hide Tasks", command=toggle_tasks)
button_display_tasks.pack(padx=10, pady=10)

listbox_tasks = tk.Listbox(root)
listbox_tasks.pack(padx=10, pady=5)

label_status = tk.Label(root, text="", fg="black")
label_status.pack(padx=10, pady=5)

root.mainloop()
