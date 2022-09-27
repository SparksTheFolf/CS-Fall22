"""
Author: Nolan T. (CS118 Class)
Online Version Avail: https://wuffs.net/CS-Fall22

This program is designed to take the input of an octahedron angle (edge length) and calculate the "Algorithm" of the
    Volume form and the surface area form and print the "f-strings" values
"""

from math import sqrt
import sys


# main runtime method
def main():
    length = input("Input Edge Length: ")

    int_length = float(length)

    volume_form = round(sqrt(2) / 3 * int_length ** 3)

    surface_area_form = round(2 * sqrt(3) * int_length ** 2)

    # Print All
    print(
        f"A octahedro edge length of {int_length} has a volume of {volume_form} and a surface area of {surface_area_form}")

    sys.exit()


if __name__ == "__main__":
    main()
