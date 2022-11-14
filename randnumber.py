from random import randint
from typing import Type

print("Creating all the integers from 1 to n (inclusive) randomly.")
n = int(input("Please enter the upper boundary, n = "))
lst = []
num = {}


def new_random(x) -> int:
    """ returns a unique random number, one that has not been returned before."""
    while True:
        r = randint(1, n)
        if r not in lst:
            lst.append(r)
            return r


def back_to_back() -> (int, int):
    """ returns a tuple 1st item is the integer that was generated back to back most often 2nd item is the mac length of the series """
    for i in lst:
        if i not in num:
            num[i] = 1
        else:
            num[i] += 1
    max_num = max(num.values())
    for key, value in num.items():
        if value == max_num:
            return key, max_num


last = lst[-1]

print(f"Creating a random sequence of all integers 1 .. {n} required {k} randint(1,{n}) calls")
print(f"The integer that was created last was {last}.")
print(f"The integer that was created the most times in a row, {how_often} times, was {most_often}.")
