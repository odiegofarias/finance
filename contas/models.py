from django.db import models
from perfil.models import Categoria


# Contas a vencer que gera a model Conta paga
class ContaPagar(models.Model):
    titulo = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    valor = models.FloatField()
    dia_pagamento = models.IntegerField()

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = 'Contas a Pagar'
    

class ContaPaga(models.Model):
    conta = models.ForeignKey(ContaPagar, on_delete=models.DO_NOTHING)
    data_pagamento = models.DateField()


    class Meta:
        verbose_name_plural = 'Contas Pagas'
    
