amigos_proximos = []

opcao = -1 
while opcao != 0:
    print(""" 
Amigos Próximos
---------------
[1] - Cadastrar
[2] - Excluir
[3] - Listar
[0] - Sair
      """)

    opcao = int(input("Digite a opção escolhida: "))

    if opcao == 1: 
        quantidade = int(input("Quantos amigos deseja cadastrar? "))
    
        indice = 0 
        while indice < quantidade: 
            amigo = (input("Digite o nome do amigo: "))
            amigos_proximos.append(amigo)
            indice = indice + 1 

    elif opcao == 2:
        remover = (input("Digite o nome do amigo que deseja remover: "))
        amigos_proximos.remove(remover)
        

    elif opcao == 3:
        if len(amigos_proximos) == 0:
            print("Lista vazia!")
        else:
            indice = 0 
            while indice < len(amigos_proximos): 
                print(amigos_proximos[indice])
                indice = indice + 1 

    elif opcao == 0:
        print("Programa encerrado.")





