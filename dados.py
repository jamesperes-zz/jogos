import random


jogada1 = int(input("digite o numero de 1 a 6 : "))

jogada2 = random.randrange(1, 6)

if jogada1 == jogada2:
    print ("voce ganhou!")

else:
    print ("voce perdeu")


    
print ("O dado deu o numero %d" %jogada2)
