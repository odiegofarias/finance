# Recebe a queryset e o campo
# Usamos o getattr pra pegar o campo da queryset, ou seja, conta.valor
def calcula_total(obj, campo):
    total = 0
    for i in obj:
        total += getattr(i, campo)

    return total