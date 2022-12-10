from time import sleep
from random import randint
print("--------------------------------")
print("      JOGO DA ADVINHAÇÃO")
print("--------------------------------")
num2 = 1
s = 0
num1 = randint(0, 10)
while num1 != num2:
    num2 = int(input("Em que n° de 0 a 10 eu estou pensando ?"))
    print("Analisando...")
    sleep(3)
    if num1 == num2:
        print("VOCÊ ACERTOU !!")
        print("Parabéns, você venceu a máquina depois de {} rodadas.".format(s))
    if num1 > num2:
        print("Maior...tente novamente.")
        s = s + 1
    if num1 < num2:
        print("Menor...tente novamente.")
        s = s + 1
    print("------------------------------")
