import requests

url = 'https://api.pokemonbattle.ru/v2'
token = '2eb381c48b291478d1f68dc764bc4c25'
header = {'Content-Type': 'application/json', 'trainer_token': token}

body_create = {
    "name": "Булка",
    "photo_id": 15
}

response_create = requests.post(url = f'{url}/pokemons', headers = header, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']

body_change = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}

response_change = requests.put(url = f'{url}/pokemons', headers = header, json = body_change)
print(response_change.text)

body_catch = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = body_catch)
print(response_catch.text)
