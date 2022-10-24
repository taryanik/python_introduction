"""Zadanie 2 (2.py) Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie
spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu paliwa oraz o szacowanych
kosztach podróży (cena paliwa 6.5 zł/l).
Zadanie 2_2 (2.py) Zmodyfikuj skrypt tak, aby długość przejechanej drogi była generowana losowo (liczba
całkowita z zakresu <1, 1000>)."""

import random

distance = float(input('Enter the distance: '))
consumption = float(input('Enter the fuel consumption(l/km): '))

consumedFuel = (distance / 100) * consumption
tripCost = consumedFuel * 6.5

print(f"Consumed {consumedFuel} liters of fuel.")
print(f"The trip cost is {tripCost} zl.")


# Zadanie 2_2
print('\n', 'Zadanie 2_2')

distance = random.randint(1, 1000)
consumedFuel = (distance / 100) * consumption
tripCost = consumedFuel * 6.5

print(f"Consumed {consumedFuel} liters of fuel.")
print(f"The trip cost is {tripCost} zl.")
