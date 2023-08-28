numbers = input()
list_with_numbers = numbers.split(" ")  # The split(" ") function is a string method that splits the string into a list of substrings whenever it encounters a space (" ")
flipped_numbers = list()  # store the negated numbers
for digit in list_with_numbers:
    flipped_digit = -1 * int(digit)
    flipped_numbers.append(int(flipped_digit))
print(flipped_numbers)