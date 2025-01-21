from django.shortcuts import render
from django.http import HttpResponse
from main import GerarNomes
from django.utils.html import escape


def home(request):
    """Visualização para a parte sobre"""
    return render(request, 'recipes/pages/home.html')


def partial(request, id):
    """Visualização para a parte sobre"""
    page = 'recipes/pages/partial_home.html'
    return render(request, page, context={
        'nome': GerarNomes()
    })
