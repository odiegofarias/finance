from django.db import models
from perfil.models import Categoria, Conta


CHOICE_TIPO = (
    ('E', 'Entrada'),
    ('S', 'Saída')
)


class Valores(models.Model):
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    data = models.DateField()
    conta = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    tipo = models.CharField(max_length=1, choices=CHOICE_TIPO)

    def __str__(self) -> str:
        return self.descricao
