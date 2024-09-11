from .models import Carrito, carritoItem
from .views import _id_carrito

def counter(request):
    carrito_contador = 0
    if 'admin' in request.path:
        return{}
    else:
        try:
            carrito = Carrito.objects.filter(id_carrito=_id_carrito(request))
            carrito_items = carritoItem.objects.all().filter(carrito= carrito[:1])
            for carrito_item in carrito_items:
                carrito_contador += carrito_item.cantidad
        except Carrito.DoesNotExist:
            carrito_contador = 0
    return dict(carrito_contador=carrito_contador)