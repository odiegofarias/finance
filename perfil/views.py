from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum
from django.http import HttpResponse
from .models import Conta, Categoria



def home(request):
    return render(request, 'home.html')

def gerenciar(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    total_contas = contas.aggregate(Sum('valor'))['valor__sum']
    # total_contas = 0

    # for conta in contas:
    #     total_contas += conta.valor

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
    except Conta.DoesNotExist:
        return HttpResponse('Não encontrado')

    return redirect(reverse('gerenciar'))

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