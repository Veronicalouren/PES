# valor_total = int(input("Digite o valor total da compra: "))
# if valor_total >= 100: 
#     print(" Você ganhou um cupom de desconto! ")
# else:
#     print(" Continue comprando para ganhar um cupom de desconto! ")


# import random 
# escolha_jogador = input ("Diga pedra,papel ou tesoura: ")
# escolhido = random.randit(1, 3)

# if escolhido == 1:
#     escolha_maquina = "pedra"
# elif escolhido == 2:
#     escolha_maquina = "papel"
# elif escolhido == 3:
#     escolha_maquina = "tesoura"


class Aluno:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade 

Luis = Aluno("Luis Schalata", 16)
Vitoria = Aluno("Vitoria Garcia", 17)
Vitor = Aluno("Vitor Roberto", 16)

alunos = [Luis, Vitoria, Vitor]

for aluno in alunos: 
    print("Aluno:", aluno.nome, "Idade:", aluno.idade)

