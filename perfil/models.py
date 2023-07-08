from django.db import models
from datetime import datetime


class Categoria(models.Model):
    categoria = models.CharField(max_length=25)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.DecimalField(default=0, max_digits=8, decimal_places=2) # type: ignore

    def __str__(self) -> str:
        return self.categoria
    
    def total_gasto(self):
        # Importação Circular, RESOLVER MAIS TARDE
        from extrato.models import Valores

        # Filtrando por valores correspondentes à categoria atual, do mês atual e que seja uma saída
        valores = Valores.objects.filter(
            categoria__id=self.id).filter(
                data__month=datetime.now().month).filter(
                    tipo='S'
            )
        
        # TODO: transformar o código parecido com o utils e aggregate
        total = 0
        for valor in valores:
            total += valor.valor

        return total
    
    def calcula_percentual_gasto_por_categoria(self):
        return int((self.total_gasto() * 100) / self.valor_planejamento)
    

    # TODO: REalizar BARRA COM TOTAL de GASTOS NO MÊS
    

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
    banco = models.CharField(max_length=2 , choices=BANCO_CHOICES)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    valor = models.DecimalField(default=0, max_digits=8, decimal_places=2) # type: ignore
    icone = models.ImageField(upload_to='icones')

    def __str__(self) -> str:
        return self.apelido
    