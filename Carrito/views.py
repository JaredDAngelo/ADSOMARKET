from django.shortcuts import render, redirect, get_object_or_404
from Tienda.models import Producto
from .models import Carrito, carritoItem
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


# Create your views here.

def _id_carrito(request):
    carrito = request.session.session_key
    if not carrito:
        carrito = request.session.create()
    return carrito

def agregar_carrito(request, id_producto):
    color = request.GET['color']
    size = request.GET['size']
    return HttpResponse(color + ' ' + size)
    exit()

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

def quitar_carrito(request, id_producto):
    carrito = Carrito.objects.get(id_carrito=_id_carrito(request))
    producto = get_object_or_404(Producto, id=id_producto)
    carrito_item = carritoItem.objects.get(producto=producto, carrito=carrito)
    if carrito_item.cantidad > 1:
        carrito_item.cantidad -= 1
        carrito_item.save()
    else:
        carrito_item.delete()
    return redirect('carrito')

def quitar_carrito_item(request, id_producto):
    carrito = Carrito.objects.get(id_carrito=_id_carrito(request))
    producto = get_object_or_404(Producto, id=id_producto)
    carrito_item = carritoItem.objects.get(producto=producto, carrito=carrito)
    carrito_item.delete()
    return redirect('carrito')

def carrito(request, total=0, cantidad=0, carrito_item=None):
    try:
        iva = 0
        grand_total = 0
        carrito = Carrito.objects.get(id_carrito=_id_carrito(request))
        carrito_items = carritoItem.objects.filter(carrito=carrito, activo=True)
        for carrito_item in carrito_items:
            total += (carrito_item.producto.precio * carrito_item.cantidad)
            cantidad += carrito_item.cantidad

        iva = int(0.19 * total)
        grand_total = int(total + iva)
        
    except ObjectDoesNotExist:
        pass

    context = {
        'total' : total,
        'cantidad' : cantidad,
        'carrito_items' : carrito_items,
        'iva'           : iva,
        'grand_total'   : grand_total,
    }
    return render(request, "Tienda/carrito.html", context)