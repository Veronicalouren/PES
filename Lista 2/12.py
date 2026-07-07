opcao = -1 

while opcao != 0:

    print("""Menu
    -------
    1 – Adição
    2 – Subtração
    3 – Divisão
    4 – Multiplicação
    0 - Sair
        """)

    opcao = int(input("Digite a opcao: "))

    if opcao == 0:
        print("Programa encerrado. ")

    elif opcao == 1: 
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", num1 + num2)

    elif opcao == 2:
        num1 = float (input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", num1 - num2)

    elif opcao == 3:
        num1 = float (input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if num1 != 0:
            print("Resultado: ", num1 / num2)
        else:
            print("Não é possível dividir por zero.")

    elif opcao == 4:
        num1 = float (input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", num1 * num2)

    else:
            print("Opção inválida!")
        