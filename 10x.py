data = "yay-yay ow-hay are-yay you-yay oing-day oday-tay"
hi = data.split()

for i in range(len(hi) - 1, -1, -1):
    print(hi[i], end="")


if "-yay" in data or "-ay" in data:
        print()
