
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Tienda, name="Tienda"),
    path("<slug:categoria_slug>/", views.Tienda, name="productos_by_categoria"),
    path("<slug:categoria_slug>/<slug:producto_slug>/", views.producto_detalles, name="producto_detalles"),
    
]
