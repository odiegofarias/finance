from django.shortcuts import render
from perfil.models import Categoria
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from decimal import Decimal


def definir_planejamento(request):
    categorias = Categoria.objects.all()

    return render(request, 'definir_planejamento.html', {'categorias': categorias})

@csrf_exempt
def atualiza_valor_vcategoria(request, id):
    novo_valor = json.load(request)
    valor_decimal = Decimal(novo_valor['novo_valor'])
    

    print(type(valor_decimal))
    
    categoria = Categoria.objects.get(id=id)
    categoria.valor_planejamento = valor_decimal

    categoria.save()

    return JsonResponse({'status': 'sucesso'})