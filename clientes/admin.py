from django.contrib import admin

# Register your models here.

# 5) (Opcional pero útil) Admin
#En clientes/admin.py:

from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("clave", "nombre", "email", "telefono", "actualizado")
    search_fields = ("clave", "nombre", "email")
