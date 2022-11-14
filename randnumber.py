from random import randint
from typing import Type

print("Creating all the integers from 1 to n (inclusive) randomly.")
n = int(input("Please enter the upper boundary, n = "))
randomlist = []
num = {}
often = 0


def new_random(x) -> int:
    """ returns a unique random number, one that has not been returned before."""
    while True:
        rand = randint(1, x)
        if rand not in randomlist:
            randomlist.append(rand)
            return rand


def back_to_back() -> (int, int):
    """ returns a tuple 1st item is the integer that was generated back to back most often 2nd item is the mac length of the series """
    for i in range(len(randomlist) - 1):
        if randomlist[i] == randomlist[i + 1]:
            if randomlist[i] not in num:
                num[randomlist[i]] = 1
            else:
                num[randomlist[i]] += 1
    return max(num, key=num.get), max(num.values())


last = randomlist[-1]
k = len(randomlist)

print(f"Creating a random sequence of all integers 1 .. {n} required {k} randint(1,{n}) calls")
print(f"The integer that was created last was {last}.")
print(f"The integer that was created the most times in a row, {how_often} times, was {most_often}.")
