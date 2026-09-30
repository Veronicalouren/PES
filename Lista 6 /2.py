2 – Crie uma classe chamada Carro com:
• Atributos: marca e cor.
• Um método chamado pintar que recebe uma nova cor como argumento e altera o
atributo cor para essa nova cor.
• Um método chamado mostrar_cor que retorna a cor atual do carro.
Teste criando um objeto, alterando sua cor com o método pintar e exibindo a nova cor
com mostrar_cor.

class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor 
    
    def pintar(self,nova_cor):
        self.cor = nova_cor 
    
    def mostrar(self):
        return self.cor
    



    class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self):
       return f"{self.titulo} foi escrito por {self.autor}"

livro1 = Livro("O principe cruel", "Holly Black")

print(livro1.descricao())