from django.shortcuts import render
from .models import Producto

# Create your views here.

def Tienda(request):
    productos = Producto.objects.all().filter(esta_disponible=True)
    producto_contador = productos.count()

    context = {
        'productos': productos,
        'producto_contador': producto_contador,
    } 
    return render(request, 'Tienda/Tienda.html', context)
