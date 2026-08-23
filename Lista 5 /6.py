def tempo_total(horas, minutos):
    total = horas * 60 + minutos
    return total 

horas1 = int(input("Digite a quantidade de horas: "))
minutos1 = int(input("Digite a quantidade de minutos: "))

print("Tempo total:", tempo_total(horas1, minutos1))