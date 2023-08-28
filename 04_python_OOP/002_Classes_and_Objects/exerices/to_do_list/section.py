from to_do_list.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for section_task in self.tasks:
            if section_task.name == new_task.name:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for section_task in self.tasks:
            if section_task.name == task_name:
                section_task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for curr_task in self.tasks:
            if curr_task.completed:
                removed_tasks += 1
                self.tasks.remove(curr_task)
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        message = [f"Section {self.name}:"]
        for curr_task in self.tasks:
            message.append(curr_task.details())
        return '\n'.join(message)
