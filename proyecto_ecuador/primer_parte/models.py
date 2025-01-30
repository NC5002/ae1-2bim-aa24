from django.db import models
from django.core.exceptions import ValidationError

class PlatoTipico(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    region = models.CharField(max_length=100)
    precio_estimado = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre + " - "+ " $"+ str(self.precio_estimado) 
    
    def clean(self):
        # Asegurarse de que el precio sea positivo
        if self.precio_estimado < 0:
            raise ValidationError("El precio estimado debe ser un número positivo.") 