from django.db import models

# Create your models here.


class Pariente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=100)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.apellido)
