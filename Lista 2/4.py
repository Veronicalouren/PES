numero = int(input("Digite um número: "))

i = 0 

while i <= numero:
    if i % 2 == 0:
        print(i)
    i += 1

# Solicita ao usuário um número
numero = int(input("Digite um número: "))

# A contagem começa em 0
i = 0

# Repete enquanto i for menor ou igual ao número digitado
while i <= numero:

    # Verifica se i é par
    if i % 2 == 0:
        print(i)  # Exibe o número par

    # Passa para o próximo número
    i += 1