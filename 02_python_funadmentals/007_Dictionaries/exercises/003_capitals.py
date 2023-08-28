countries = input().split(', ')
capitals = input().split(', ')

country_and_capital = {print(f"{countries[i]} -> {capitals[i]}") for i in range(len(countries))}