# # # Questão 01
# # ano = int(input("Digite um ano para descobrir se ele é bissexto: "))

# # if (ano % 4 == 0 or ano % 400 == 0) and (ano % 100 != 0):
# #     print("O ano é bissexto!")
# # else:
# #     print("O ano não é bissexto!")


# Questão 02
# numeros = []


# while len(numeros) < 15:
#     numero = int(input("Digite os números da cartela de bingo: "))
#     if (numero < 1 or numero > 75):
#         print("Número inválido!")
#     elif numero in numeros:
#         print("Não pode número repetido!")
#     else:
#         numeros.append(numero)
#         print("Número adicionado!")


# numeros_ordenados = sorted(numeros)
# print(numeros_ordenados)



# # 3 – Faça um algoritmo que leia o preço de um produto e a quantidade comprada. Calcule o total
# # da compra e, caso ele seja maior ou igual a R$ 100,00, aplique um desconto de 10%. Ao final,
# # exiba o valor a ser pago.

# preco = float(input("Digite o preço do produto: "))
# quantidade = int(input("Digite a quantidade comprada: "))

# total = preco * quantidade

# if total >= 100:
#     desconto = total * 0.1
#     total = total - desconto
# else:
#     print("Você não tem direito ao desconto!")

# print("O total da sua compra é:", total)


4 – Crie um dicionário de palavras da língua portuguesa, utilizando as palavras como chaves e seus
significados como valores. Inicie com:
"apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma
situação difícil, ou usar de meios extremos e exagerados"
Solicite ao usuário mais 4 palavras e seus respectivos significados. Em seguida, peça uma
palavra para consulta e exiba seu significado. Caso ela não esteja cadastrada, informe “Palavra
não encontrada”.

dicionario = {
    "apelar" : "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados"
    }

indice = 0 

while indice < 4:
    palavra = input("Digite a palavra: ")
    significado = input("Digite o seu significado: ")

    dicionario[palavra] = significado

     