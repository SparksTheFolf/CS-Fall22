from random import randint

print("Creating all the integers from 1 to n (inclusive) randomly.")

n = input("Please enter the upper boundary, n = ")


def new_random():
    if type(n) == int:
        p = int(n)
        print("ok")
    elif type(n) == str:
        print("not ok")


new_random()
