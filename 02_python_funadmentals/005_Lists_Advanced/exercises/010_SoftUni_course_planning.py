initial_lessons = input().split(', ')
command = input()


def print_lessons(a_list):
    for i in range(1, len(a_list) + 1):
        print(f"{i}.{a_list[i - 1]}")


while command != 'course start':
    command = command.split(':')
    current_command = command[0]
    lesson_title = command[1]
    if current_command == 'Add':
        if lesson_title not in initial_lessons:
            initial_lessons.append(lesson_title)
    elif current_command == "Insert":
        index = int(command[2])
        if lesson_title not in initial_lessons:
            initial_lessons.insert(index, lesson_title)
    elif current_command == "Remove":
        if lesson_title in initial_lessons:
            initial_lessons.remove(lesson_title)
            if f'{lesson_title}-Exercise' in initial_lessons:
                index = initial_lessons.index(f'{lesson_title}-Exercise')
                initial_lessons.pop(index)
    elif current_command == "Swap":
        swap_lesson = command[2]
        if lesson_title in initial_lessons and swap_lesson in initial_lessons:
            swap_lesson_index = initial_lessons.index(swap_lesson)
            lesson_title_index = initial_lessons.index(lesson_title)
            initial_lessons[swap_lesson_index], initial_lessons[lesson_title_index] = initial_lessons[
                                                                                          lesson_title_index], \
                                                                                      initial_lessons[swap_lesson_index]
            if f'{swap_lesson}-Exercise' in initial_lessons:
                initial_lessons.pop(initial_lessons.index(f'{swap_lesson}-Exercise'))
                initial_lessons.insert(lesson_title_index+1, f'{swap_lesson}-Exercise')
    elif current_command == "Exercise":
        if lesson_title in initial_lessons and f'{lesson_title}-Exercise' not in initial_lessons:
            index = initial_lessons.index(lesson_title) + 1
            initial_lessons.insert(index, f'{lesson_title}-Exercise')
        elif lesson_title not in initial_lessons:
            initial_lessons.append(lesson_title)
            initial_lessons.append(f'{lesson_title}-Exercise')
    command = input()
print_lessons(initial_lessons)
