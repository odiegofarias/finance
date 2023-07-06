from django.db import models
from django.db.models import Sum


class Categoria(models.Model):
    categoria = models.CharField(max_length=25)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.categoria
    

BANCO_CHOICES = (
    ('NU', 'Nubank'),
    ('CE', 'Caixa Econômica'),
    ('IT', 'Itaú'),
    ('BB', 'Banco do Brasil'),
)

TIPO_CHOICES = (
    ('PF', 'Pessoa Física'),
    ('PJ', 'Pessoa Jurídica'),
)


class Conta(models.Model):
    apelido = models.CharField(max_length=25)
    banco = models.CharField(max_length=2 ,choices=BANCO_CHOICES)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    valor = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    icone = models.ImageField(upload_to='icones')

    def __str__(self) -> str:
        return self.apelido
    