from django.shortcuts import redirect, render
from perfil.models import Categoria, Conta
from .models import Valores
from django.contrib.messages import constants
from django.contrib import messages
from decimal import Decimal
from datetime import datetime


def novo_valor(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        contas = Conta.objects.all()
        
        return render(request, 'novo_valor.html', {
            'categorias': categorias,
            'contas': contas
        })
    elif request.method == "POST":
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo')

        valores = Valores(
            valor = valor,
            categoria_id = categoria,
            descricao = descricao,
            data = data,
            conta_id = conta,
            tipo = tipo
        )

        valores.save()

        conta = Conta.objects.get(id=conta) # type: ignore

        mensagem_tipo = ''

        if tipo == "E":
            conta.valor += Decimal(valor)
            mensagem_tipo = 'Entrada'
        else:
            conta.valor -= Decimal(valor)
            mensagem_tipo = 'Saída'
        
        conta.save()

        messages.add_message(request, constants.SUCCESS, f'{mensagem_tipo} cadastrada com sucesso.')

        return redirect('novo_valor')
    
def extrato(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    conta_get = request.GET.get('conta')
    categoria_get = request.GET.get('categoria')

    valores = Valores.objects.filter(data__month=datetime.now().month)
    # TODO: Criar o Filtro de 7 dias
    if conta_get:
        valores = valores.filter(conta_id=conta_get)
    if categoria_get:
        valores = valores.filter(categoria_id=categoria_get)

    context = {
        'valores': valores,
        'contas': contas,
        'categorias': categorias,
    }


    return render(request, 'extrato.html', context)

def limpa_filtros(request):
    return redirect('extrato')

def exportar_pdf(request):
    ...



