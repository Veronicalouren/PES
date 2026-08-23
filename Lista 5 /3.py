def calcular_volume (raio, altura):
    volume = 3.14 * raio ** 2 * altura 
    return volume 

raio = float(input("Digite o raio do cilindro em metros: "))
altura = float(input("Digite a altura do cilindo em metros: "))

volume = calcular_volume (raio, altura)

print("O volume do cilindro é: ", volume)