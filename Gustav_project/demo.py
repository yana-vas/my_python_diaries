import pyttsx3
import keyboard
import time

from PIL import Image


def speak(text):
    engine = pyttsx3.init()
    #  resets the TTS engine each time you want to speak a text, which might allow interrupting the previous speech when a new text comes in.

    engine.say(text)
    engine.runAndWait()


with open('book.txt', 'r', encoding='utf-8') as file:
    book_lines = file.readlines()

# Define the variables for line and character positions
line_number = 0
char_position = 0


def fancy(line):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0.07)


def on_enter(e):
    global line_number

    if line_number < len(book_lines):
        line = book_lines[line_number].strip()

        if line.endswith('?'):
            print(line + ' (question)')
        else:
            fancy(line)
        line_number += 1
    else:
        print("End of the book.txt.")
        keyboard.unhook_all()

    speak(line)

    if 'open image_0001' in line.lower():  # Check if the secret word is in the line
        try:
            image = Image.open(r'C:\Python\images\frozen.jpg')
            image.show()
        except Exception as e:
            print(e)


keyboard.on_press_key('enter', on_enter)
keyboard.wait('esc')
