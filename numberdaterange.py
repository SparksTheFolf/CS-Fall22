"""
Nolan T.
number to week days week converter

Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7

"""

lst = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
inputCustom = input("Please enter a number 1-7: ")
if inputCustom.isnumeric():
    num = int(inputCustom)
    if num in range(1,8):
        print(lst[num-1])
    else:
        print("Invalid entry")
else:
    print("input not numeric.")
