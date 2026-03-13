import re
import unicodedata

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
print(snake_to_camel("user_first_name"), '\n')

def vowel_occurrences(string: str) -> int:
    return sum(1 for c in string.lower() if c in "aeiouy")

print("fonction 7 nombre d'occurence des voyelles :")
print(vowel_occurrences("combien il y a t-il de voyelles dans cette phrase"), '\n')

def swap_case(string: str) -> str:
    return string.swapcase()

print("fonction 8 inversement des majuscule et minuscules :")
print(swap_case("Inversement Des Majuscules Et Minuscules"), '\n')

#à noter que cette fonction possède un problème de conception sur les mots possédant naturellement 2 lettres collées
def remove_consecutive_duplicates(string: str) -> str:
    return re.sub(r"(.)\1+", r"\1", string)

print("fonction 9 retire les caractères en double consécutifs :")
print(remove_consecutive_duplicates("Bonjouuuur !!! J'ai besoiiiin d'aide...."), '\n')

def extract_initials(full_name: str) -> str:
    return ".".join(re.findall(r"(?:^|(?<=[\s-]))\w", full_name.upper()))

print("fonction 10 extraction des initiales d'un nom complet :")
print(extract_initials("jean-pierre dupont"), '\n')

def mask_string(string: str, n: int) -> str:
    return re.sub(r".(?=.{" + str(n) + r"})", "*", string)

print("fonction 11 masquage des caractères jusqu'au N derniers :")
print(mask_string("1234567890123456", 4), '\n')

def is_palindrome(string: str) -> bool:
    normalized = unicodedata.normalize("NFD", string.lower())
    cleaned = re.sub(r"[^a-z]", "", normalized)
    return cleaned == cleaned[::-1]

print("fonction 12 Vérification palindrome :")
print(is_palindrome("Eh ! ça va la vache ?"), '\n')

def longest_sequence(string: str) -> str:
    matches = re.finditer(r"(.)\1*", string)
    return max(matches, key=lambda m: len(m.group())).group()

print("fonction 12 Recherche de la plus longue séquence de caractères identiques :")
print(longest_sequence("aaabbbbbcccc"), '\n')

def truncate(string: str, n: int) -> str:
    return string[:n - 3].rstrip() + "..." if len(string) > n else string

print("fonction 13 Tronque un string en laissant '...' :")
print(truncate("Ceci est une très longue description d'un produit", 20))