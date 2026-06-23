deposito = float(input("Digite o valor do depósito mensal: "))
saldo = 0 
juros = 0.5 / 100

contador = 1 

while contador <= 24: 
    saldo += deposito 
    saldo = saldo + (saldo * juros)

    print("Mês", contador, " - Saldo: R$", saldo)

    contador += 1 

# # Valor depositado todo mês
# deposito = float(input("Digite o valor do depósito mensal: "))

# # Saldo inicial da poupança
# saldo = 0

# # Taxa de juros de 0,5% ao mês
# juros = 0.5 / 100

# # Contador começa em 1
# i = 1

# # Repete durante 24 meses
# while i <= 24:

#     # Adiciona o depósito ao saldo
#     saldo += deposito

#     # Aplica os juros sobre o saldo
#     saldo = saldo + (saldo * juros)

#     # Exibe o saldo acumulado no mês
#     print("Mês", i, "- Saldo: R$", saldo)

#     # Aumenta i em 1
#     # É o mesmo que: i = i + 1
#     i += 1