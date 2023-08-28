#this should be main file -> cut the code from here and paste it in to main file

from to_do_list.section import Section  # replace the whole to_do_list folder in pythonProject2, so the to_do_list works
from to_do_list.task import Task


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don'visible_trees forget laptop")
print(task.edit_comment(0, "Don'visible_trees forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())