placas = [0] * 15

opcao = -1

while opcao != 0:

    print("""
# 1 - Cadastrar
# 2 - Excluir
# 3 - Listar
# 0 - Sair
""")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:

        print("Opção de cadastro selecionada")

        indice = 0

        while indice < len(placas):

            if placas[indice] == 0:

                print("Foi encontrada uma vaga!")

                placa = input("Digite a placa do seu carro: ")

                placas[indice] = placa

                break

            indice = indice + 1

        else:
            print("Não há espaço disponível!")

    elif opcao == 2:

        placa = input("Digite a placa do carro que você deseja remover: ")

        if placa in placas:

            indice = placas.index(placa)

            placas[indice] = 0

            print("Placa removida com sucesso!")

        else:
            print("Placa não encontrada!")

    elif opcao == 3:

        indice = 0

        while indice < len(placas):

            print(f"A vaga {indice} é: {placas[indice]}")

            indice = indice + 1