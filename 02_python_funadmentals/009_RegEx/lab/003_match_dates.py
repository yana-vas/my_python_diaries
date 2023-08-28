import re
input_dates = input()
regex = "\\b(\\d{2})([-.\\/])([A-Z][a-z]{2})\\2(\\d{4})\\b"
valid_dates = re.findall(regex, input_dates)
for date in valid_dates:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")
