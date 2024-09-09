
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Tienda, name="Tienda"),
    path("<slug:categoria_slug>/", views.Tienda, name="productos_by_categoria"),
    
]
