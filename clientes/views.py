from django.shortcuts import render

# Create your views here.
#9) Views (la “capa de orquestación”)

#Usamos class-based views para velocidad y limpieza.

#En clientes/views.py:

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm

class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes/cliente_list.html"
    context_object_name = "clientes"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().order_by("nombre")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(nombre__icontains=q)
        return qs

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "clientes/cliente_detail.html"
    context_object_name = "cliente"

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/cliente_form.html"
    success_url = reverse_lazy("clientes:list")

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/cliente_form.html"
    success_url = reverse_lazy("clientes:list")

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "clientes/cliente_confirm_delete.html"
    success_url = reverse_lazy("clientes:list")


#Aquí “traducimos” tu menú:

#Agregar cliente → ClienteCreateView

#Buscar por nombre → ClienteListView con ?q=texto

#Eliminar → ClienteDeleteView

#Actualizar → ClienteUpdateView