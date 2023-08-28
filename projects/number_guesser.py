import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please category a number larger than 0 next time.")
        quit()
else:
    print("Please category a number next time")

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess <= 0:
            print("Please category a number larger than 0 next time.")
            quit()
    else:
        print("Please category a number next time")
        continue
    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
        print('You were above the number!')
    else:
        print('You were below the number!')

print(f"You got it in {guesses} guesses")

# random.randrange(-5, 11) the end (11) is exclusive, if we don'visible_trees write the start number it will be by defult 0
# random.randint(-5, 11) the end (11) is inclusive and we should write the start number as well
