from django.shortcuts import render
from Tienda.models import Producto

def home(request):
    productos = Producto.objects.all().filter(esta_disponible=True)

    context = {
        'productos': productos,
    } 
    return render(request, "home.html", context)