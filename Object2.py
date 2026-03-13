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


#fonction fusion deux objets
def merge_objects(d1: dict, d2: dict) -> dict:
    return {k: d1.get(k, 0) + d2.get(k, 0) for k in list(d1) + [k for k in d2 if k not in d1]}

store1_sales = {"january": 1000, "february": 1200, "march": 900}
store2_sales = {"january": 800, "february": 950, "march": 1100}
print(merge_objects(store1_sales, store2_sales)) # {"january": 1800, "february": 2150, "march": 2000}


#fonction qui filtre un objet selon une condition sur les valeurs
def filter_object(d: dict, func) -> dict:
    return {k: v for k, v in d.items() if func(v)}

inventory = {"laptop": 0, "smartphone": 5, "tablet": 0, "headphones": 8}
print(filter_object(inventory, lambda stock: stock == 0)) # {"laptop": 0, "tablet": 0}


#fonction qui convertit un objet plat en objet imbriqué en utilisant les points comme séparateurs
def flat_to_nested(d: dict) -> dict:
    result = {}
    for key, value in d.items():
        parent, child = key.split(".", 1)
        result.setdefault(parent, {})[child] = value
    return result

flat_config = {
    'app.name': 'MyApp',
    'app.version': '1.0.0',
    'database.host': 'localhost',
    'database.port': 5432
}
print(flat_to_nested(flat_config)) # {'app': {'name': 'MyApp', 'version': '1.0.0'}, 'database': {'host': 'localhost', 'port': 5432}}