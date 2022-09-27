"""
Author: Nolan T. (CS118 Fall Class)
Last Edited: 09/26/2022
Online Version Avail: https://s.wuffs.net/CS-Fall22

This program is designed to take the input of a prime number {prime} and determine if it is a Prime number {TRUE} or
not a prime number {FALSE}, then print the max values {max_value}.
"""

prm_number = []  # Adds the primed number to list
number = []  # Adds the main input number to list
repeat = 5  # Repeats the program 5 times

for x in range(repeat):
    print()  # Empty Line For Readability
    prime = int(input("Enter a possible prime number greater than 1: "))
    number.append(prime)
    if prime <= 1:
        print(prime, f"is not a prime number because it is less than 1")
    if prime > 1:
        for num in range(2, prime):
            if (prime % num) == 0:  # Prime Number Formula
                print(f"{prime} is not a prime number because it is devisable by {num}")
                break
        else:
            print(prime, f"is a prime number")
            prm_number.append(prime)

#  Bonus Points Section
if repeat >= 5:
    length_num = len(number)
    length_prm = len(prm_number)
    max_value = max(prm_number)
    print()  # Empty Line For Readability
    print(f"{length_num} of numbers were examined, {length_prm} of those were prime, "
          f" and the largest was {max_value}.")
