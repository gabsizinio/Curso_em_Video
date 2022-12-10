from random import randint
from time import sleep
cab = list()


def sorteia(num):
    print("Sorteando 5 valores da lista:", end=" ")
    for c in range(0, 5):
        val = randint(0, 10)
        print(val, end=" ")
        num.append(val)
        sleep(0.5)
    print("PRONTO!")


sorteia(cab)


def somapar(num):
    pos = 0
    lis = list()
    print(f"Somando os valores pares de {num}, temos", end=" ")
    for i in num:
        if i % 2 == 0:
            pos += i
    print(pos)



somapar(cab)
