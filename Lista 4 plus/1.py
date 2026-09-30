professores = [{
    "cod": "001",
    "nome": "Prof Tiago Paes"
}, {
    "cod": "002",
    "nome": "Prof Schalata"
}, {
    "cod": "003",
    "nome": "Prof Ignácio"
}, {
    "cod": "004",
    "nome": "Prof Ryan"
}, {
    "cod": "005",
    "nome": "Prof André"
}, {
    "cod": "006",
    "nome": "Profª Fabiana"
}, {
    "cod": "007",
    "nome": "Prof Alberto"
}, {
    "cod": "008",
    "nome": "Prof Juliano"
}, {
    "cod": "009",
    "nome": "Prof Thiago Waltrik"
}, {
    "cod": "010",
    "nome": "Prof João Eduardo"
}]

acessos = [{
    "lab": "Lab102",
    "cod": ["001", "003", "004", "005", "006"]
}, {
    "lab": "Lab103",
    "cod": ["007"]
}, {
    "lab": "Lab104",
    "cod": ["002", "004", "005", "008"]
}, {
    "lab": "Lab105",
    "cod": ["001", "003", "007", "009"]
}, {
    "lab": "Lab106",
    "cod": ["001", "002", "003", "009"]
}, {
    "lab": "Lab107",
    "cod": ["001", "002", "005", "009", "010"]
}]

opcao = -1

while opcao != 0:

    print("""
[1] Professor: adicionar
[2] Professor: alterar
[3] Professor: listar
[4] Professor: excluir
[5] Acesso: adicionar
[6] Acesso: alterar
[7] Acesso: listar
[8] Acesso: excluir
[9] Testar acesso
[0] Sair
""")

    opcao = int(input("Me diga: "))

    if opcao == 1:

        cod = input("Qual é o código do professor? R: ")
        nome = input("Qual é o nome do professor? R: ")

        professores.append({
            "cod": cod,
            "nome": nome
        })

        print("Professor cadastrado!")

    elif opcao == 2:

        cod = input("Qual código deseja alterar? R: ")

        indice = 0

        while indice < len(professores):

            if professores[indice]["cod"] == cod:

                nome = input("Qual é o novo nome? R: ")

                professores[indice]["nome"] = nome

                print("Professor alterado!")

            indice += 1

    elif opcao == 3:

        indice = 0

        while indice < len(professores):

            print(
                "- Professor: " +
                professores[indice]["nome"] +
                " | Código: " +
                professores[indice]["cod"]
            )

            indice += 1

    elif opcao == 4:

        cod = input("Qual código deseja excluir? R: ")

        indice = 0

        while indice < len(professores):

            if professores[indice]["cod"] == cod:

                professores.pop(indice)

                print("Professor excluído!")

                break

            indice += 1

    elif opcao == 5:

        lab = input("Qual laboratório? R: ")
        cod = input("Qual código do professor? R: ")

        indice = 0

        while indice < len(acessos):

            if acessos[indice]["lab"] == lab:

                acessos[indice]["cod"].append(cod)

                print("Acesso cadastrado!")

            indice += 1

    elif opcao == 6:

        lab = input("Qual laboratório atual? R: ")
        cod = input("Qual código do professor? R: ")
        novo_lab = input("Qual o novo laboratório? R: ")

        indice = 0

        while indice < len(acessos):

            if acessos[indice]["lab"] == lab:

                if cod in acessos[indice]["cod"]:

                    acessos[indice]["cod"].remove(cod)

            indice += 1

        indice = 0

        while indice < len(acessos):

            if acessos[indice]["lab"] == novo_lab:

                acessos[indice]["cod"].append(cod)

                print("Acesso alterado!")

            indice += 1

    elif opcao == 7:

        indice = 0

        while indice < len(acessos):

            print("\nLaboratório:", acessos[indice]["lab"])

            indice2 = 0

            while indice2 < len(acessos[indice]["cod"]):

                print("Código:", acessos[indice]["cod"][indice2])

                indice2 += 1

            indice += 1

    elif opcao == 8:

        lab = input("Qual laboratório? R: ")
        cod = input("Qual código do professor? R: ")

        indice = 0

        while indice < len(acessos):

            if acessos[indice]["lab"] == lab:

                if cod in acessos[indice]["cod"]:

                    acessos[indice]["cod"].remove(cod)

                    print("Acesso excluído!")

            indice += 1

    elif opcao == 9:

        lab = input("Qual laboratório? R: ")
        cod = input("Qual código do professor? R: ")

        indice = 0

        while indice < len(acessos):

            if acessos[indice]["lab"] == lab:

                if cod in acessos[indice]["cod"]:
                    print("ACESSO PERMITIDO!")
                else:
                    print("ACESSO NEGADO!")

            indice += 1

    elif opcao == 0:

        print("Programa encerrado!")

    else:

        print("Opção inválida!")
