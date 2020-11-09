from django.db import models

# Create your models here.
class Trago(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    grados = models.IntegerField()

    def __str__(self):
        return self.nombre

class Miembro(models.Model):
    trago = models.ForeignKey(Trago, null=True, blank=True, on_delete=models.CASCADE)
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

