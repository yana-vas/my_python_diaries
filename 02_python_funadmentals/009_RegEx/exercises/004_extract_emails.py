import re
input_data = input()
pattern = r"(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@([a-z\-])+(\.[a-z]+)+)\b"
match = re.findall(pattern, input_data)
[print(email[0]) for email in match]