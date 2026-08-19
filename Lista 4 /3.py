notas = []

opcao = -1 

while opcao != 0:
    print("""
[1] - Cadastrar nota
[2] - Exibir notas com while
[3] - Exibir notas com for
[0] - Sair
""")

    opcao = int(input("Digite a opção escolhida: "))

    if opcao == 1:
        quantidade = int(input("Quantas notas deseja cadastrar? "))

        indice = 0

        while indice < quantidade:
            nota = float(input("Digite a nota: "))
            notas.append(nota)
            indice = indice + 1

    elif opcao == 2:
        indice = 0

        while indice < len(notas):
            print("Nota:", notas[indice])
            indice = indice + 1

    elif opcao == 3:
        for nota in notas:
            print("Nota:", nota)

    elif opcao == 0:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")