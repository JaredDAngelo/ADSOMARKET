from django.shortcuts import render, redirect
from .forms import FormularioRegistro
from .models import Cuenta
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


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
    if request.method == 'POST':
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']

        user = auth.authenticate(request, correo=correo, password=contraseña)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Ingreso Exitoso')
            return redirect('home')
        else:
            messages.error(request, 'Datos de ingreso incorrectos')
            return redirect('login')
    return render(request, 'Cuentas/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Sesion finalizada.') 
    return redirect('login')