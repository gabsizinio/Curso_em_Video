from random import randint
from time import sleep
print("-" * 30)
print("      JOGA NA MEGA SENA")
print("-" * 30)
num = int(input("Quantos jogos que você quer que eu sorteie? "))
ms = list()
print(f"-=-=-= SORTEANDO {num} JOGOS -=-=-=")
for c in range(1, num + 1):
    for a1 in range(0, 7):
        while True:
            val = randint(1, 60)
            if val not in ms:
                break
        ms.append(val)
    ms.sort()
    print(f"Jogo {c}: {ms}")
    sleep(0.5)
    ms.clear()
print("-=-=-=-=-= < BOA SORTE! > =-=-=-=-=-")
