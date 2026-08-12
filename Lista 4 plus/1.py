professores = [{
    "cod": "001",
    "nome": "Prof Tiago Paes"
}, {
    "cod": "002",
    "nome": "Prof Schalata"
}, {
    "cod": "003",
    "nome": "Prof Ignácio"

}]

def listar_todos_os_professores ():
    indice = 0 
    while indice < len(professores):
        prof = professores[indice]
        print("- Professor: " + prof["nome"] + " | Còdigo: " + prof["cod"])
        indice
opcao = -1 
while opcao != 0:
    print("""
          [1] Professor: adicionar
          [2] Professor: Alterar
          [3] Professor: Listar
          [4] Professor: Excluir
          [0] Sair 
""")

opcao = int(input("Me diga "))

if opcao == 1:
    cod = input("Qual é o código do professor? R: ")
    nome = input("Qual é o nome do professor? R: ")

    professores.append({
        "cod": cod,
        "nome": nome
    })
elif opcao == 4:
    indice = 0
    while indice < len(professores):    
        print("Professor: "+professores[indice]["nome"])
        indice += 1 