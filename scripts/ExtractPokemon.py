# poblar_bd.py
import os, sys
import django
import pandas as pd 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/backend'
print(BASE_DIR)
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from logica.models import Pokemon

Pokemon.objects.all().delete()

excel_pokemon = BASE_DIR + '/utils/pokemon/excel_pokemon_usm.xlsx'

pokemon_df = pd.read_excel(excel_pokemon)

id = 1
count = 0
while id != 151:
    print(pokemon_df.iloc[count]['Name'])

    name = pokemon_df.iloc[count]['Name']
    pokedex = pokemon_df.iloc[count]['#']
    tipo1 = pokemon_df.iloc[count]['Type 1']
    tipo2 = pokemon_df.iloc[count]['Type 2'] if pokemon_df.iloc[count]['Type 2'] is not None else ""
    hp = pokemon_df.iloc[count]['HP']
    attack = pokemon_df.iloc[count]['Attack']
    defense = pokemon_df.iloc[count]['Defense']


    pokemon, _ = Pokemon.objects.get_or_create(
        nombre_pokemon = name,
        num_pokedex = pokedex,
        tipo1 = tipo1,
        tipo2 = tipo2,
        hp = hp,
        ataque = attack,
        defensa = defense
    )

    id = pokedex
    count += 1

print("Importacion terminada")

for p in Pokemon.objects.all():
    print(p)




