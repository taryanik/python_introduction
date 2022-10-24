"""Zadanie 1 (1.py) Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i obwód
oraz wyświetla wyniki na ekranie.

Zadanie 1_1 (1.py) Wykorzystaj f-stringi do wyświetlenia wyników (pole i obwód) z zadania 1."""

sideA = float(input('Enter the first side: '))
sideB = float(input('Enter the second side: '))

square = sideA * sideB
perimeter = 2 * (sideA + sideB)

print(f"The square of the rectangle {square}")
print(f"The perimeter of the rectangle {perimeter}")

