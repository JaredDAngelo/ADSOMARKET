from django.shortcuts import render, redirect
from .forms import FormularioRegistro
from .models import Cuenta
from django.contrib import messages


def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            username = form.cleaned_data['username']
            ciudad = form.cleaned_data['ciudad']
            telefono = form.cleaned_data['telefono']
            contraseña = form.cleaned_data['contraseña']

            usuario = Cuenta.objects.create_user(
                nombre=nombre,
                apellido=apellido,
                correo=correo,
                username=username,
                ciudad=ciudad,
                telefono=telefono,
                password=contraseña
            )
            usuario.save()
            messages.success(request, 'Registro Exitoso! ')
            return redirect('registro')
    else:
        form = FormularioRegistro()
    context = {
        'form': form,
    }
    return render(request, 'Cuentas/registro.html', context)

def login(request):
    return render(request, 'Cuentas/login.html')

def logout(request):
    return 