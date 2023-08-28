movie_name = input()
days = int(input())
tickets_for_a_single_day = int(input())
price_for_a_single_ticket = float(input())
cinema_percent = int(input())

tickets_price = tickets_for_a_single_day * price_for_a_single_ticket * days
cinema_percent_money = tickets_price * cinema_percent / 100
profit_from_the_movie = tickets_price - cinema_percent_money
print(f"The profit from the movie {movie_name} is {profit_from_the_movie:.2f} lv.")
