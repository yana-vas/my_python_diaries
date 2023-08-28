command = input()
results = {}
submissions = {}
while command != "exam finished":
    command = command.split('-')
    username = command[0]
    if command[1] == 'banned':
        for k,v in results.items():
            for j,i in v.items():
                if j == username:
                    results[k][j] = 'banned'
        command = input()
        continue
    language, points = command[1], int(command[2])
    if language not in results.keys():
        results[language] = {}
        results[language][username] = points
    else:
        if username not in results[language]:
            results[language][username] = points
        else:
            if results[language][username] < points:
                results[language][username] = points
    if language not in submissions.keys():
        submissions[language] = 0
    submissions[language] += 1

    command = input()

print('Results: ')
for language, usernames in results.items():
    for username, points in usernames.items():
        if points != 'banned':
            print(f"{username} | {points}")
print("Submissions: ")
for language, submission in submissions.items():
    print(f"{language} - {submission} ")
