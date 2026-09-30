# 1 – Crie uma classe chamada Livro com:
# • Atributos: titulo e autor.
# • Um método chamado descricao que retorna: "{titulo} foi escrito por {autor}."
# Teste criando um objeto e chamando o método para exibir a descrição.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self):
       return f"{self.titulo} foi escrito por {self.autor}"

livro1 = Livro("O principe cruel", "Holly Black")

print(livro1.descricao())







    
# class Aluno:
#     def __init__ (self, nome, idade):
#         self.nome = nome
#         self.idade = idade 

# Luis = Aluno("Luis Schalata", 16)
# Vitoria = Aluno("Vitoria Garcia", 17)
# Vitor = Aluno("Vitor Roberto", 16)

# alunos = [Luis, Vitoria, Vitor]

# for aluno in alunos: 
#     print("Aluno:", aluno.nome, "Idade:", aluno.idade)