# Homework 2 by Rudakov N.
# Task 14

limit = int(input())

for i in range(limit):
    power_2 = 2**i
    if power_2 > limit:
        break
    print(power_2, end=' ')
