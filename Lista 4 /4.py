cidades = []

quantidade = int(input("Digite a quantiade de cidades que devem ser cadastradas: "))

indice =  0

while indice < quantidade:
    cidade = (input("Digite o nome da cidade: "))
    cidades.append(cidade)
    indice = indice + 1

print("\nCidades cadastradas: ")

indice = 0 

while indice < len(cidades): 
    print(cidades[indice])
    indice = indice + 1 

remover = (input("\nDigite uma cidade para ser removida: "))

cidades.remove(remover)

print("\nCidades após a remoção: ")

indice = 0 

while indice < len(cidades):
    print(cidades[indice])
    indice = indice + 1 




        

