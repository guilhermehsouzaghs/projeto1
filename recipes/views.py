from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Visualização para a parte sobre"""
    return render(request, 'recipes/home.html')


def sobre(request):
    """Visualização para a parte sobre"""
    return render(request, 'recipes/sobre.html')


def contato(request):
    """Visualização para a parte sobre"""
    return render(request, 'recipes/contato.html')
