from django.db import models
from django.urls import reverse

# Create your models here.

class Categorias(models.Model):
    nombre_categoria = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=255, blank=True)
    imagen = models.ImageField(upload_to='fotos/categorias', blank=True)

    #correcion de S en categorias
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


    def get_url(self):
        return reverse('productos_by_categoria', args=[self.slug])

    def __str__(self):
        return self.nombre_categoria
    

    
