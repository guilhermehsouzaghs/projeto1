from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Visualização para a parte sobre"""
    return render(request, 'recipes/pages/home.html',context={'nome': 'guilherme','qtd':range(10)})