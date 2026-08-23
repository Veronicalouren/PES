def soma_elementos (lista):
    soma = 0 
    indice = 0 

    while indice < len(lista):
        soma = soma + lista[indice]
        indice = indice + 1 

    return soma 

lista = []

indice = 0 

while indice < 4:
    numero = float(input("Digite um número: "))
    lista.append(numero)
    indice = indice + 1 

soma = soma_elementos(lista)

print("Soma: ", soma)