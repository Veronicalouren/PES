automoveis = [-1]*15






opcao = 0 
menu = """
# 1 - cadastrar 
# 2 - Excluir 
# 3 - Listar
# 0 - Sair 
"""

while opcao != 0: 
    print(menu)
    print("Qual apção você quer?")
    opcao = int(input("R: "))

if (opcao == 1):
    print("Opção de cadastro selecionada")
    indice = 0 
    while indice < len(automoveis):
        if automoveis[indice] == -1:
            print("Foi encontrado uma vaga!")
            print("Adicionando carro")
            print("Qual é sua placa?")

            placa = input("R: ")
            automoveis[indice] = placa

            houve_cadastro = true 
            break 
        indice = indice + 1 
    if houve_cadastro:
        print("Cadastro com sucesso!")
    else:
        print("Sem vagas disponiveis")

elif(opcao == 2):
    print("Me diga qual a placa do carro que você deseja remover!")
    placa = input("R: ")

    #Buscar posição 
    posicao = -1
    indice = 0 
    while indice < len(automoveis):
        if automoveis[indice] == placa:
            posicao = indice 
        indice = indice + 1
    
    if(posicao != -1)
       print("carro encontrado, removendo")
       automoveis[posicao]
                  