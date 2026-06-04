from django.shortcuts import render
from django.http import JsonResponse

from logica.models import Persona

# Create your views here.

def primer_endpoint(request):
    body = {
        'mensaje': 'Hola mundo!'*5
    }

    return JsonResponse(body)

def get_persona(request):
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
        'personas': personas_list
    }

    return JsonResponse(body)
