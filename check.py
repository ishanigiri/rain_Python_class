class TodoFile:
    def __init__(self, filename="todo_list.txt"):
        self.filename = filename
        # Ensure the file exists by creating it if it doesn't exist
        open(self.filename, 'a').close()

    def add_task(self, task):
        with open(self.filename, 'a') as file:
            file.write(task + "\n")
        print(f"Task '{task}' added to the file.")

    def remove_task(self, task):
        tasks = self._read_tasks()
        if task in tasks:
            tasks.remove(task)
            self._write_tasks(tasks)
            print(f"Task '{task}' removed from the file.")
        else:
            print(f"Task '{task}' not found in the file.")

    def update_task(self, old_task, new_task):
        tasks = self._read_tasks()
        if old_task in tasks:
            index = tasks.index(old_task)
            tasks[index] = new_task
            self._write_tasks(tasks)
            print(f"Task updated from '{old_task}' to '{new_task}'.")
        else:
            print(f"Task '{old_task}' not found in the file.")

    def show_tasks(self):
        tasks = self._read_tasks()
        if tasks:
            print("Your Todo List:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Your Todo List is empty.")

    def _read_tasks(self):
        with open(self.filename, 'r') as file:
            return file.read().splitlines()

    def _write_tasks(self, tasks):
        with open(self.filename, 'w') as file:
            for task in tasks:
                file.write(task + "\n")

# Example usage
todo_file = TodoFile()

todo_file.add_task("Buy groceries")
todo_file.add_task("Finish the report")
todo_file.add_task("Call mom")

todo_file.show_tasks()
todo_file.remove_task("Finish the report")
todo_file.update_task("Buy groceries", "Go for a walk")
todo_file.show_tasks()
