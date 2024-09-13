from django.shortcuts import render, get_object_or_404
from .models import Producto
from Categorias.models import Categorias
from Carrito.models import carritoItem
from django.http import HttpResponse
from django.db.models import Q

from Carrito.views import _id_carrito
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.

def Tienda(request, categoria_slug=None):
    categorias = None
    productos = None

    if categoria_slug != None:
        categorias = get_object_or_404(Categorias, slug=categoria_slug)
        productos = Producto.objects.filter(categoria=categorias, esta_disponible= True)
        paginator = Paginator(productos, 6)
        page = request.GET.get("page")
        paged_producto = paginator.get_page(page)
        producto_contador = productos.count()
    else:
        productos = Producto.objects.all().filter(esta_disponible=True).order_by('id')
        paginator = Paginator(productos, 3)
        page = request.GET.get("page")
        paged_producto = paginator.get_page(page)
        producto_contador = productos.count()

    context = {
        'productos': paged_producto,
        'producto_contador': producto_contador,
    } 
    return render(request, 'Tienda/Tienda.html', context)

def producto_detalles(request, categoria_slug, producto_slug):
    try:
        producto_individual= Producto.objects.get(categoria__slug=categoria_slug , slug=producto_slug)
        en_carrito = carritoItem.objects.filter(carrito__id_carrito=_id_carrito(request), producto=producto_individual).exists()



    except Exception as e:
        raise e 
    
    context ={
        'producto_individual': producto_individual,
        'en_carrito'         : en_carrito,
    }
    return render(request, 'Tienda/producto_detalles.html', context)


def buscar(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            productos = Producto.objects.order_by('-crear_fecha').filter(Q(descripcion__icontains=keyword) | Q(producto_nombre__icontains=keyword))
            producto_contador = productos.count()
    context = {
        'productos': productos,
        'producto_contador': producto_contador,
    }
    return render(request, 'Tienda/Tienda.html', context)
