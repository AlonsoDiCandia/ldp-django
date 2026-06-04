from django.shortcuts import render
from django.http import JsonResponse

from logica.models import Persona

# Create your views here.

def primer_endpoint(request):
    body = {
        'mensaje': 'Hola mundo!'
    }

    return JsonResponse(body)

def get_persona(request):
    personas = Persona.objects.all().first()

    persona = {
        'nombre': personas.nombre,
        'edad': personas.edad,
        'casado': personas.casado
    }

    # print(personas)

    body = {
        'personas': [persona] * 8
    }

    return JsonResponse(body)
