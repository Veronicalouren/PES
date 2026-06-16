nome_usuario = (input("Digite seu nome de usuário:" ))
senha = int(input("Digite sua senha: "))

if nome_usuario == "admin" and senha == 12345: 
    print("Login bem-sucedido")
else:
    print("Nome de usuário ou senha incorretos")