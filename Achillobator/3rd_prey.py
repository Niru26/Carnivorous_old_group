# Homework 1 by N.Rudakov
# Task 6

ticket_number = int(input("Enter 6 digits number: "))
trigger = True

while trigger:
    if len(str(ticket_number)) != 6:
        ticket_number = int(input("Enter 6 digits number: "))
    else:
        right_part_sum = 0
        left_part_sum = 0
        total_sum = 0
        counter = 0

        while ticket_number > 0:
            term = ticket_number % 10
            ticket_number = ticket_number // 10
            total_sum += term
            counter += 1
            if counter == 3:
                right_part_sum = total_sum

        left_part_sum = total_sum - right_part_sum
        print(
            f"Total sum - {total_sum}, right part sum - {right_part_sum}. left part sum - {left_part_sum}")

        if right_part_sum == left_part_sum:
            print("This is lucky ticket")
        else:
            print("Bad luck")

        trigger = False
