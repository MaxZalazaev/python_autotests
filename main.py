import requests

host_name = 'https://api.pokemonbattle.me/v2'
trainer_token = 'af69ef36d4fd0a379601a30ea832e051'
trainer_id = 2369

response = requests.post(
    url = host_name + '/pokemons',
    headers = {'Content-Type': 'application/json',
               'trainer_token': trainer_token},
    json = {"name": "Максозавр",
            "photo": "https://dolnikov.ru/pokemons/albums/001.png"}
)
print ('Создан покемон: ', response.json())

pokemon_id = response.json()["id"]

response = requests.put(
    url = host_name + '/pokemons',
    headers = {'Content-Type': 'application/json',
               'trainer_token': trainer_token},
    json = {
            "pokemon_id": pokemon_id,
            "name": "Максонелло",
            "photo": "https://dolnikov.ru/pokemons/albums/001.png"
            }
)
print ('Заменили имя на Максонелло: ', response.json())

response = requests.post(
    url = host_name + '/trainers/add_pokeball',
    headers = {'Content-Type': 'application/json',
               'trainer_token': trainer_token},
    json = {
            "pokemon_id": pokemon_id,
            }
)
print(f"Покемон {pokemon_id} пойман в покебол: {response.json()}")

