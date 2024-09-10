from django.shortcuts import render, redirect
from Tienda.models import Producto
from .models import Carrito, carritoItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def _id_carrito(request):
    carrito = request.session.session_key
    if not carrito:
        carrito = request.session.create()
    return carrito

def agregar_carrito(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    try:
        carrito = Carrito.objects.get(id_carrito=_id_carrito(request)) # obtenga el carrito usando el id_carrito presente en la sesión
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(
            id_carrito = _id_carrito(request)
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
    return redirect('carrito')


def carrito(request, total=0, cantidad=0, carrito_item=None):
    try:
        carrito = Carrito.objects.get(id_carrito=_id_carrito(request))
        carrito_items = carritoItem.objects.filter(carrito=carrito, activo=True)
        for carrito_item in carrito_items:
            total += (carrito_item.producto.precio * carrito_item.cantidad)
            cantidad += carrito_item.cantidad
    except ObjectDoesNotExist:
        pass

    context = {
        'total' : total,
        'cantidad' : cantidad,
        'carrito_items' : carrito_items,
    }
    return render(request, "Tienda/carrito.html", context)