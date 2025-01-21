from django.urls import path
from . import views


urlpatterns = [
    path('partial/<id>', views.partial, name='testando'),  # home
    path('', views.home),  # home
]
