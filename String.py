import re

def character_count(string: str) -> str:
    return len(string.replace(' ', ''))

print("fonction 1 longueur d'un string :")
print(character_count("Bonjour le monde !"),'\n')

def salutation(name: str) -> str:
    return "Bonjour " + re.sub(r"\w+", lambda m: m.group().capitalize(), name)

print("fonction 2 Salutation :")
print(salutation("jean-pierre"),'\n')

def ends_with_exclamation_mark(string: str) -> bool:
    return True if re.search(r'!$', string) is not None else False

print("fonction 3 Vérification du ton :")
print(ends_with_exclamation_mark("Je suis très satisfait !"),'\n')


def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])

print("fonction 4 inversement de l'ordre des mots :")
print(reverse_words("Je mange une pomme"), '\n')


def letter_occurences(letter: str, string: str) -> int:
    return string.count(letter)

print("fonction 5 nombre d'occurence d'une lettre :")
print(letter_occurences("e","combien il y a t-il de fois la même lettre dans cette phrase"), '\n')

def snake_to_camel(string: str) -> str:
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])

print("fonction 6 format un string de snake_case à camelCase :")
print(snake_to_camel("user_first_name"))