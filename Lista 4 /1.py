bairros = ["Centro"]

indice = 0 

while indice < 5: 
    bairro = input("Digite o nome do bairro: ")
    bairros.append(bairro)
    indice = indice + 1 

print("\nBairros cadastrados: ")

indice = 0 

while indice < len(bairros):
    print(bairros[indice])
    indice = indice + 1 