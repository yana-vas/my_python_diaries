name = input('Type your name: ')
print(f'Welcome {name} to this adventure!')

answer = input('You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ').lower()

if answer == 'left':
    answer = input('You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim accross: ').lower()

    if answer == 'swim':
        print('You swam across and were eaten by an alligator.')
    elif answer == 'walk':
        print('YOu walked for many miles, ran out of water and you lost the game.')
    else:
        print('Not a valid option. You lose.')
elif answer == 'right':
    answer = input('You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ').lower()
    if answer == 'back':
        answer = input('You go back to the main road. Now you can decide to drive to the /left/ or to the /right/').lower()
        if answer == 'left':
            print('You get lost along the way and can\'visible_trees find your way back. You lose.')
        elif answer == 'right':
            print('The car stops working, you go out to check on it and you get bitten by a deadly snake. You lose')
    elif answer == 'cross':
        answer = input('You cross the bridge and meet a stranger. Do you talk to them (yes/no) ? ')

        if answer == 'yes':
            print('You talk to the strange and they give you gold. You WIN!')
        elif answer == 'no':
            print('You ignore the stranger and they are offended and you lose.')
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')
else:
    print('Not a valid option. You lose.')

print(f'Thank you for trying {name}!')