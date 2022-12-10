from time import sleep


def contador2(f, g, h):
    for t in range(f, g - 1, -1 * h):
        print(t, " ", end="")
        sleep(0.5)
    print("FIM!")


def contador(a, b, c):
    for d in range(a, b + 1, c):
        print(d, " ", end="")
        sleep(0.5)
    print("FIM!")


def linhas():
    print("-=" * 18)


linhas()
print("Contagem de 1 até 10 de 1 em 1:")
contador(1, 10, 1)
linhas()
print("Contagem de 10 até 0 de 2 em 2:")
contador(10, -2, -2)
linhas()
print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input("Fim:    "))
pas = int(input("Passo:  "))
linhas()
if "-" not in str(pas) and pas != 0:
    print(f"Contagem de {ini} até {fim} de {pas} em {pas}.")
    if ini < fim:
        contador(ini, fim, pas)
    elif ini > fim:
        contador2(ini, fim, pas)
if "-" in str(pas) and pas != 0:
    print(f"Contagem de {ini} até {fim} de {pas} em {pas}.")
    contador(ini, fim - 2, pas)
if pas == 0 and ini < fim:
    pas = 1
    print(f"Contagem de {ini} até {fim} de {pas} em {pas}.")
    contador(ini, fim, 1)
if pas == 0 and ini > fim:
    pas = -1
    print(f"Contagem de {ini} até {fim} de {pas} em {pas}.")
    contador2(ini, fim, 1)
