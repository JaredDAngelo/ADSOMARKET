from django.shortcuts import render, redirect
from Tienda.models import Producto
from .models import Carrito, carritoItem
from django.http import HttpResponse

# Create your views here.

def id_carrito(request):
    carrito = request.session.session_key
    if not carrito:
        carrito = request.session.create()
    return carrito

def agregar_carrito(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    try:
        carrito = Carrito.objects.get(id_carrito=id_carrito(request)) # obtenga el carrito usando el id_carrito presente en la sesión
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(
            id_carrito = id_carrito(request),
        )
    carrito.save()

    try:
        carrito_item = carritoItem.objects.get(producto=producto, carrito=carrito)
        carrito_item.cantidad +=1
        carrito_item.save()
    except carritoItem.DoesNotExist:
        carrito_item = carritoItem.objects.create(
            producto = producto,
            cantidad = 1,
            carrito = carrito,
        )
        carrito_item.save() 
    return HttpResponse(carrito_item.producto) # tambien se le puede agregar la cantidad en vez del producto con carrito_item.cantidad
    exit()
    return redirect('carrito')

def carrito(request):
    return render(request, "Tienda/carrito.html",)