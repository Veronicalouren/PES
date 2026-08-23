#Simples
def impar_ou_par():
    if (valor % 2) != 0:
        print("È ímpar")
    else:
        print("È par")

    
numero = int(input("Digite um número: "))
impar_ou_par(numero)



#Avançado
def impar_ou_par(valor):
    if (valor % 2) != 0:
        print("È ímpar")
    else:
        print("È par")

    
numero = int(input("Digite um número: "))
impar_ou_par(numero)


#Expert
def impar_ou_par(valor):
    if (valor % 2) != 0:
        return "È ímpar"
    else:
        return "È par"

    
numero = int(input("Digite um número: "))
resultado = impar_ou_par(numero)
print(resultado)

