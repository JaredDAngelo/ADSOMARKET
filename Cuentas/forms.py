from typing import Any
from django import forms
from .models import Cuenta

DEPARTAMENTOS = [
    ('Amazonas', 'Amazonas'),
    ('Antioquia', 'Antioquia'),
    ('Arauca', 'Arauca'),
    ('Atlántico', 'Atlántico'),
    ('Bolívar', 'Bolívar'),
    ('Caldas', 'Caldas'),
    ('Caquetá', 'Caquetá'),
    ('Casanare', 'Casanare'),
    ('Cauca', 'Cauca'),
    ('Cesar', 'Cesar'),
    ('Chocó', 'Chocó'),
    ('Córdoba', 'Córdoba'),
    ('Cundinamarca', 'Cundinamarca'),
    ('Guainía', 'Guainía'),
    ('Guaviare', 'Guaviare'),
    ('Huila', 'Huila'),
    ('La Guajira', 'La Guajira'),
    ('Magdalena', 'Magdalena'),
    ('Meta', 'Meta'),
    ('Nariño', 'Nariño'),
    ('Norte de Santander', 'Norte de Santander'),
    ('Putumayo', 'Putumayo'),
    ('Quindío', 'Quindío'),
    ('Risaralda', 'Risaralda'),
    ('San Andrés y Providencia', 'San Andrés y Providencia'),
    ('Santander', 'Santander'),
    ('Sucre', 'Sucre'),
    ('Tolima', 'Tolima'),
    ('Valle del Cauca', 'Valle del Cauca'),
    ('Vaupés', 'Vaupés'),
    ('Vichada', 'Vichada'),
]

class FormularioRegistro(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={#atributos
            'placeholder': 'Ingresa Tu contraseña',
            'class': 'form-control',
    }))
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirma Tu contraseña',
            'class': 'form-control',
    }))
    departamento = forms.ChoiceField(choices=DEPARTAMENTOS, widget=forms.Select(attrs={
        'class': 'form-control'
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

    def clean(self):
        cleaned_data = super(FormularioRegistro, self).clean()
        contraseña = cleaned_data.get('contraseña')
        confirmar_contraseña = cleaned_data.get('confirmar_contraseña')

        if contraseña != confirmar_contraseña:
             raise forms.ValidationError(
                  'La contraseña no coincide'
             )