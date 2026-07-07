quantidade = 0
soma = 0 

numero = int(input("Digite um número: "))

while numero != 0:
    quantidade += 1
    soma += numero 
    numero = int(input("Digite outro número (0 para encerrar): "))


if quantidade > 0:
    media = soma/quantidade 
else:
    media = 0 


print("Quantidade de números digitados:", quantidade)
print("soma:", soma)
print("Media:", media)