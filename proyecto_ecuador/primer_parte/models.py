from django.db import models

class PlatoTipico(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    region = models.CharField(max_length=100)
    precio_estimado = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre + " - "+ " $"+ str(self.precio_estimado) 