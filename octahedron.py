#Copyright (c) (Nolan T.) 2022 ~ MIT Public Licence (Current Valid Licence is available at: http://wuffs.net/Licence )
#.Interactive Python Notebook version available at: https://wuffs.net/CS-Fall22
#.Py File Last Modified: 9/13/2022
#!!No external PIP repos needing to be imported!!



                                ## WHAT THIS PROGRAM IS ABOUT ##
#! This program is designed to take the input of an octahedron angle (edge length) and calculate the "Algorithm" of the
#    volume form and the surface area form and print the "f-strings" values


##Start of Code##
from math import sqrt

#Constants
vertices = 6
faces = 8
edges = 12


#main runtime method
def main():
    length = input("Input Edge Length: ")

    int_length = float(length)

    volume_form = float(sqrt(2) / 3 * int_length ** 3)

    surface_area_form = float((2 * sqrt(3) * int_length  ** 2))

#Print All
    print(f"Volume Output: {volume_form}")
    print('\n')
    print(f"Surface Area Output: {surface_area_form}")

#TODO ~~ Only Run Main method once all errors are gone  ~~
if __name__ == "__main__":
    main()
