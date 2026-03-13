import re

def character_count(string: str) -> str:
    return len(string.replace(' ', ''))

print("fonction 1 :")
print(character_count("Bonjour le monde !"),'\n')

def salutation(name: str) -> str:
    return "Bonjour " + re.sub(r"\w+", lambda m: m.group().capitalize(), name)

print("fonction 2 :")
print(salutation("jean-pierre"),'\n')