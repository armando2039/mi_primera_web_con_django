from django.db import models


# Create your models here.
# 3) Definir el modelo (equivalente a tu clase Cliente)

#from django.db import models

class Cliente(models.Model):
    clave = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=120, db_index=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.clave} - {self.nombre}"


#Esto reemplaza la lista en memoria de tu script y la vuelve tabla real.

#4) Migraciones
#python manage.py makemigrations
#python manage.py migrate