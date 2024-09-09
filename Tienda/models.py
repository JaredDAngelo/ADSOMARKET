from django.db import models
from Categorias.models import Categorias
from django.urls import reverse

# Create your models here.
class Producto(models.Model):
    producto_nombre      = models.CharField(max_length=200, unique=True)
    slug                 = models.SlugField(max_length=200, unique=True)
    descripcion          = models.TextField(max_length=500, blank=True)
    precio               = models.IntegerField()
    Imagen               = models.ImageField(upload_to='fotos/productos')
    stock                = models.IntegerField()
    esta_disponible      = models.BooleanField(default=True)
    categoria            = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    crear_fecha          = models.DateTimeField(auto_now_add=True)
    modificar_fecha      = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('producto_detalles', args=[self.categoria.slug, self.slug])

    def __str__(self):
        return self.producto_nombre
    




