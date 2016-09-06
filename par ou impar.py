print ( 30 * '-')
print (" \n    Jogo do par ou impar     \n")
print (30 * '-')
try:
    escolha = str(input("Escolha par ou impar: "))
except ValueError:
    print ("espaço vazio")
dedos = int(input("Escolha o numero de dedos: "))
if escolha == "":
        print ("espaço vazio")
import random
maquina = random.randrange(0, 10)

print ("voce escolheu %s" %escolha)
print (" voce jogou %d e a maquina jogou %d" %(dedos, maquina))
print (" deu o numero %d" %(dedos + maquina))


if escolha == "par":
    if ((dedos + maquina) % 2) == 0:
        print (" voce venceu!!")
    else:
        print ("voce perdeu! ")
    
if escolha == "impar":
    if ((dedos + maquina) % 2) != 0:
        print (" voce venceu!!")
    else:
        print ("voce perdeu! ")


