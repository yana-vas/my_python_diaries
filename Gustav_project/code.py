def play_sound(sec):
    import time

    import vlc
    import sys

    vlc_path = r'C:\Program Files\VideoLAN\VLC'  # modify this path if your VLC is installed elsewhere
    if vlc_path not in sys.path:
        sys.path.append(vlc_path)

    sound_file = vlc.MediaPlayer(r"C:\Python\sam.mp3")
    sound_file.play()
    time.sleep(sec)


import keyboard
import time

with open('book.txt', 'r', encoding='utf-8') as file:
    book_lines = file.readlines()

# Define the variables for line and character positions
line_number = 0
char_position = 0


def fancy(line):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0.07)


# def on_enter(e):
#     global line_number
#
#     if line_number < len(book_lines):
#         line = book_lines[line_number]
#
#         if line.endswith('?'):
#             print(line + ' (question)')
#         else:
#             fancy(line)
#         line_number += 1

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
        print("End of the book.")
        keyboard.unhook_all()


# print(book_lines[line_number][char_position], end='', flush=True)  # Print the first character of the book

keyboard.on_press_key('enter', on_enter)
keyboard.wait('esc')  # end the loop when 'esc' is pressed
