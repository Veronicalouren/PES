def converter(hora):
    h = int(hora[0:2])
    m = hora[3:5]

    if h == 0:
        h = 12
        periodo = "A"
    elif h < 12:
        periodo = "A"
    elif h == 12:
        periodo = "P"
    else:
        h = h - 12
        periodo = "P"

    return h, m, periodo


def imprimir(hora, minutos, periodo):
    if periodo == "A":
        print(hora, ":", minutos, "A.M.")
    else:
        print(hora, ":", minutos, "P.M.")


opcao = "s"

while opcao == "s":

    entrada = input("Digite a hora (HH:MM): ")

    hora, minutos, periodo = converter(entrada)

    imprimir(hora, minutos, periodo)

    opcao = input("Deseja continuar? (s/n): ")
