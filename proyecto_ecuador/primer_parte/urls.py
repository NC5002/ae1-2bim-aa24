from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_platos, name='lista_platos'),
]
