from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_platos, name='lista_platos'),
    path('agregar_al_carrito/<int:plato_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/<int:plato_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]