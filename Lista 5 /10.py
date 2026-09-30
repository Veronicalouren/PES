import random

def embaralhar(palavra):

    palavra = palavra.lower()
    resultado = ""

    while palavra != "":

        posicao = random.randint(0, len(palavra) - 1)

        resultado = resultado + palavra[posicao]

        palavra = palavra[:posicao] + palavra[posicao + 1:]

    return resultado


texto = input("Digite uma palavra: ")

print("Palavra embaralhada:", embaralhar(texto))
