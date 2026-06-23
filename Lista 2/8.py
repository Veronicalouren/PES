divida = (float(input("Digite o valor da dívida: ")))
meses = int(input("Digite a quantidade de meses: "))
juros = 15.3 / 100

i = 1

while i <= meses:
    divida = divida + (divida * juros)
    i += 1 

print("Divida após", meses, "meses: R$", divida)

# Valor inicial da dívida
divida = 1000

# Taxa de juros mensal de 15,3%
juros = 15.3 / 100

# Quantidade de meses
meses = int(input("Digite a quantidade de meses: "))

# Contador começa em 1
i = 1

# Calcula a dívida mês a mês
while i <= meses:
    divida = divida + (divida * juros)

    # É o mesmo que: i = i + 1
    i += 1

# Exibe o valor final da dívida
print("Dívida após", meses, "meses: R$", divida)