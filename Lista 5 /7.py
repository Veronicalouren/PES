def moldura(linhas=1, colunas=1):

    if linhas < 1:
        linhas = 1

    if linhas > 20:
        linhas = 20

    if colunas < 1:
        colunas = 1

    if colunas > 20:
        colunas = 20

    print("+" + "-" * colunas + "+")

    indice = 1

    while indice <= linhas:
        print("|" + " " * colunas + "|")
        indice += 1

    print("+" + "-" * colunas + "+")


linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

moldura(linhas, colunas)

    
