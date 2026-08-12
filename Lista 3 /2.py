# 2 – Crie um programa que leia 4 notas de um(a) determinado(a) estudante. Após a leitura
# de todas notas, exiba a média aritmética simples e a situação final (aprovado(a) ou
# reprovado(a)).

notas = [-1, -1, -1, -1]

opcao = -1 

while opcao != 0:
    print("""
[1] - Cadastrar nota
[2] - Média aritmética e situação final
[0] - Sair
""")
    
    opcao = int(input("Digite a opção escolhida: "))

    if opcao == 1:
        print("Vamos cadastrar")
        indice = 0 

        while indice < len(notas):
            notas[indice] = float(input("Digite a nota do aluno" + str(indice + 1) + ": "))
            indice += 1 

    elif 
    



media = media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4

print(f"Média: {media:.2f}")

if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")


















notas = [-1, -1, -1, -1]

opcao = -1

while opcao != 0:
    print("""
[1] - Cadastrar nota
[2] - Média aritmética e situação final
[0] - Sair
""")

    opcao = int(input("Digite a opção escolhida: "))

    if opcao == 1:
        print("Vamos cadastrar")
        indice = 0

        while indice < len(notas):
            notas[indice] = float(
                input("Digite a nota do aluno " + str(indice + 1) + ": ")
            )
            indice += 1

    elif opcao == 2:
        media = sum(notas) / len(notas)

        print("Média:", media)

        if media >= 7:
            print("Situação: Aprovado")
        elif media >= 5:
            print("Situação: Recuperação")
        else:
            print("Situação: Reprovado")

    elif opcao == 0:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")
