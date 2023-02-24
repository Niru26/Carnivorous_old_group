# Homework 1 by N.Rudakov
# Task 6

trigger = True

while trigger:
    ticket_number = int(input("Enter 6 digits number: "))
    if len(str(ticket_number)) < 6:
        ticket_number = int(input("Enter 6 digits number: "))
    else:
        right_part = ticket_number % 1000
        left_part = ticket_number // 1000
        right_part_sum = 0
        left_part_sum = 0
        devider = 1

        while right_part > 0:
            right_term = right_part % 10
            right_part //= 10
            right_part_sum += right_term
            left_term = left_part // (devider)
            left_part_sum += left_term
            print(f"LT - {left_term}, LT sum - {left_part_sum}")

        print(f"RP - {right_part_sum}, LP - {left_part_sum}")
        if right_part_sum == left_part_sum:
            print("This is lucky number")
        else:
            print("Bad luck")
    trigger = False
