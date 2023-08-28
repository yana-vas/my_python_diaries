# sequence of integers, separated by space
distance_to_the_pokemons = list(map(int, input().split(' ')))
# captured pokemons
removed_elements = 0


def change_list_component(numbers_list, element):
    for ind in range(len(numbers_list)):
        if numbers_list[ind] <= element:
            numbers_list[ind] += element
        else:
            numbers_list[ind] -= element


while len(distance_to_the_pokemons) > 0:
    index = int(input())
    if 0 <= index < len(distance_to_the_pokemons):
        current_element = distance_to_the_pokemons[index]
        distance_to_the_pokemons.pop(index)
    elif index < 0:
        current_element = distance_to_the_pokemons[0]
        distance_to_the_pokemons[0] = distance_to_the_pokemons[-1]
    else:
        current_element = distance_to_the_pokemons[-1]
        distance_to_the_pokemons[-1] = distance_to_the_pokemons[0]
    removed_elements += current_element
    change_list_component(distance_to_the_pokemons, current_element)
print(removed_elements)
