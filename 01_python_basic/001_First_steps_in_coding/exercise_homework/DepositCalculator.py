deposit = float(input())
term_deposit = int(input())
annual_interest_rate = float(input())

interest = deposit * (annual_interest_rate / 100)
interest_month = interest / 12
sum = deposit + term_deposit * interest_month
print(sum)
