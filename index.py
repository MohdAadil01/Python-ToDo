import tkinter as tk

class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, width=20)
        self.add_button.grid(row=0, column=2, padx=5, pady=5)

        self.task_listbox = tk.Listbox(master, width=60, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.mark_done_button = tk.Button(master, text="Mark Done", command=self.mark_done, width=20)
        self.mark_done_button.grid(row=1, column=2, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, width=20)
        self.delete_button.grid(row=2, column=2, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append((task, False)) 
            self.update_task_listbox()

    def mark_done(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            task, status = self.tasks[index]
            self.tasks[index] = (task, not status) 
            self.update_task_listbox()

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task, status in self.tasks:
            status_str = "Done" if status else "Not Done"
            self.task_listbox.insert(tk.END, f"{task} - {status_str}")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
