from django.db import models
from django.contrib.auth.models import User


class Alunos(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    data_cadastro = models.TimeField(auto_now=True)

