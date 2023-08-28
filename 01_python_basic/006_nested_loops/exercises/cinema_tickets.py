student_ticket_counter = 0
kid_ticket_counter = 0
standard_ticket_counter = 0
total_ticket_counter = 0
command = input()

while command != "Finish":
    movie_name = command
    free_seats = int(input())
    sold_tickets = 0
    total_places = free_seats

    while free_seats > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_ticket_counter += 1
        elif ticket_type == "kid":
            kid_ticket_counter += 1
        elif ticket_type == "standard":
            standard_ticket_counter += 1
        free_seats -= 1
        sold_tickets += 1
        total_ticket_counter += 1
    percent_full_hall = sold_tickets/total_places * 100
    print(f"{movie_name} - {percent_full_hall:.2f}% full.")
    command = input()

percent_student_tickets = student_ticket_counter/total_ticket_counter * 100
percent_standard_tickets = standard_ticket_counter/total_ticket_counter * 100
percent_kid_tickets = kid_ticket_counter/total_ticket_counter * 100
print(f"Total tickets: {total_ticket_counter}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")


