from random import randint

from django.shortcuts import render
from django.http import JsonResponse

from logica.models import Persona, Tortuga

# Create your views here.

def primer_endpoint(request):
    body = {
        'mensaje': 'Hola mundo!'*5
    }

    return JsonResponse(body)

def get_personas(request):
    personas = Persona.objects.all()

    personas_list = []

    for p in personas:

        persona = {
            'nombre': p.nombre,
            'edad': p.edad,
            'casado': p.casado
        }

        personas_list.append(persona)

    # print(personas)

    body = {
        'personas': personas_list * 2
    }

    return JsonResponse(body)


def create_tortuga(request):
    velocidad = randint(0,100)
    fuerza = randint(0,100)
    nombre = f"Tortuga_{velocidad}_{fuerza}"

    tortuga, created = Tortuga.objects.get_or_create(
        nombre = nombre,
        velocidad = velocidad,
        fuerza = fuerza,
    )

    t = {
        "nombre": tortuga.nombre,
        "velocidad": tortuga.velocidad,
        "fuerza": tortuga.fuerza,
        "created": created
    }

    return JsonResponse(t)

def get_tortugas(request, velocidad, fuerza):
    tortugas_v = Tortuga.objects.filter(velocidad__gte=velocidad)
    tortugas_f = Tortuga.objects.filter(fuerza__gte=fuerza)

    tortugas = set(list(tortugas_v) + list(tortugas_f))

    tortugas_list = []

    for tortuga in tortugas:
        t = {
            "nombre": tortuga.nombre,
            "velocidad": tortuga.velocidad,
            "fuerza": tortuga.fuerza,
        }

        tortugas_list.append(t)
    

    return JsonResponse({
        "count": len(tortugas_list),
        "tortugas": tortugas_list
    })

def get_tortugas_by_id(request, id):
    tortugas = Tortuga.objects.filter(id=id)

    tortugas_list = []

    for tortuga in tortugas:
        t = {
            "id": tortuga.id,
            "nombre": tortuga.nombre,
            "velocidad": tortuga.velocidad,
            "fuerza": tortuga.fuerza,
        }

        tortugas_list.append(t)
    

    count = len(tortugas_list)
    return JsonResponse({
        "count": count,
        "tortugas": tortugas_list if count > 0 else "No hay tortuga con ese id."
    })




