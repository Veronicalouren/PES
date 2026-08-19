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

///////////////////////////////////////////

def eh_digimon_ou_pokemon(nome): 
    if(nome == "metamon"):
        return "pokemon"
    
    if "mon" in nome: 
        return "digimon"
    else: 
        return "pokemon"

nome_bixo = input("Me diga o nome da criatura: ")
tipo = eh_digimon_ou_pokemon(nome_bixo)
if tipo == "pokemon":
    print("Muito legal seu monstrinho do pokemon")
    print("O meu favorito é a Eevee")
else:
    print("Não sei nada de digimon")