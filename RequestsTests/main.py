"""
Kolorado backend test API
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    "Content-Type": "application/json", 
    "trainer_token": "4264fd12f64d7c645c5ac6ca86cf090c"
}

body = {
    "name": "БУБ",
    "photo": "https://dolnikov.ru/pokemons/albums/045.png"
}

response = requests.post(url = f'{URL}/pokemons', json = body, headers = HEADER, timeout = 5)
print(response.text)

idpok = response.json()["id"]

body = {
    "pokemon_id": idpok,
    "name": "АБОБА",
    "photo": "https://dolnikov.ru/pokemons/albums/054.png"
}


response = requests.put(url = f'{URL}/pokemons', json = body, headers = HEADER, timeout = 5)
print(response.text)

body = {
    "pokemon_id": idpok
}

response = requests.post(url = f'{URL}/trainers/add_pokeball', json = body, headers = HEADER, timeout = 5)
print(response.text)