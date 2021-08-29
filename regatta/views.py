from django.shortcuts import render, get_object_or_404
from .models import Boat, Clazz, Race, RaceResult, Regatta


def index(request):
    return render(request, 'main.html')

def regattas(request):
    regattas = Regatta.objects.all()
    context = {'regattas': regattas}
    
    return render(request, 'regattas.html', context=context)

def regatta(request, pk):
    regatta = get_object_or_404(Regatta, pk=pk)
    clazz = get_object_or_404(Clazz, pk=1)
    race = get_object_or_404(Race, pk=1)
    results = RaceResult.objects.filter(race=race)

    context = {
        'regatta': regatta,
        'clazz': clazz,
        'race': race,
        'results': results
    }
    
    return render(request, 'regatta.html', context=context)

def boats(request):
    boats = Boat.objects.all()
    context = {'boats': boats}

    return render(request, 'boats.html', context=context)
