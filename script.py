import requests
pikachu_data = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu');
 
print(pikachu_data)
 
print(pikachu_data.json()['name']);


import requests

def comparer_force(pokemon1, pokemon2):
    force_pokemon1 = len(pokemon1["abilities"])
    force_pokemon2 = len(pokemon2["abilities"])

    if force_pokemon1 > force_pokemon2:
        return "{} est plus fort que {} avec {} capacités contre {} capacités".format(pokemon1["name"], pokemon2["name"], force_pokemon1, force_pokemon2)
    elif force_pokemon2 > force_pokemon1:
        return "{} est plus fort que {} avec {} capacités contre {} capacités".format(pokemon2["name"], pokemon1["name"], force_pokemon2, force_pokemon1)
    else:
        return "Les deux Pokémon ont la même force avec {} capacités chacun".format(force_pokemon1)

# Récupérer les données de Pikachu
pikachu_response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
pikachu_data = pikachu_response.json()

# Créer un dictionnaire à partir des données de Pikachu
pikachu_dict = {
    "name": pikachu_data["name"],
    "abilities": [ability["ability"]["name"] for ability in pikachu_data["abilities"]]
}

# Exemple d'utilisation :
bulbasaur = {
    "name": "Bulbasaur",
    "abilities": ["Overgrow", "Chlorophyll"]
}

resultat = comparer_force(bulbasaur, pikachu_dict)
print(resultat)

