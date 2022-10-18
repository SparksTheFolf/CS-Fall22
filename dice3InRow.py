"""

Count the amount of times you have to roll the dice depending on the number of rolls to get 3 times in a row

"""
from random import randint

total = 0
count = 0
roll = randint(1, 6)
while True:
    for _ in range(3):
        total += 1
        if 6 != roll:
            break
    else:
        break
print(f"Rolled the dice {total} times to get six 3 times in a row")
