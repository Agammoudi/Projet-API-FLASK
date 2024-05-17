# import requests

# swapi_data = requests.get('https://swapi.dev/api/starships/9/');
 
# print(swapi_data)
 
# print(swapi_data.json()['name']);

# from flask import Flask
# import requests

# app = Flask(__name__)

# @app.route("/mon_api/<prenom>")
# def search_pokemon(prenom):
#     v= requests.get('https://swapi.dev/api/starships/9/')
#     json = v.json()
#     try :
#         p_prenom = json["prenom"]
#         return "true"
#     except:
#         return "false"



# app.run(debug=True)


from flask import Flask

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/find/<univers>/<id>")
def find(univers, id):
    if univers == "sw":
        result = recherche_star_wars(id)
        return jsonify(result)
    elif univers == "pk":
        result = recherche_pokemon(id)
        return jsonify(result)
    else:
        return "Univers not found"

def recherche_star_wars(id):
   
    pass

def recherche_pokemon(id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        return {"error": "Pokémon not found"}

if __name__ == "__main__":
    app.run(debug=True)
