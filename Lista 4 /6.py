# 6 – Elabore um programa que funcionará como um cadastro notas de um estudante. Seu
# programa deve permitir que notas sejam cadastradas ou removidas (através do seu
# índice, pois podem haver notas repetidas), conforme a solicitação do usuário. Também
# deve ser possível exibir a lista com todas as notas cadastradas, porém, o programa deve
# avisar o usuário caso a lista esteja vazia. O programa também deve ter uma opção para
# calcular a média do aluno e exibir sua situação (aprovado se média for maior ou igual a 6
# e reprovado, caso contrário). Crie um menu, conforme abaixo, para permitir a interação
# com o seu programa:
# Notas
# -----
# 1 - Cadastrar
# 2 - Excluir
# 3 - Listar
# 4 - Calcular média
# 0 - Sair
# Opção:

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
        indice = 0 
        while indice < len(notas):
            print(indice," posição, ", notas[indice], " nota")
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

            # calcular a média
            # mostrar a média

            # verificar se média >= 6
            # aprovado ou reprovado
        

    elif opcao == 0:
        print("Programa encerrado.")

                                
