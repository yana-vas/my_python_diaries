from colorama import Fore, Back, Style, init
import keyboard
import time

with open('book.txt', 'r', encoding='utf-8') as file:
    book_lines = file.readlines()

# Define the variables for line and character positions
line_number = 0
char_position = 0


def print_line(line):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0.007)


def on_enter(e):
    global line_number

    if line_number < len(book_lines):
        line = book_lines[line_number]
        if line_number == 10:
            print("Line 10")

        if line.endswith('?'):
            print(line + ' (question)')
        else:
            print_line(line)

        line_number += 1


# Add a hook for the 'enter' key
keyboard.on_press_key('enter', on_enter)

# Print the first character of the book
print(book_lines[line_number][char_position], end='', flush=True)

# Start a blocking event loop
keyboard.wait()

