"""Zadanie 4 (4.py). Napisz skrypt, która zamienia wprowadzoną literę na przeciwną (co do wielkości) i wypisuje
ją na ekranie."""

string = input('Enter a letter to change its case(We check only the first character): ')

string = string.strip()
if len(string) < 1:
    print("Please enter at least one character")
    exit()

char = string[0]
if not char.isalpha():
    print("It is not a character")
    exit()

if char.isupper():
    changedChar = char.lower()
else:
    changedChar = char.upper()

print(f"We changed your letter from {char} to {changedChar}")
