"""Nolan T. 11/14/2022 - Playing with functions, list, dictionaries and random numbers."""
from random import randint
from typing import List, Dict

print("Creating all the integers from 1 to n (inclusive) randomly.")
n = int(input("Please enter the upper boundary, n = "))
randomlist = []
often = 0

"""Write a Python program that generates random numbers 1 to n (inclusive), until all integers 1 to n have been generated at least once."""


def new_random() -> int:
    """ returns a unique random number, one that has not been returned before. and adds it to the list"""
    random = randint(1, n)
    return randint(1, n)


while len(randomlist) < n:
    randomlist.append(new_random())


def last_number():
    """ returns the last number in the list"""
    return randomlist[-1]


def most_often() -> int:
    """return the most shown number in the list"""
    return max(randomlist, key=randomlist.count)


def how_often() -> int:
    """return the most shown number in the list"""
    return randomlist.count(most_often())


def back_to_back() -> (int, int):
    """ returns a tuple 1st item is the integer that was generated back to back most often 2nd item is the max length of the series """
    return most_often(), how_often()


k = len(randomlist)

print(f"Creating a random sequence of all integers 1 .. {n} required {k} randint(1,{n}) calls")
print(f"The integer that was created last was {last_number()}.")
print(f"The integer that was created the most times in a row, {how_often()} times, was {most_often()}.")
