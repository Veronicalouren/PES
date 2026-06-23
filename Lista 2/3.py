numero = int(input("Digite um número: "))

contador = 1 

if numero >= 1:
    while contador <= numero: 
        print(contador)
        contador += 1 
else: 
    while contador >= numero:
        print(contador)
        contador -= 1 


# Solicita ao usuário um número inteiro
numero = int(input("Digite um número: "))

# A contagem sempre começa em 1
contador = 1

# Verifica se o número informado é positivo ou igual a 1
if numero >= 1:

    # Enquanto o contador for menor ou igual ao número digitado
    while contador <= numero:
        print(contador)      # Exibe o valor do contador
        contador += 1        # Aumenta o contador em 1

# Caso o número seja menor que 1 (zero ou negativo)
else:

    # Enquanto o contador for maior ou igual ao número digitado
    while contador >= numero:
        print(contador)      # Exibe o valor do contador
        contador -= 1        # Diminui o contador em 1