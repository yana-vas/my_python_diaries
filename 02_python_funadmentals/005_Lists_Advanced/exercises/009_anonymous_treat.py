def merge(def_list: list, start: int, end: int, negative=False):
    """
    The negative parameter is needed in order for the function to work correctly while mutating the input.
    Note: Using merge in the divide function has to be with a negative index, hence negative = True
    """

    # Defining start index
    if start < 0 and not negative:
        start = 0

    # Defining end index
    if end > len(def_list):
        end = len(def_list)

    # Items to merge
    items_to_merge = ''.join(def_list[start:end + 1])
    def_list[start:end + 1] = [items_to_merge]
    return def_list


def divide(def_list: list, index: int, partitions: int):
    # Getting the item to divide and the subitems per part - as per description always in the array
    item_to_divide = def_list[index]
    item_length = len(item_to_divide)
    subitems_per_part = item_length // partitions
    subitems_per_part = 1 if subitems_per_part == 0 else subitems_per_part

    # Creating a list with the new subitems:
    subitems_list = []
    for i in range(0, item_length, subitems_per_part):
        subitem = item_to_divide[i:i + subitems_per_part]
        subitems_list.append(subitem)

    # Finding out if subitems list is too long and merging the last items
    if len(subitems_list) > partitions:
        len_difference = abs(len(subitems_list) - partitions) + 1
        subitems_list = merge(subitems_list, -len_difference, len(subitems_list), negative=True)

    # Replace desired elements with divided subitems and return
    def_list.pop(index)
    for item in range(len(subitems_list)):
        def_list.insert(index + item, subitems_list[item])

    return def_list


def run():
    # Getting the input and executing the program
    string = input().strip().split(' ')

    while True:
        command = input().strip().split(' ')

        # Get commands and execute functions
        if command[0] == '3:1':
            break
        elif command[0] == 'merge':
            string = merge(string, int(command[1]), int(command[2]))
        elif command[0] == 'divide':
            string = divide(string, int(command[1]), int(command[2]))

    print(' '.join(string))


if __name__ == '__main__':
    run()
