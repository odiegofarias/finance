from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum
from django.http import HttpResponse
from .models import Conta, Categoria
from .utils import calcula_total, calcula_equilibrio_financeiro
from extrato.models import Valores
from datetime import datetime



def home(request):
    contas = Conta.objects.all()
    total_contas = calcula_total(contas, 'valor')
    valores = Valores.objects.filter(data__month=datetime.now().month)
    entradas = valores.filter(tipo='E')
    saidas = valores.filter(tipo='S')

    
    
    # Duas formas de fazer a mesma coisa
    total_entradas = calcula_total(entradas, 'valor')
    
    total_saidas = 0
    for saida in saidas:
        total_saidas += saida.valor

    # TODO: ORGANIZAR OS SALDOS DA HOME

    percentual_gastos_essenciais, percentual_gastos_nao_essenciais = calcula_equilibrio_financeiro()

    context = {
        'contas': contas,
        'total_contas': total_contas,
        'total_entradas': total_entradas,
        'total_saidas': total_saidas,
        'percentual_gastos_essenciais': round(percentual_gastos_essenciais),
        'percentual_gastos_nao_essenciais': round(percentual_gastos_nao_essenciais)
        
    }
    return render(request, 'home.html', context)

def gerenciar(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    # total_contas = contas.aggregate(Sum('valor'))['valor__sum']
    total_contas = calcula_total(contas, 'valor')

    context = {
        'contas': contas,
        'total_contas': total_contas,
        'categorias': categorias,
    }

    return render(request, 'gerenciar.html', context)

def cadastrar_banco(request):
    # Puxa do atributo name
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')

    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Dados incorretos. Preencha novamente.')
        return redirect(reverse('gerenciar'))
        


    conta = Conta(
        apelido = apelido,
        banco = banco,
        tipo = tipo,
        valor = valor,
        icone = icone
    )

    conta.save()

    messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso.')
    return redirect(reverse('gerenciar'))

def deletar_banco(request, id):
    try:
        conta = Conta.objects.get(id=id)
        conta.delete()

        return redirect(reverse('gerenciar'))
    except Conta.DoesNotExist:
        return HttpResponse('Não encontrado')

def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    if len(nome.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Dados incorretos.')

        return redirect('gerenciar')

    categoria = Categoria(
        categoria = nome,
        essencial = essencial
    )

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso.')

    return redirect(reverse('gerenciar'))

def atualiza_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.essencial = not categoria.essencial
    categoria.save()

    return redirect('gerenciar')

def dashboard(request):
    dados = {}
    categorias = Categoria.objects.all()

    for categoria in categorias:
        total = 0
        valores = Valores.objects.filter(categoria=categoria)
        for v in valores:
            total += float(v.valor)
        # print(f'{categoria} -> {total}')
        dados[categoria.categoria] = total
    """
    for categoria in categorias:
        dados[categoria.categoria] = Valores.objects.filter(categoria=categoria).aggregate(Sum('valor'))['valor__sum']

    return render(request, 'dashboard.html', {'labels': list(dados.keys()), 'values': list(dados.values())})
    """



    return render(request, 'dashboard.html', 
                  {'labels': list(dados.keys()),
                   'values': list(dados.values())
    })