import random


rand_numbers = []

for elem in range(5):
    rand_numbers.append(random.randint(1,100))


print(f'Zufällige Zahlen {rand_numbers}')