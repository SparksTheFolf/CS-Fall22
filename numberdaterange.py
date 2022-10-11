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

inputCustom = input("Please enter a number 1-7: ")
if inputCustom.isnumeric():
    num = int(inputCustom)
    if num == 1:
        print("Monday")
    elif num == 2:
        print("Tuesday")
    elif num == 3:
        print("Wednesday")
    elif num == 4:
        print("Friday")
    elif num == 5:
        print("Saturday")
    elif num == 6:
        print("Saturday")
    elif num == 7:
        print("Sunday")
    else:
        print("Invalid Input.")
else:
    print("BRUH")
