#fonction qui récupère toutes les valeurs d'un objet en tableau
def get_values(d: dict) -> list:
    return list(d.values())

scores = {
    "level1": 100,
    "level2": 85,
    "level3": 95
}

print(get_values(scores)) # [100, 85, 95]


#fonction qui transforme les valeurs d'un objet
def transform_values(d: dict, func) -> dict:
    return {k: func(v) for k, v in d.items()}

prices_in_euros = {"book": 20, "pen": 5, "notebook": 10}
to_dollars = lambda euros: euros * 1.1
print(transform_values(prices_in_euros, to_dollars)) # {"book": 22.0, "pen": 5.5, "notebook": 11.0}