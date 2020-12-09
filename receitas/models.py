from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateField(default=datetime.now, blank=True)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    publicada = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='foto/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.nome_receita
