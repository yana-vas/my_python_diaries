import re
places = input()

destinations = []
pattern = r"([\/\=])([A-Z][a-zA-Z]{2,})\1"
matches = re.findall(pattern, places)
travel_points = 0
for match in matches:
    destinations.append(match[1])
    travel_points += len(match[1])
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")