import re

def character_count(string: str) -> str:
    return len(string.replace(' ', ''))

print("fonction 1 longueur d'un string :")
print(character_count("Bonjour le monde !"),'\n')

def salutation(name: str) -> str:
    return "Bonjour " + re.sub(r"\w+", lambda m: m.group().capitalize(), name)

print("fonction 2 Salutation :")
print(salutation("jean-pierre"),'\n')

def ends_with_exclamation_mark(string: str) -> str:
    return True if re.search(r'!$', string) is not None else False

print("fonction 3 Vérification du ton :")
print(ends_with_exclamation_mark("Je suis très satisfait !"),'\n')


def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])

print("fonction 4 inversement de l'ordre des mots :")
print(reverse_words("Je mange une pomme"))