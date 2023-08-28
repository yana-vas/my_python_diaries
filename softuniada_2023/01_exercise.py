n = int(input())

last_message = [1]
new_message = [1]
for i in range(n):
    new_message = [1]

    if len(last_message) > 1:
        for j in range(len(last_message)-1):
            new_message.append(last_message[j]+last_message[j+1])
    new_message.append(1)
    last_message = new_message

new_message = [str(num) for num in new_message]
print(' '.join(new_message))