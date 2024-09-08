from django.contrib import admin
from .models import Categorias

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria',)
    prepopulated_fields ={'slug': ('nombre_categoria',)}

admin.site.register(Categorias, CategoriaAdmin)
