from django.contrib.auth.models import User
from django.db import models


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    ra = models.CharField(max_length=20, unique=True)
    digito_ra = models.CharField(max_length=2, default="")
    uf = models.CharField(max_length=2, default="SP")
    turma = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    @property
    def identificador_login(self):
        return f"{self.ra}-{self.digito_ra}-{self.uf.upper()}"


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    rg = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome
