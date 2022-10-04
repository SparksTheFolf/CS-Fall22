def run():
    number = int(input("Enter and numeric grade: "))
    if number > 89:
        letter = 'A'
    elif number > 79:
        letter = 'B'
    elif number > 69:
        letter = 'C'
    else:
        letter = 'D'
    print(f"The letter grade is {letter}")
    run()
