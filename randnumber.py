from random import randint
from typing import Type

print("Creating all the integers from 1 to n (inclusive) randomly.")
s = int(input("Please enter the upper boundary, n = "))
n = s
lst = []
num = {}


def new_random() -> Type[int]:
    if type() == int:
        p = int(n)
        p = randint(1, p)
        p.append(lst)
        return int
    elif type(n) == str:
        print("not ok")


def back_to_back() -> (int, int):
    """ returns a tuple
         1st item is the integer that was generated back to back most often
         2nd item is the mac length of the series
    """

print(f"Creating a random sequence of all integers 1 .. {n} required {k} randint(1,{n}) calls")
print(f"The integer that was created last was {last}.")
print(f"The integer that was created the most times in a row, {how_often} times, was {most_often}.")
