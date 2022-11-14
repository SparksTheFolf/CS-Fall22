"""
Author: Nolan T. (CS118 Fall Class)
Last Edited: 11/14/2022
Online Version Avail: https://github.com/SparksTheFolf/CS-Fall22
This program will generate a random number between 1 and n and then repeat until n number of times is generated.
Then it will print the number of times the random number generator was called, the last number generated, the number of times
the most common integer was generated, and the most common integer.
"""

from random import randint

print("Creating all the integers from 1 to n (inclusive) randomly.")
n = input("Please enter the upper boundary, n = ")
randomlist = []


if not n.isdigit():
    print("Please enter a valid number.")
    exit()

n = int(n)


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


def how_often() -> int:
    """ returns the number of times the most common integer was generated """
    return max(randomlist.count(x) for x in randomlist)


def most_often() -> int:
    """ returns the most common integer """
    return max(set(randomlist), key=randomlist.count)


def number_last() -> int:
    """ returns the last number generated from the how_often function """
    return randomlist[-1]


def main() -> None:
    """ main function """
    random_generator()
    print(f"Creating a random sequence of all integers 1 to {n} required {back_to_back()} randint(1,{n}) calls")
    print(f"The integer that was created last was {number_last()}.")
    print(f"The integer that was created the most times in a row, {how_often()} times, was {most_often()}.")
    print(f"Number of random integers generated: {len(randomlist)}")


if __name__ == "__main__":
    main()
