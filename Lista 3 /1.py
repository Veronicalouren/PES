idades = [-1,-1,-1,-1,-1,-1]

opcao = -1 

while opcao != 0:
    print("""
[1] - Cadastro
[2] - Listar
[0] - Sair
""")
    opcao = int(input("Digite a opção escolhida: "))

    if opcao == 1: 
        print("Faremos o cadastro")
        indice = 0 
        while indice < len(idades):
            idades[indice] = int(input("Digite a idade do aluno"+str(indice+1)+": "))
            indice += 1 
    elif opcao == 2:
        print("Listaremos")
        for idade in idades:
            if(idade >= 16):
                print(idade)
    elif opcao == 0:
        print("Saindo")