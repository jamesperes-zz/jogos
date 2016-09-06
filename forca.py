import time
import random

print ( 30 * '-')
print (" \n    Jogo da forca    \n")
print (30 * '-')

itens_fruta = ["banana", "abacaxi", "maca"]

fruta = random.choice(itens_fruta)

print ("o numero de letras e: %s " %(len(fruta)))

letra_1 = str(input("digite uma letra: "))
k = 0
troca = ""
while k < len(fruta):
    if letra in fruta:
        troca = troca + letra
    else:
        break

print ("%s" %troca)

time.sleep (5)
