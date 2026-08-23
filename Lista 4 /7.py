notas = []

opcao = -1
while opcao != 0:
    print("""            
            Notas
            --------
            [1] - Cadastrar
            [2] - Excluir
            [3] - Listar
            [4] - Calcular média
            [5] - Mostrar maior nota
            [6] - Mostrar menor nota 
            [0]- Sair
            Opção: 
          """)
    
    opcao = int(input("Digite a opcao escolhida: "))

    if opcao == 1: 
        quantidade = int(input("Quantas notas você deseja cadastrar?"))
        indice = 0

        while indice < quantidade:
            nota = float(input("Digite a nota: "))
            notas.append(nota)
            indice = indice + 1 
    
    elif opcao == 2: 
        if len(notas) == 0:
            print("Erro: não há notas cadastradas")
        else:
            indice = 0 

            while indice < len(notas):
                print(indice, " posição, ", notas[indice], " nota")
                indice = indice + 1 

            indice_selecionado = int(input("Digite a nota que deseja remover: "))
            notas.pop(indice_selecionado)
    
    elif opcao == 3:
        if len(notas) == 0:
            print("Lista vazia!")
        else:
            indice = 0 

            while indice < len(notas): 
                print(notas[indice])
                indice = indice + 1 
    
    elif opcao == 4:

        if len(notas) == 0:
            print("Lista vazia!")

        else:
            soma = 0
            indice = 0

            while indice < len(notas):
                soma = soma + notas[indice]
                indice = indice + 1

            media = soma / len(notas)
            print("Média:", media)

            if media >= 6:
                print("Aprovado!")
            else:
                print("Reprovado!")

    elif opcao == 5:
        if len(notas) == 0:
            print("Erro: não há notas cadastradas")

        else:
            maior = notas[0]
            indice = 1 

            while indice < len(notas):
                if notas[indice] > maior:
                    maior = notas[indice]

                indice = indice + 1 

            print("Maior nota:", maior)

    elif opcao == 6:
        if len(notas) == 0:
            print("Erro: não há notas cadastradas")

        else:
            menor = notas[0]
            indice = 1 

            while indice < len(notas):
                if notas[indice] < menor:
                    menor = notas[indice]

                indice = indice + 1 

            print("Menor nota:", menor)

    elif opcao == 0:
        print("Programa encerrado.")

    else:
        print("Opção inválida!")

                           