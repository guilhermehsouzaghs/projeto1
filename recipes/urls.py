from django.urls import path
from recipes.views import sobre, contato, home


urlpatterns = [
    path('', home),  # home
    path('sobre/', sobre),  # sobre,
    path('contato/', contato),  # contato
]
