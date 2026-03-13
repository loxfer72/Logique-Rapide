import re

def character_count(string: str) -> str:
    return len(string.replace(' ', ''))

print("fonction 1 :")
print(character_count("Bonjour le monde !"),'\n')

def salutation(name: str) -> str:
    return "Bonjour " + re.sub(r"\w+", lambda m: m.group().capitalize(), name)

print("fonction 2 :")
print(salutation("jean-pierre"),'\n')

def ends_with_exclamation_mark(string: str) -> str:
    return True if re.search(r'!$', string) is not None else False

print("fonction 3 :")
print(ends_with_exclamation_mark("Je suis très satisfait !"),'\n')