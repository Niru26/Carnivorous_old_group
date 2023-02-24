# Homework 1 by N.Rudakov
# Task 2

initial_number = int(input("Enter number: "))
numbers_sum = 0

while (initial_number > 0):

    term = initial_number % 10
    initial_number //= 10
    numbers_sum += term

print(f"Result: {numbers_sum}")
