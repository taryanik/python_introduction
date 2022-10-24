"""Zadanie 4 (4.py)
Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała."""

string = input('Enter the character(We check only the first character): ')

string = string.strip()
if len(string) < 1:
    print("Please enter at least one character")
    exit()

char = string[0]
if not char.isalpha():
    print("It is not a character")
    exit()

charCase = 'lowercase'
if char.isupper():
    charCase = 'uppercase'


print(f"You entered {charCase} character")
