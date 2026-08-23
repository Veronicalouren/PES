def eh_digimon_ou_pokemon(nome): 
    if(nome == "metamon"):
        return "pokemon"
    
    if "mon" in nome: 
        return "digimon"
    else: 
        return "pokemon"

nome_bixo = input("Me diga o nome da criatura: ")
tipo = eh_digimon_ou_pokemon(nome_bixo)
if tipo == "pokemon":
    print("Muito legal seu monstrinho do pokemon")
    print("O meu favorito é a Eevee")
else:
    print("Não sei nada de digimon")