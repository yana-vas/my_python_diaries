def take_odd(text):
    new_text = ''
    for i in range(len(text)):
        if i % 2 != 0:
            new_text += text[i]
    text = new_text
    return text


text = input()
command = input()
while command != "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        text = take_odd(text)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        text = ''.join([text[i] for i in range(len(text)) if i < index or i >= index + length])
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in text:
            text = text.replace(substring, substitute)
        else:
            print("Nothing to replace!")
            command = input()
            continue
    print(text)
    command = input()
print(f"Your password is: {text}")
