from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cuenta


# Register your models here.

class CuentaAdmin(UserAdmin):
    list_display = ('correo', 'nombre', 'apellido', 'username','ultima_sesion', 'fecha_ingreso', 'activo')
    list_display_links = ('correo', 'nombre', 'apellido')
    readonly_fields = ('ultima_sesion', 'fecha_ingreso')
    ordering = ('-fecha_ingreso',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cuenta, CuentaAdmin)
