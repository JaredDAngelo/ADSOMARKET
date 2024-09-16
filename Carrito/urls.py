from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito, name='carrito'),
    path('agregar_carrito/<int:id_producto>/', views.agregar_carrito, name='agregar_carrito'),
    path('quitar_carrito/<int:id_producto>/', views.quitar_carrito, name='quitar_carrito'),
    path('quitar_carrito_item/<int:id_producto>/', views.quitar_carrito_item, name='quitar_carrito_item'),

    path('pagos/', views.pagar, name='pagos')
]
