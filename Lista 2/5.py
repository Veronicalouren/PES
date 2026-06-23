numero = int(input("Digite um número: "))

print("Tabuada do número", numero)

i = 1 

while i <= 10:
    print(numero, "x", i, "=", numero * i)
    i += 1


# Solicita ao usuário um número
numero = int(input("Digite um número: "))

# Exibe o título da tabuada
print("Tabuada do número", numero)

# O contador começa em 1
contador = 1

# Repete enquanto o contador for menor ou igual a 10
while contador <= 10:
    
    # Exibe a multiplicação e o resultado
    print(numero, "x", contador, "=", numero * contador)
    
    # Aumenta o contador em 1
    # É o mesmo que: contador = contador + 1
    contador += 1