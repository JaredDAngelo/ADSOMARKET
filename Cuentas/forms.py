from django import forms
from .models import Cuenta


class FormularioRegistro(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={#atributos
            'placeholder': 'Ingresa Tu contraseña',
            'class': 'form-control',
    }))
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirma Tu contraseña',
            'class': 'form-control',
    }))
    class Meta:
        model = Cuenta
        fields = ['nombre', 'apellido', 'correo', 'username', 'telefono', 'ciudad', 'departamento' ]

    def __init__(self, *args, **kwargs ):
            super(FormularioRegistro, self).__init__(*args, **kwargs)
            self.fields['nombre'].widget.attrs['placeholder'] = 'Ingresa tu Nombre'
            self.fields['apellido'].widget.attrs['placeholder'] = 'Ingresa tu Apellido'
            self.fields['correo'].widget.attrs['placeholder'] = 'Ingresa tu Correo'
            self.fields['username'].widget.attrs['placeholder'] = 'Ingresa tu Username'
            self.fields['telefono'].widget.attrs['placeholder'] = 'Ingresa tu Telefono'
            self.fields['ciudad'].widget.attrs['placeholder'] = 'Ingresa tu Ciudad'
            
            for field in self.fields:
                 self.fields[field].widget.attrs['class'] = 'form-control'#configuracion para darle el estilo definido en bootstrap a todos los campos 