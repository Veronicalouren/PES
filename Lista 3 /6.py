nomes = []
idades = []
alturas = []
pesos = []
codigos = []

opcao = -1 
while opcao != 0:
    print("""
# 1 - Cadastrar
# 2 - Excluir pelo nome
# 3 - Excluir pelo código
# 4 - Alterar
# 5 - Pesquisar pelo nome
# 6 - Listar
# 0 - Sair
""")
    
    opcao = int(input("Digite uma opção: "))
    
    if opcao == 1:
        nome = input("Digite o nome da pessoa que deseja cadastrar: ")
        nomes.append(nome)
        idade = int(input("Digite a idade: "))
        idades.append(idade)
        altura = float(input("Digite a altura: "))
        alturas.append(altura)
        peso = float(input("Digite o peso: "))
        pesos.append(peso)
        codigo = int(input("Digite o código da pessoa: "))
        codigos.append(codigo)

    elif opcao == 2:

        nome = input("Digite o nome da pessoa que deseja excluir: ")

        if nome in nomes:

             indice = nomes.index(nome)

             nomes.pop(indice)
             idades.pop(indice)
             alturas.pop(indice)
             pesos.pop(indice)
 
             print("Pessoa excluída com sucesso!")
 
        else:
             print("Pessoa não encontrada!")  
    
    elif opcao == 3:
        
        codigo = int(input("Digite o coódigp da pessoa que deseja excluir: "))
        
        if codigo in codigos:

            indice = codigos.index(codigo)

            nomes.pop(indice)
            idades.pop(indice)
            alturas.pop(indice)
            pesos.pop(indice)

            print("Pessoa removida com sucesso!")
        
        else:
            print("Pessoa não encontrada")


    elif opcao == 4:

        nome = input("Digite o nome da pessoa que deseja alterar: ")

        if nome in nomes:
            indice = nomes.index(nome)

            idade = int(input("Digite a idade alterada: "))
            idades[indice] = idade

            peso = float(input("Digite o peso alterado: "))
            pesos[indice] = peso

            altura = float(input("Digite a altura alterada: "))
            alturas[indice] = altura

            print("Cadastro alterado com sucesso!")
        else:
            print("Pessoa não encontrada!")
    
    elif opcao == 5:
        nome = input("Digite o nome da pessoa que você deseja pesquisar: ")

        if nome in nomes:
            indice = nomes.index(nome)
            print(f"Nome: {nomes[indice]}")
            print(f"Idade: {idades[indice]}")
            print(f"Altura: {alturas[indice]}")
            print(f"Peso: {pesos[indice]}")
        else:
            print("Pessoa não encontrada!")

    elif opcao == 6:
        indice = 0 
        while indice < len(nomes):
            print(f"Nome: {nomes[indice]}")
            print(f"Idade: {idades[indice]}")
            print(f"Altura: {alturas[indice]}")
            print(f"Peso: {pesos[indice]}")
            indice = indice + 1 
            print("--------------------")

    
    elif opcao == 0:
        print("Saindo...")

    else:
        print("Opção inválida!")
