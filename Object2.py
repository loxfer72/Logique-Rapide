#fonction qui récupère toutes les valeurs d'un objet en tableau
def get_values(d: dict) -> list:
    return list(d.values())

scores = {
    "level1": 100,
    "level2": 85,
    "level3": 95
}

print(get_values(scores)) # [100, 85, 95]