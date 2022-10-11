"""

Count the amount of times you have to roll the dice depending on the number of rolls

"""
from random import randint
total = 0
count = 0
while count < 6:
    total += 1
    if 6 == randint(1, 6):
        count += 1
print(f"Rolled the dice {total} times")
