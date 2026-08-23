def lista_vazia(lista):
    if len(lista) == 0:
        return True
    else:
        return False


def maior_valor(lista):
    if len(lista) == 0:
        return -1
    
    indice = 1
    maior = lista[0]

    while indice < len(lista):
        if lista[indice] > maior:
            maior = lista[indice]

        indice = indice + 1

    return maior


def menor_valor(lista):
    if len(lista) == 0:
        return -1

    indice = 1
    menor = lista[0]

    while indice < len(lista):
        if lista[indice] < menor:
            menor = lista[indice]

        indice = indice + 1

    return menor


def valor_medio(lista):
    if len(lista) == 0:
        return -1

    soma = 0
    indice = 0

    while indice < len(lista):
        soma = soma + lista[indice]
        indice = indice + 1

    media = soma / len(lista)

    return media


vazia = []
lista_numeros = [8, 5, 10, 7, 3]


print("Lista vazia:", lista_vazia(vazia))
print("Lista com elementos:", lista_vazia(lista_numeros))

print("Maior valor:", maior_valor(lista_numeros))
print("Lista vazia:", maior_valor(vazia))

print("Menor valor:", menor_valor(lista_numeros))
print("Lista vazia:", menor_valor(vazia))

print("Média dos valores:", valor_medio(lista_numeros))
print("Lista vazia:", valor_medio(vazia))
