from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito, name='carrito'),
    path('agregar_carrito/<int:id_producto>/', views.agregar_carrito, name='agregar_carrito'),
]
