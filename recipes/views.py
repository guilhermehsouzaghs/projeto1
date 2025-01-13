from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Visualização para a parte sobre"""
    return render(request, 'recipes/home.html', context={
        'nome': 'Guilherme Henrique'
    })


def sobre(request):
    """Visualização para a parte sobre"""
    return HttpResponse('sobre')


def contato(request):
    """Visualização para a parte sobre"""
    return HttpResponse('contato')
