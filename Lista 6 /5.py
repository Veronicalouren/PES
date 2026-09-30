# 5 – Crie uma classe chamada Pessoa com:
# • Atributos: nome, idade, altura e peso;
# • Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
# pessoa;
# • Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
# • Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
# Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
# estão corretos.

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome 
        self.idade = idade 
        self.altura = altura 
        self.peso = peso
    
    def exibir(self):
        print(self.nome, self.idade, self.altura, self.peso)
    
    def imc(self):
        return self.peso / (self.altura ** 2)
    
    def mostrar_imc(self):
        return f"{self.nome} - IMC: {self.imc():.2f}"


pessoa1 = Pessoa("Ana", 20, 1.70, 60)
pessoa2 = Pessoa("João", 25, 1.80, 80)
pessoa3 = Pessoa("Maria", 30, 1.60, 55)

pessoa1.exibir()
print(pessoa1.mostrar_imc())

pessoa2.exibir()
print(pessoa2.mostrar_imc())

pessoa3.exibir()
print(pessoa3.mostrar_imc())