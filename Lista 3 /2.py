# 2 – Crie um programa que leia 4 notas de um(a) determinado(a) estudante. Após a leitura
# de todas notas, exiba a média aritmética simples e a situação final (aprovado(a) ou
# reprovado(a)).

notas = []

notas.append(float(input("Digite a 1ª nota: ")))
notas.append(float(input("Digite a 2ª nota: ")))
notas.append(float(input("Digite a 3ª nota: ")))
notas.append(float(input("Digite a 4ª nota: ")))

media = media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4

print(f"Média: {media:.2f}")

if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
