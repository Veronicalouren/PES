numero = int(input("Digite um número: "))

inicio = int(input("Digite o inicio da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

print("Tabuada do número", numero)

i = inicio 

while i <= fim: 
    print(numero, "x", i, "=", numero * i)
    i += 1 


# Número da tabuada
numero = int(input("Digite um número: "))

# Início e fim da tabuada
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

# Exibe o título da tabuada
print("Tabuada do número", numero)

# i começa no valor inicial informado
i = inicio

# Repete enquanto i for menor ou igual ao valor final
while i <= fim:

    # Exibe a multiplicação e o resultado
    print(numero, "x", i, "=", numero * i)

    # Aumenta i em 1
    # É o mesmo que: i = i + 1
    i += 1