from django.db import models

# Create your models here.

class Trago(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    grados = models.IntegerField()

    def __str__(self):
        return self.nombre

class Detalle(models.Model):
    trago = models.ForeignKey(Trago, null=True, blank=True, on_delete=models.CASCADE)
    ingrediente = models.TextField()
    preparacion = models.TextField()

    def __str__(self):
        return self.ingrediente

class Bar(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre