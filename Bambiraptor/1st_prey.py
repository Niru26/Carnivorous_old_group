# Homework 2 by Rudakov N.
# Task 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
coins_array = [1, 1, 1, 0, 1]
total_coins = len(coins_array)
count_heads = 0

for i in range(total_coins):
    if coins_array[i] == 1:
        count_heads += 1
count_tails = total_coins - count_heads

found_less = f"Heads - {count_heads}" if count_heads < count_tails else f"Tails - {count_tails}"
print(found_less)
