from django.shortcuts import render
from .models import PlatoTipico

def lista_platos(request):
    platos = PlatoTipico.objects.all()
    return render(request, 'primer_parte/lista_platos.html', {'platos': platos})

