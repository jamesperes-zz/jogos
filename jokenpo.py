print ( 30 * '-')
print (" \n    Jogo Jokenpo     \n")
print (30 * '-')

soma1 = 0
soma2 = 0

while soma1 < 3 and soma2 < 3 :

    jogada1 = str(input("jogue pedra, papel ou tesoura: "))
    print (" ")
    itens = ["pedra", "papel", "tesoura"]
    import random 
    jogada2 = random.choice(itens)

    print ("%s"%jogada1)
    print ("%s"%jogada2)
    print (" ")

    if jogada1 == jogada2:
        print ("deu empate")
        print ("vc já ganhou %s e perdeu %s partidas" %(soma1, soma2))
        print (" ")
    elif jogada1 == ("papel") and jogada2 == ("tesoura"):
        print ("Voce perdeu")
        soma2 = soma2 + 1
        print ("vc já ganhou %s e perdeu %s partidas" %(soma1, soma2))
        print (" ")
        

    elif jogada1 == ("papel") and jogada2 == ("pedra"):
        print ("Voce Ganhou!")
        soma1 = soma1 + 1
        print ("vc já ganhou %s e perdeu %s partidas" %(soma1, soma2))
        print (" ")
        

    elif jogada1 == ("pedra") and jogada2 == ("tesoura"):
        print ("Voce Ganhou")
        soma1 = soma1 + 1
        print ("vc já ganhou %s e perdeu %s partidas" %(soma1, soma2))
        print (" ")
        

    elif jogada1 == ("pedra") and jogada2 == ("papel"):
        print ("Voce perdeu")
        soma2 = soma2 + 1
        print ("vc já ganhou %s e perdeu %s partidas" %(soma1, soma2))
        print (" ")
        

    elif jogada1 == ("tesoura") and jogada2 == ("papel"):
        print ("Voce Ganhou")
        soma1 = soma1 + 1
        print ("vc já ganhou %s e perdeu %s partidas" %(soma1, soma2))
        print (" ")
        

    elif jogada1 == ("tesoura") and jogada2 == ("pedra"):
        print ("Voce perdeu")
        soma2 = soma2 + 1
        print ("vc já ganhou %s e perdeu %s partidas" %(soma1, soma2))
        print (" ")
        

if soma1 == 3:
    print ("voce ganhou a partida")
elif soma2 == 3:
    print ("voce perdeu a partida")
    
