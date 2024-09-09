from django.shortcuts import render, get_object_or_404
from .models import Producto
from Categorias.models import Categorias

# Create your views here.

def Tienda(request, categoria_slug=None):
    categorias = None
    productos = None

    if categoria_slug != None:
        categorias = get_object_or_404(Categorias, slug=categoria_slug)
        productos = Producto.objects.filter(categoria=categorias, esta_disponible= True)
        producto_contador = productos.count()
    else:
        productos = Producto.objects.all().filter(esta_disponible=True)
        producto_contador = productos.count()

    context = {
        'productos': productos,
        'producto_contador': producto_contador,
    } 
    return render(request, 'Tienda/Tienda.html', context)

def producto_detalles(request, categoria_slug, producto_slug):
    return render(request, 'Tienda/producto_detalles.html')
