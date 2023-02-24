# Homework 1 by N.Rudakov
# Task 4

total = int(input("Enter paper cranes quantity: "))
flag = True

while flag:
    if total % 6 != 0:
        print("Wrong data, pls.enter again")
        total = int(input("Enter paper cranes quantity: "))
    else:
        Peter = total // 6
        Sergei = total // 6
        Kate = (total // 3) * 2
        print(f"Peter - {Peter}, Sergei - {Sergei}, Kate - {Kate}")
        flag = False
