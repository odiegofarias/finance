from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum
from django.http import HttpResponse
from .models import Conta



def home(request):
    return render(request, 'home.html')

def gerenciar(request):
    contas = Conta.objects.all()
    total_contas = contas.aggregate(Sum('valor'))['valor__sum']
    # total_contas = 0

    # for conta in contas:
    #     total_contas += conta.valor

    return render(request, 'gerenciar.html', {'contas': contas, 'total_contas': total_contas})

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

    messages.add_message(request, constants.SUCCESS, 'Conta adicionada com sucesso.')
    return redirect(reverse('gerenciar'))

def deletar_banco(request, id):
    try:
        conta = Conta.objects.get(id=id)
        conta.delete()
    except Conta.DoesNotExist:
        return HttpResponse('Não encontrado')

    return redirect(reverse('gerenciar'))