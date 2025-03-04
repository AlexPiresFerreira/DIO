
# input do nome e nível do herói
nomeHeroi = input("Qual é o nome do grade herói: ")
quantidadeXP = int(input ("Quanto XP o grade herói tem: "))

if quantidadeXP < 1000: #Se XP for menor do que 1.000 = Ferro
    print(
        100 * "=", "\n", 
        f"O Herói de nome **{nomeHeroi}** está no nível de **Ferro**""\n",
        100 * "=", 
    )
elif quantidadeXP < 2000: #Se XP for entre 1.001 e 2.000 = Bronze
    print(
        100 * "=", "\n", 
        f"O Herói de nome **{nomeHeroi}** está no nível de **Bronze**""\n",
        100 * "=", 
    )
elif quantidadeXP < 5000: #Se XP for entre 2.001 e 5.000 = Prata
    print(
        100 * "=", "\n", 
        f"O Herói de nome **{nomeHeroi}** está no nível de **Prata**""\n",
        100 * "=", 
    )
elif quantidadeXP < 7000: #Se XP for entre 5.001 e 7.000 = Ouro
    print(
        100 * "=", "\n", 
        f"O Herói de nome **{nomeHeroi}** está no nível de **Ouro**""\n",
        100 * "=", 
    )
elif quantidadeXP < 8000: #Se XP for entre 7.001 e 8.000 = Platina
    print(
        100 * "=", "\n", 
        f"O Herói de nome **{nomeHeroi}** está no nível de **Platina**""\n",
        100 * "=", 
    )
elif quantidadeXP < 9000: #Se XP for entre 8.001 e 9.000 = Ascendente
    print(
        100 * "=", "\n", 
        f"O Herói de nome **{nomeHeroi}** está no nível de **Ascendente**""\n",
        100 * "=", 
    )
elif quantidadeXP < 10000: #Se XP for entre 9.001 e 10.000= Imortal
    print(
        100 * "=", "\n", 
        f"O Herói de nome **{nomeHeroi}** está no nível de **Imortal**""\n",
        100 * "=", 
    )
else: #Se XP for maior ou igual a 10.001 = Radiante
    print(
        100 * "=", "\n", 
        f"O Herói de nome **{nomeHeroi}** está no nível de **Radiante**""\n",
        100 * "=", 
    )

# Fim do programa
