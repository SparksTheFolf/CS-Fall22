"""Nolan T. 11/14/2022 - Playing with functions, list, dictionaries and random numbers."""
from random import randint
from typing import Tuple

print("Creating all the integers from 1 to n (inclusive) randomly.")
n = int(input("Please enter the upper boundary, n = "))
randomlist = []

"""Write a Python program that generates random numbers 1 to n (inclusive), until all integers 1 to n have been generated at least once."""


def random_generator() -> int:
    """ returns a random integer between 1 and n inclusive and then repeats until n is generated """
    while True:
        random_int = randint(1, n)
        randomlist.append(random_int)
        if random_int == n:
            break
    return random_int


def back_to_back() -> int:
    """ returns the number of times the random number generator was called """
    return len(randomlist)


def number_last() -> int:
    """ returns the last number generated """
    return randomlist[-1]


def how_often() -> int:
    """ returns the number of times the most common integer was generated """
    return max(randomlist.count(x) for x in randomlist)


def most_often() -> int:
    """ returns the most common integer """
    return max(set(randomlist), key=randomlist.count)


def main() -> None:
    """ main function """
    random_generator()
    print(f"Creating a random sequence of all integers 1 to {n} required {back_to_back()} randint(1,{n}) calls")
    print(f"The integer that was created last was {number_last()}.")
    print(f"The integer that was created the most times in a row, {how_often()} times, was {most_often()}.")
    print(f"Number of random integers generated: {len(randomlist)}")


if __name__ == "__main__":
    main()
