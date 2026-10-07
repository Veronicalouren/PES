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


pessoas = []

while True:

    print("""Cadastro de Pessoas
          -------------------
          1 - Cadastrar
          2 - Listar
          3 - Excluir
          4 - Atualizar
          0 - Sair""")

    opcao = int(input("Opção: "))

    if opcao == 1:

        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))

        pessoa = Pessoa(nome, idade, altura, peso)

        pessoas.append(pessoa)

    elif opcao == 2:

        for pessoa in pessoas:
            pessoa.exibir()
            print(pessoa.mostrar_imc())
    
    elif opcao == 3:
        nome = input("Digite o nome da pessoa que deseja excluir: ")
        for pessoa in pessoas:
            if pessoa.nome == nome:
                pessoas.remove(pessoa)
                print("Pessoa excluída!")
    
    elif opcao == 4:
        nome = input("Digite o nome da pessoa que você deseja atualizar os dados: ")
        for pessoa in pessoas:
            if pessoa.nome == nome:
                pessoa.idade = int(input("Digite a nova idade: "))
                pessoa.altura = float(input("Digite a nova altura: "))
                pessoa.peso = float(input("Digite o novo peso: " ))
                print("Pessoa atualizada!")
                                   
    elif opcao == 0:
        break