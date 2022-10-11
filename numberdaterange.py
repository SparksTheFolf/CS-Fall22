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

inputCustom = int(input("Please enter a number 1-7: "))
if inputCustom == 1:
    print("Monday")
elif inputCustom == 2:
    print("Tuesday")
elif inputCustom == 3:
    print("Wednesday")
elif inputCustom == 4:
    print("Friday")
elif inputCustom == 5:
    print("Saturday")
elif inputCustom == 6:
    print("Saturday")
elif inputCustom == 7:
    print("Sunday")
else:
    print("Invalid Input.")
