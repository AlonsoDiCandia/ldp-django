# poblar_bd.py
import os, sys
import django
import pandas as pd 
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/backend'
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

url = 'https://rickandmortyapi.com/api/location'

response = requests.get(url).json()

print(response)