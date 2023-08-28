command = input()
company_users = {}
while command != 'End':
    command = command.split(' -> ')
    company = command[0]
    user = command[1]
    if company not in company_users:
        company_users[company] = []
    if user not in company_users[company]:
        company_users[company].append(user)
    command = input()

for company, employees in company_users.items():
    print(company)
    for employee_id in employees:
        print(f"-- {employee_id}")
