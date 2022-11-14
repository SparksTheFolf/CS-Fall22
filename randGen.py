"""Nolan T. 11/14/2022 - Playing with functions, list, dictionaries and random numbers."""
from random import randint
from typing import List, Dict


# make a program that generates random numbers 1 to n, until all integers 1 to n have been generated at least once.

def new_random() -> int:
    """ returns a unique random number, one that has not been returned before."""


def back_to_back() -> (int, int):
    """ returns a tuple
         1st item is the integer that was generated back to back most often
         2nd item is the mac length of the series
    """


print("Creating all integers from 1 to n (inclusive) randomly.")
s = input("Please enter the upper boundary, n = ")
print(f"Creating a random sequence of all integers 1 .. {n} required {k} randint(1,{n}) calls")
print(f"The integer that was created last was {last}.")
print(f"The integer that was created the most times in a row, {how_often} times, was {most_often}.")
