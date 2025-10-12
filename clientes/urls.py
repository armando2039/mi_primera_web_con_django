#8) URLs de la app

#Crea clientes/urls.py:

from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path("", views.ClienteListView.as_view(), name="list"),
    path("nuevo/", views.ClienteCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ClienteDetailView.as_view(), name="detail"),
    path("<int:pk>/editar/", views.ClienteUpdateView.as_view(), name="update"),
    path("<int:pk>/eliminar/", views.ClienteDeleteView.as_view(), name="delete"),
]
