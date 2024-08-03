import tkinter as tk
from tkinter import StringVar, messagebox

class TodoList:

    def __init__(self):
        self.task_list = []

    # Voir les tasks ajoutés
    def add_task(self, task):
        if task:  
            self.task_list.append(task)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty")
        self.update_display()
    
    def del_task(self, id_task):
        if 0 <= id_task < len(self.task_list):
            self.task_list.pop(id_task)
        self.update_display()
    
    def update_task(self, id_task, task):
        if 0 <= id_task < len(self.task_list):
            self.task_list[id_task] = task
        self.update_display()

    def update_display(self):
        self.listbox.delete(0, tk.END)
        for task in self.task_list:
            self.listbox.insert(tk.END, task)
    
    def interface(self, fen):
        
        self.entry = tk.Entry(fen, border=2)
        self.entry.pack(expand=True)

        add_btn = tk.Button(fen, text='+', command=lambda: self.add_task(self.entry.get()))
        add_btn.pack(pady=5)

        self.listbox = tk.Listbox(fen)
        self.listbox.pack(expand=True, fill=tk.BOTH)
        
        del_btn = tk.Button(fen, text='Delete', command=self.delete_selected)
        del_btn.pack(pady=5)

        update_btn = tk.Button(fen, text='Update', command=self.update_selected)
        update_btn.pack(pady=5)

    def delete_selected(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.del_task(selected_task_index[0])

    def update_selected(self):
        selected_task_index = self.listbox.curselection()
        new_task = self.entry.get()
        if selected_task_index and new_task:
            self.update_task(selected_task_index[0], new_task)
        else:
            messagebox.showwarning("Input Error", "Select a task and enter the new task name")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList()
    app.interface(root)
    root.mainloop()
    
