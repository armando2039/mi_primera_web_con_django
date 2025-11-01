from django.contrib import admin
from .models import Cliente

# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("clave", "nombre", "email", "telefono", "actualizado")
    search_fields = ("clave", "nombre", "email")
