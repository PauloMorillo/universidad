from django.db import models


class Curso(models.Model):
    name = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField()
    maximo_participantes = models.IntegerField()

    def __str__(self):
        return f'{self.name} max: {self.maximo_participantes}'
