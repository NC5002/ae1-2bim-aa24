from django.shortcuts import render, get_object_or_404, redirect
from .models import PlatoTipico

def lista_platos(request):
    platos = PlatoTipico.objects.all()
    return render(request, 'primer_parte/lista_platos.html', {'platos': platos})

def agregar_al_carrito(request, plato_id):
    plato = PlatoTipico.objects.get(id=plato_id)
    carrito = request.session.get('carrito', [])
    carrito.append(plato.id)
    request.session['carrito'] = carrito
    return redirect('lista_platos')

def ver_carrito(request):
    carrito_ids = request.session.get('carrito', [])
    carrito = PlatoTipico.objects.filter(id__in=carrito_ids)
    total = sum(plato.precio_estimado for plato in carrito)
    return render(request, 'primer_parte/carrito.html', {'carrito': carrito, 'total': total})

#funcion para eliminar un plato del carrito
def eliminar_del_carrito(request, plato_id):
    plato = get_object_or_404(PlatoTipico, id=plato_id)
    carrito = request.session.get('carrito', [])
    
    # Eliminar el plato del carrito
    if plato.id in carrito:
        carrito.remove(plato.id)
        request.session['carrito'] = carrito
    
    return redirect('ver_carrito')