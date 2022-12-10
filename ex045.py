from time import sleep
from random import choice
print("\033[1;33m-=-" * 20)
print("\033[1;33m                      JOKENPÔ")
print("\033[1;33m-=-" * 20)
lista = ["PEDRA", "PAPEL", "TESOURA"]
comp = choice(lista)
hum = str(input("PEDRA, PAPEL OU TESOURA ? ")).upper()
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO !!!")
if comp == "PEDRA":
    print("COMPUTADOR JOGA PEDRA !")
    if hum == "PAPEL":
        print("VOCÊ GANHOU !")
    if hum == "TESOURA":
        print("EU GANHEI !")
    if hum == "PEDRA":
        print("EMPATOU !")
elif comp == "PAPEL":
    print("COMPUTADOR JOGA PAPEL !")
    if hum == "PAPEL":
        print("EMPATOU !")
    if hum == "TESOURA":
        print("VOCÊ GANHOU !")
    if hum == "PEDRA":
        print("EU GANHEI !")
else:
    print("COMPUTADOR JOGA TESOURA !")
    if hum == "PAPEL":
        print("EU GANHEI")
    if hum == "PEDRA":
        print("VOCÊ GANHOU !")
    if hum == "TESOURA":
        print("EMPATOU !")
