# 1 - Implemente um programa com um cadastro de idades de 6 alunos utilizando lista. O
# programa deve solicitar as idades dos 6 alunos. Após informar todas as idades, deve-se
# apresentar apenas as idades que forem maiores ou iguais a 16.

idades = [1, 2, 3, 4, 5, 6]

indice = 0 
while indice < len(idades):
    idades[indice] = int(input("Digite valor: "))
    #print("Item da lista =>", idades[indice])
    indice = indice + 1


for idade in idades:
    print("Valor é =>", idade)