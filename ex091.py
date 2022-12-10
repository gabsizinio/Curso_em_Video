from random import randint
from time import sleep
dad = dict()
cont = 1
lis = list()
lis1 = list()
cont2 = 0
for c in range(1, 5):
    val = randint(1, 6)
    print(f"o jogador {c} tirou {val}")
    sleep(0.5)
    dad[f"Jogador {c}"] = val
print("-=" * 40)
print("== Ranking dos Jogadores ==")
for item in sorted(dad, key=dad.get):
    lis.append(dad[item])
lis.sort(reverse=True)
for k, v in dad.items():
    lis1.append(k)
    lis1.append(v)
for co in lis:
    ind = lis1.index(co)
    print(f"O {cont}°Lugar é {lis1[ind - 1]} com {co}.")
    sleep(0.5)
    lis1.remove(lis1[ind - 1])
    lis1.remove(co)
    cont = cont + 1





