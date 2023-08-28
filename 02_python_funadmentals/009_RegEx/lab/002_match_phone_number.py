import re
input_data = input()
regex = "\\+359 2 \\d{3} \\d{4}|\\+359-2-\\d{3}-\\d{4}"
phone_numbers = re.findall(regex, input_data)
print(", ".join(phone_numbers))
