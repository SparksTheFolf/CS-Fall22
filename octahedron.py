from math import sqrt

#Constants
vertices = 6
faces = 8
edges = 12


#main runtime method
def main():
    length = input("Input Edge Length: ")

    int_length = float(length)

    volume_form = float(sqrt(2)/3*(int_length^3))

    surface_area_form = float((2 * sqrt(3) * int_length ^ 2))

    float_vol = float(volume_form)
    float_area = float(surface_area_form)

#Print All
    print(f"Volume Output: {float_vol} ")
    print('\n')
    print(f"Surface Area Output: {float_area}")

#TODO ~~ Only Run Main method once all errors are gone  ~~
if __name__ == "__main__":
    main()



#Copyright (c) SparksTheFolf 2022 ~ MIT Public GNU Licence