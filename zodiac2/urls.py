from django.urls import path
from . import views

#127.0.0.1:8000/zodiac/
urlpatterns = [
    path('',views.index, name="index"),
    #127.0.0.1:8000/zodiac/aries
    path('<str:name>', views.get_by_name, name="get-by-name"),
]