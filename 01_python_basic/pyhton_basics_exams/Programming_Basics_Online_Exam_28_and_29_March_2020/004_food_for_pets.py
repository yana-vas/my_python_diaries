days = int(input())
food_quantity = float(input())
biscuits = 0
cat_food_counter = 0
dog_food_counter = 0
for i in range(1, days+1):
    dog_food = float(input())
    cat_food = float(input())
    if i % 3 == 0:
        biscuits += 10 * (cat_food + dog_food)/100
    cat_food_counter += cat_food
    dog_food_counter += dog_food

print(f"Total eaten biscuits: {round(biscuits)}gr.")
percent_eaten_food = (dog_food_counter + cat_food_counter) / food_quantity * 100
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
percent_dog_eaten_food = dog_food_counter / (dog_food_counter + cat_food_counter) * 100
print(f"{percent_dog_eaten_food:.2f}% eaten from the dog.")
percent_cat_eaten_food = cat_food_counter / (dog_food_counter + cat_food_counter) * 100
print(f"{percent_cat_eaten_food:.2f}% eaten from the cat.")


