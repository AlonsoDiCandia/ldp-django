# poblar_bd.py
import os, sys
import django
import json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/backend'
print(BASE_DIR)
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from logica.models import Tortuga

tortugas = Tortuga.objects.all()

for t in tortugas:
    print(f"{t.id} {t}")