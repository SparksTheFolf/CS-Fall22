"""

Count the amount of times you have to roll the dice depending on the number of rolls

"""
from random import randint
total = 0
count = 0
roll = randint(1, 6)
while count < 6:
    total += 1
    print(roll)
    if 6 == roll:
        count += 1
print(f"Rolled the dice {total} times to get six 10 times")
