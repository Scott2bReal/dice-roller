import random
from time import sleep

# Number of dice
while True:
    try:
        dice = int(input("number of dice to roll: "))
        break
    except ValueError:
        print("please supply an integer")
        continue

# Number of sides
while True:
    try:
        sides = int(input("number of sides: "))
        break
    except ValueError:
        print("please supply an integer")
        continue

# Bonus
while True:
    try:
        bonus = int(input("bonus: "))
        break
    except ValueError:
        print("please supply an integer")
        continue

sleep(.5)

# Calculate roll and print each individual for user
i = 0
total = 0
while i < dice:
    roll = random.randint(1,sides + 1)
    sleep(.5)
    print(f'Die {i + 1}: {roll}')
    sleep(.5)
    total = total + roll
    i += 1

total = total + bonus
sleep(.5)
print(f'Final result: {total}')