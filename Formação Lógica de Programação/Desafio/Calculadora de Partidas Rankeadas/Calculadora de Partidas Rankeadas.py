
# input do nome e nível do herói
nomeHeroi = input("Qual é o nome do grade herói: ")
quantidadeXP = int(input ("Quanto XP o grade herói tem: "))
vit = int(input("Quantas vitória o grande herói teve: "))
der = int(input("Quantas derrotas o grande herói teve: "))

def xpHeroi(nomeHeroi, quantidadeXP):
    if quantidadeXP < 1000: #Se XP for menor do que 1.000 = Ferro
        return ("Ferro")
    elif quantidadeXP < 2000: #Se XP for entre 1.001 e 2.000 = Bronze
        return ("Bronze")
    elif quantidadeXP < 5000: #Se XP for entre 2.001 e 5.000 = Prata
        return ("Prata")
    elif quantidadeXP < 7000: #Se XP for entre 5.001 e 7.000 = Ouro
        return ("Ouro")
    elif quantidadeXP < 8000: #Se XP for entre 7.001 e 8.000 = Platina
        return("Platina")
    elif quantidadeXP < 9000: #Se XP for entre 8.001 e 9.000 = Ascendente
        return ("Ascendente")
    elif quantidadeXP < 10000: #Se XP for entre 9.001 e 10.000= Imortal
        return ("Imortal")
    else: #Se XP for maior ou igual a 10.001 = Radiante
        return ("Radiante")

def vitoria(vit,der):
    return (vit - der) 

def rankeada(vitoria):
    if qvit <= 10: #Se vitórias for menor do que 10 = Ferro
        return ("Ferro")
    elif qvit <= 20: #Se vitórias for entre 11 e 20 = Bronze
        return ("Bronze")
    elif qvit <= 50: #Se vitórias for entre 21 e 50 = Prata
        return ("Prata")
    elif qvit <= 80: #Se vitórias for entre 51 e 80 = Ouro
        return ("Ouro")
    elif qvit <= 90: #Se vitórias for entre 81 e 90 = Diamante
        return("Diamante")
    elif qvit <= 100: #Se vitórias for entre 91 e 100= Lendário
        return ("Lendário")
    else: #Se vitórias for maior ou igual a 101 = Imortal
        return ("Imortal")


xp = xpHeroi(nomeHeroi,quantidadeXP)
qvit = vitoria(vit,der)
ranke = rankeada(qvit)

print(f"O Herói de Nome **{nomeHeroi}** está no nível de **XP:{xp}** tem de saldo de **Vitória:{qvit}** **Ranke:{ranke}**")




# Fim do programa
