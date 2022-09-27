"""
Author: Nolan T. (CS118 Fall Class)
Last Edited: 09/26/2022
Online Version Avail: https://s.wuffs.net/CS-Fall22

This program is designed to take the input of a {prime} prime number and determine if it is a Prime number {TRUE} or
not a prime number {FALSE}.
"""
prm_number = []
number = []
repeat = 5

for x in range(repeat):
    print()  # Empty Line For Readability
    prime = int(input("Enter a possible prime number greater than 1: "))
    number.append(prime)
    #    def main():
    if prime <= 1:
        print(prime, f"is not a prime number because it is less than 1")
    if prime > 1:
        for num in range(2, prime):
            if (prime % num) == 0:
                print(prime, f"is not a prime number because it is devisable by {num}")
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
