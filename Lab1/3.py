"""Zadanie 3 (3.py):
• Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
• Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
• Dla osób powyżej 18 roku życia bilet kosztuje 20zł.
Przykład: Wprowadź wiek klienta: 5
Cena biletu: 10zł"""

age = int(input('Enter the client age: '))

if age < 4:
    price = 0
elif age <= 18:
    price = 10
else:
    price = 20

print(f"Ticket price is {price} zl")
