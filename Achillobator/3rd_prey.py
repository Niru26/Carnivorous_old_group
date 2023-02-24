# Homework 1 by N.Rudakov
# Task 6

ticket_number = int(input("Enter 6 digits number: "))
trigger = True

while trigger:
    digit_length = len(str(ticket_number))
    if digit_length != 6:
        ticket_number = int(input("Enter 6 digits number: "))
    else:
        # right_part = ticket_number % 1000
        # left_part = ticket_number // 1000
        accamulator = 0
        right_part_sum = 0
        left_part_sum = 0
        counter = 0

        while ticket_number > 0:
            term = ticket_number % 10
            ticket_number //= 10
            right_part_sum += term
            counter += 1
            if counter == 3:
                accamulator = right_part_sum
                right_part_sum = 0
        left_part_sum = right_part_sum
        print(f"LP - {left_part_sum}, RP - {right_part_sum}")
        trigger = False
                
           