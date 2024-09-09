from django.db import models
from Tienda.models import Producto

# Create your models here.

class carrito(models.Model):
    id_carrito = models.CharField(max_length=250, blank=True)
    fecha_agregada = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id_carrito


class carritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(carrito, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.producto