from django.shortcuts import render
from .forms import FormularioRegistro


def registro(request):
    form = FormularioRegistro()
    context = {
        'form': form,
    }
    return render(request, 'Cuentas/registro.html', context)

def login(request):
    return render(request, 'Cuentas/login.html')

def logout(request):
    return 