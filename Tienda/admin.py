from django.contrib import admin
from .models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto_nombre', 'precio', 'stock', 'categoria', 'modificar_fecha', 'esta_disponible')
    prepopulated_fields ={'slug': ('producto_nombre',)}

admin.site.register(Producto, ProductoAdmin)

