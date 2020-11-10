from django.db import models

# Create your models here.
class Trago(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    grados = models.IntegerField()

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    trago = models.ForeignKey(Trago, null=True, blank=True, on_delete=models.CASCADE)
    IngredientePrincipal = models.CharField(max_length=50)
    IngredienteSecundario = models.CharField(max_length=50)
    IngredienteTerciario = models.CharField(max_length=50)
    Preparacion = models.TextField()
    Decoracion = models.CharField(max_length=100)

    def __str__(self):
        return self.IngredientePrincipal 

