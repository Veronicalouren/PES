quantidade = int(input("Digite a quantidade de notas: "))

soma = 0 

i = 1 

while i <= quantidade:
    nota = float(input("Digite a nota: "))
    soma += nota
    i += 1 

media = soma / quantidade 

print("Média final:", media)

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")


# Solicita a quantidade de notas
quantidade = int(input("Digite a quantidade de notas: "))

# Variável para armazenar a soma das notas
soma = 0

# Contador começa em 1
i = 1

# Repete até que todas as notas sejam digitadas
while i <= quantidade:

    # Solicita uma nota
    nota = float(input("Digite a nota: "))

    # Adiciona a nota à soma
    soma += nota

    # Aumenta i em 1
    # É o mesmo que: i = i + 1
    i += 1

# Calcula a média
media = soma / quantidade

# Exibe a média
print("Média final:", media)

# Verifica se o aluno foi aprovado ou reprovado
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")