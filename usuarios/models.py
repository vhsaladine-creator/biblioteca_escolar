from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    nome = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    telefone = models.CharField(
        max_length=15
    )

    ra = models.CharField(
        max_length=20,
        unique=True
    )

    turma = models.CharField(
        max_length=50
    )


    def __str__(self):
        return self.nome



class Professor(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    nome = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    telefone = models.CharField(max_length=12)

    rg = models.CharField(
        max_length=20,
        unique=True
    )


    def __str__(self):
        return self.nome