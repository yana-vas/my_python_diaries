numbers = input().split(", ")


def palindrome(integers):
    is_palindrome = False
    first_half_digits = ''
    last_half_digits = ''
    for j in range(len(integers)):
        current_number = integers[j]
        if len(current_number) == 1:
            is_palindrome = True
        else:
            for i in range(len(current_number)//2):
                first_half_digits += current_number[i]
                last_half_digits += current_number[-(i+1)]
            if int(first_half_digits) == int(last_half_digits):
                is_palindrome = True
            else:
                is_palindrome = False
        print(is_palindrome)
        first_half_digits = ''
        last_half_digits = ''


palindrome(integers=numbers)
