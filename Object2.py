from collections import Counter
from urllib.parse import urlencode
import statistics

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


#fonction qui trouve les clés d'un objet ayant une valeur spécifique
def find_keys_by_value(d: dict, target) -> list:
    return [k for k, v in d.items() if v == target]

product_stock = {"laptop": 0, "mouse": 5, "keyboard": 0, "monitor": 3}
print(find_keys_by_value(product_stock, 0)) # ["laptop", "keyboard"]


#fonction qui crée un objet à partir de deux tableaux
def create_object_from_arrays(keys: list, values: list) -> dict:
    return dict(zip(keys, values))

player_names = ["Alice", "Bob", "Charlie"]
scores = [100, 85, 90]
print(create_object_from_arrays(player_names, scores)) # {"Alice": 100, "Bob": 85, "Charlie": 90}


#fonction qui compte les occurrences de valeurs dans un objet
def count_values(d: dict) -> dict:
    return dict(Counter(d.values()))

order_statuses = {
    "order1": "pending",
    "order2": "delivered",
    "order3": "pending",
    "order4": "cancelled",
    "order5": "pending"
}
print(count_values(order_statuses)) # {"pending": 3, "delivered": 1, "cancelled": 1}


#fonction qui extrait certaines propriétés d'un objet
def extract_properties(d: dict, keys: list) -> dict:
    return {k: d[k] for k in keys if k in d}

user_profile = {
    "name": "Jean Martin",
    "email": "jean@email.com",
    "password": "secret123",
    "age": 35,
    "address": "123 rue Principal"
}
public_info = ["name", "age"]
print(extract_properties(user_profile, public_info)) # {"name": "Jean Martin", "age": 35}


#fonction qui trie les propriétés d'un objet par valeur
def sort_object_by_value(d: dict) -> dict:
    return dict(sorted(d.items(), key=lambda x: x[1]))

player_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
print(sort_object_by_value(player_scores)) # {"Charlie": 78, "Alice": 85, "Bob": 92, "David": 95}


#fonction qui trouve la valeur maximale dans un objet de nombres
def find_max_value(d: dict) -> int:
    return max(d.values())

game_scores = {"level1": 850, "level2": 920, "level3": 880, "level4": 1020}
print(find_max_value(game_scores))  # 1020


#fonction qui créé un objet à partir d'un tableau de paires clé-valeur
def create_object_from_pairs(pairs: list) -> dict:
    return dict(pairs)

product_pairs = [["pommes", 2.5], ["bananes", 1.8], ["oranges", 2.2]]
print(create_object_from_pairs(product_pairs)) # {"pommes": 2.5, "bananes": 1.8, "oranges": 2.2}

#fonction qui recherche une valeur dans un objet imbriqué
def find_value_in_object(d: dict, target, path: list = []) -> list:
    for k, v in d.items():
        current_path = path + [k]
        if v == target:
            return current_path
        if isinstance(v, dict):
            result = find_value_in_object(v, target, current_path)
            if result:
                return result
    return []

config = {
    "app": {
        "name": "MonApp",
        "settings": {
            "theme": "dark",
            "notifications": {
                "email": True,
                "push": False
            }
        }
    }
}
print(find_value_in_object(config, "dark"))   # ["app", "settings", "theme"]


#fonction qui groupe les objets par une propriété spécifique
def group_by_property(items: list, key: str) -> dict:
    result = {}
    for item in items:
        result.setdefault(item[key], []).append(item)
    return result

students = [
    {"name": "Alice", "level": "Débutant"},
    {"name": "Bob", "level": "Intermédiaire"},
    {"name": "Charlie", "level": "Débutant"},
    {"name": "David", "level": "Avancé"}
]
print(group_by_property(students, "level")) # {"Débutant": [{"name": "Alice", ...}, {"name": "Charlie", ...}], ...}


#fonction qui vérifie si un objet correspond à un schéma spécifique
#ajout d'un dictionnaire de type pour compatibilité python
TYPE_MAP = {
    "string": str,
    "number": (int, float),
    "boolean": bool,
    "list": list,
    "dict": dict
}

def validate_object(obj: dict, schema: dict) -> bool:
    return all(
        k in obj and isinstance(obj[k], TYPE_MAP[v])
        for k, v in schema.items()
    )

user_schema = {
    "name": "string",
    "age": "number",
    "email": "string"
}
user_input = {
    "name": "Marie",
    "age": 25,
    "email": "marie@email.com"
}
print(validate_object(user_input, user_schema))  # True


#fonction qui compare les modifications entre deux objets
def compare_differences(old: dict, new: dict) -> dict:
    result = {}
    all_keys = old.keys() | new.keys()
    for k in all_keys:
        if k not in old:
            result[k] = {"type": "added", "new": new[k]}
        elif k not in new:
            result[k] = {"type": "removed", "old": old[k]}
        elif old[k] != new[k]:
            result[k] = {"type": "modified", "old": old[k], "new": new[k]}
    return result

old_profile = {
    "name": "Jean Dupont",
    "email": "jean@email.com",
    "age": 30
}
new_profile = {
    "name": "Jean Dupont",
    "email": "jean.dupont@email.com",
    "age": 31,
    "phone": "0123456789"
}
print(compare_differences(old_profile, new_profile)) # {"email": {"type": "modified", ...}, "age": {"type": "modified", ...}, "phone": {"type": "added", ...}}


#fonction qui convertit un objet en chaîne de paramètres d'URL
def object_to_url_params(d: dict) -> str:
    normalized = {k: str(v).lower() if isinstance(v, bool) else v for k, v in d.items()}
    return urlencode(normalized, quote_via=__import__('urllib.parse', fromlist=['quote']).quote)

search_params = {
    "query": "ordinateur portable",
    "maxPrice": 1000,
    "brand": "Dell",
    "inStock": True
}
print(object_to_url_params(search_params)) # query=ordinateur%20portable&maxPrice=1000&brand=Dell&inStock=true


#fonction qui génère un résumé statistique d'un objet contenant des nombres
def get_object_stats(d: dict) -> dict:
    values = list(d.values())
    n = len(values)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / n
    return {
        "basic": {
            "min": min(values),
            "max": max(values),
            "average": mean,
            "total": sum(values)
        },
        "advanced": {
            "median": statistics.median(values),
            "variance": variance,
            "standardDeviation": round(variance ** 0.5, 2)
        }
    }

monthly_revenues = {"january": 1000, "february": 1200, "march": 900, "april": 1500}
print(get_object_stats(monthly_revenues))
"""
{
 basic: {
   min: 900,
   max: 1500,
   average: 1150,
   total: 4600
 },
 advanced: {
   median: 1100,
   variance: 52500,
   standardDeviation: 229.13
 }
}
"""