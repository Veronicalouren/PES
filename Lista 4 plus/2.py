condutores = [{
    "cod": "001",
    "nome": "Roberto Souza"
}, {
    "cod": "002",
    "nome": "João Graciano"
}, {
    "cod": "003",
    "nome": "Karine Silva"
}, {
    "cod": "004",
    "nome": "Pedro Luiz"
}, {
    "cod": "005",
    "nome": "Maria Catarina"
}, {
    "cod": "006",
    "nome": "Júlio Cardoso"
}, {
    "cod": "007",
    "nome": "Altivo Antônio"
}, {
    "cod": "008",
    "nome": "Jorge Gonçalves"
}, {
    "cod": "009",
    "nome": "Marcos Vinícius"
}, {
    "cod": "010",
    "nome": "Heleno Nunes"
}, {
    "cod": "011",
    "nome": "Mara Cristina"
}, {
    "cod": "012",
    "nome": "Otávio Rocha"
}]

caminhoes = [{
    "cod": "001",
    "modelo": "Monobloco"
}, {
    "cod": "002",
    "modelo": "Scania 112 HW"
}, {
    "cod": "003",
    "modelo": "Volkswagen Express 4150"
}, {
    "cod": "004",
    "modelo": "Volkswagen Express 6160"
}, {
    "cod": "005",
    "modelo": "Volkswagen VW 17230 Worker"
}, {
    "cod": "006",
    "modelo": "Volkswagen Express 9170"
}, {
    "cod": "007",
    "modelo": "Iveco Daily 40s14"
}, {
    "cod": "008",
    "modelo": "Iveco Tectro 310E28"
}]

saidas = []

opcao = -1

while opcao != 0:

    print("""
[1] Listar caminhões
[2] Listar condutores
[3] Registrar saída
[4] Registrar retorno
[5] Verificar caminhão
[6] Listar retornos por data
[7] Verificar entregas do dia
[0] Sair
""")

    opcao = int(input("Me diga: "))

    if opcao == 1:

        indice = 0

        while indice < len(caminhoes):

            print(
                "Caminhão: " +
                caminhoes[indice]["cod"] +
                " | Modelo: " +
                caminhoes[indice]["modelo"]
            )

            indice += 1

    elif opcao == 2:

        indice = 0

        while indice < len(condutores):

            print(
                "Condutor: " +
                condutores[indice]["cod"] +
                " | Nome: " +
                condutores[indice]["nome"]
            )

            indice += 1

    elif opcao == 3:

        cod_caminhao = input("Código do caminhão: ")
        cod_condutor = input("Código do condutor: ")
        data = input("Data da saída: ")
        hora = input("Hora da saída: ")

        saidas.append({
            "caminhao": cod_caminhao,
            "condutor": cod_condutor,
            "data": data,
            "hora_saida": hora,
            "hora_retorno": ""
        })

        print("Saída registrada!")

    elif opcao == 4:

        cod_caminhao = input("Código do caminhão: ")
        data = input("Data do retorno: ")
        hora = input("Hora do retorno: ")

        indice = 0

        while indice < len(saidas):

            if saidas[indice]["caminhao"] == cod_caminhao:
                saidas[indice]["hora_retorno"] = hora
                saidas[indice]["data"] = data

                print("Retorno registrado!")

            indice += 1

    elif opcao == 5:

        cod_caminhao = input("Código do caminhão: ")

        indice = 0

        while indice < len(saidas):

            if saidas[indice]["caminhao"] == cod_caminhao:

                cod_condutor = saidas[indice]["condutor"]

                indice2 = 0

                while indice2 < len(condutores):

                    if condutores[indice2]["cod"] == cod_condutor:

                        nome = condutores[indice2]["nome"]

                    indice2 += 1

                print("Caminhão:", cod_caminhao)
                print("Condutor:", nome)
                print("Data:", saidas[indice]["data"])
                print("Hora de saída:", saidas[indice]["hora_saida"])

                if saidas[indice]["hora_retorno"] == "":
                    print("O caminhão ainda não retornou!")
                else:
                    print(
                        "Hora de retorno:",
                        saidas[indice]["hora_retorno"]
                    )

            indice += 1

    elif opcao == 6:

        data = input("Digite a data: ")

        indice = 0

        while indice < len(saidas):

            if saidas[indice]["data"] == data:

                if saidas[indice]["hora_retorno"] != "":

                    print(
                        "Caminhão:",
                        saidas[indice]["caminhao"],
                        "| Retorno:",
                        saidas[indice]["hora_retorno"]
                    )

            indice += 1

    elif opcao == 7:

        data = input("Digite a data: ")

        total = 0
        retornaram = 0

        indice = 0

        while indice < len(saidas):

            if saidas[indice]["data"] == data:

                total += 1

                if saidas[indice]["hora_retorno"] != "":
                    retornaram += 1

            indice += 1

        print("Caminhões que saíram:", total)
        print("Caminhões que retornaram:", retornaram)

        if total == retornaram:
            print("Todas as entregas foram realizadas!")
        else:
            print("Ainda existem entregas pendentes!")

    elif opcao == 0:

        print("Programa encerrado!")

    else:

        print("Opção inválida!")
