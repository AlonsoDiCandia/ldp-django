from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    casado = models.BooleanField()

    def __str__(self):
        return self.nombre