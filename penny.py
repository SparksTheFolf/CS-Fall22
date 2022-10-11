"""

Figure out the final pay-stub amount

"""

inputCustomDays = int(input(f"Please enter the number of days you have worked: "))
total = 0
for d in range(0, inputCustomDays):
    payBase = pow(2, d)
    total += payBase
    print(f"{d+1} : {payBase}")
print(f"Your total pay is {total}")
