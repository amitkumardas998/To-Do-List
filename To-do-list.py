import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def mark_task_done():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, f"{task} ✔")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as done.")

def close_app():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x300")

# Styling
root.configure(bg="#f5f5f5")
font_style = ("Helvetica", 12)

# Create and place the widgets
frame_tasks = tk.Frame(root, bg="#ffffff", padx=10, pady=10)
frame_tasks.pack(pady=20, fill=tk.BOTH, expand=True)

listbox_tasks = tk.Listbox(frame_tasks, width=40, height=10, font=font_style, bg="#e6e6e6", selectmode=tk.SINGLE)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=40, font=font_style, bd=2, relief=tk.SUNKEN)
entry_task.pack(pady=10)

button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

button_add_task = tk.Button(button_frame, text="Add Task", command=add_task, font=font_style, bg="#4CAF50", fg="white", bd=0, padx=10, pady=5)
button_add_task.pack(side=tk.LEFT, padx=5)

button_delete_task = tk.Button(button_frame, text="Delete Task", command=delete_task, font=font_style, bg="#f44336", fg="white", bd=0, padx=10, pady=5)
button_delete_task.pack(side=tk.LEFT, padx=5)

button_mark_done = tk.Button(button_frame, text="Mark Done", command=mark_task_done, font=font_style, bg="#2196F3", fg="white", bd=0, padx=10, pady=5)
button_mark_done.pack(side=tk.LEFT, padx=5)

button_close_app = tk.Button(button_frame, text="Exit", command=close_app, font=font_style, bg="#9E9E9E", fg="white", bd=0, padx=10, pady=5)
button_close_app.pack(side=tk.LEFT, padx=5)

# Run the main event loop
root.mainloop()