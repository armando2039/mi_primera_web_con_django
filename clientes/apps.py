from django.apps import AppConfig


class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientes' # <-- este debe ser el path real del paquete
    verbose_name = "Gestión de Clientes"  # opcional, solo para el admin
