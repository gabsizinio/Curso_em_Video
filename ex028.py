from time import sleep
from random import randint
print("--------------------------------")
print("      JOGO DA ADVINHAÇÃO")
print("--------------------------------")
num1 = 0
num2 = 1
while num1 != num2:
    num1 = randint(0, 5)
    num2 = int(input("Em que n° de 0 a 5 eu estou pensando ?"))
    print("Analisando...")
    sleep(3)
    if num1 == num2:
        print("VOCÊ ACERTOU !!")
        print("Parabéns, você venceu a máquina.")
    else:
        print("VOCÊ ERROU !!")
        print("Eu pensei no n° {}.".format(num1))
        print("Tente de novo.")
    print("------------------------------")


