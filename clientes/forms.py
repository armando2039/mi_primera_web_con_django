#6) Formularios (para validar y renderizar)

#En clientes/forms.py:

from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["clave", "nombre", "email", "telefono"]
