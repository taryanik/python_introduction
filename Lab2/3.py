"""Zadanie 3 (3.py) Napisz skrypt działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć,
dzielić oraz obliczać potęgę. """

import sys

operation = int(input("""Jaką operację chcesz wykonać?
    1) dodawanie
    2) odejmowanie
    3) mnożenie
    4) dzielenie
    5) potęgowanie
Please enter the operation number: """))

firstValue = int(input("Enter the first argument: "))
secondValue = int(input("Enter the second argument: "))

allowedRange = range(1, 6)
if operation not in allowedRange:
    print("This operation doesn't exist.")
    exit()

if operation == 4 and secondValue == 0:
    print("It's impossible to divide by zero.")
    exit()


def calculate_using_old_version(operation, firstValue, secondValue):
    if operation == 1:
        return firstValue + secondValue
    elif operation == 2:
        return firstValue - secondValue
    elif operation == 3:
        return firstValue * secondValue
    elif operation == 4:
        return firstValue / secondValue
    elif operation == 5:
        return firstValue ** secondValue
    else:
        print(f"Unexpected error.")
        exit()


def calculate_using_new_version(operation, firstValue, secondValue):
    match operation:
        case 1:
            return firstValue + secondValue
        case 2:
            return firstValue - secondValue
        case 3:
            return firstValue * secondValue
        case 4:
            return firstValue / secondValue
        case 5:
            return firstValue ** secondValue
        case _:
            print(f"Unexpected error.")
            exit()


if sys.version_info[0] >= 3 and sys.version_info[1] >= 10:
    result = calculate_using_new_version(operation, firstValue, secondValue)
else:
    result = calculate_using_old_version(operation, firstValue, secondValue)

print(f"Result is: {result}")
