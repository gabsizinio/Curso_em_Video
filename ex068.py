from random import randint

c = 0
print("-=-" * 20)
print("                      PAR OU ÍMPAR")
print("-=-" * 20)
while True:
    val = int(input("Diga um valor: "))
    vol = ' '
    while vol not in "PpTi":
        vol = str(input("Par ou Ímpar [P/I]: ")).strip().upper()
    vel = randint(0, 10)
    if vol == "P":
        if (val + vel) % 2 == 0:
            res = "VENCEU"
            print(f"Você jogou {val} e o computador {vel}.Total de {val + vel} DEU PAR")
            print("-" * 40)
            print(f"Você {res}!")
            print("-=-" * 20)
            c = c + 1
        else:
            res = "PERDEU"
            print(f"Você jogou {val} e o computador {vel}.Total de {val + vel} DEU ÍMPAR")
            print("-" * 40)
            print(f"Você {res}!")
            print("-=-" * 20)
    else:
        if (val + vel) % 2 == 0:
            res = "PERDEU"
            print(f"Você jogou {val} e o computador {vel}.Total de {val + vel} DEU PAR")
            print("-" * 40)
            print(f"Você {res}!")
            print("-=-" * 20)
        else:
            res = "VENCEU"
            print(f"Você jogou {val} e o computador {vel}.Total de {val + vel} DEU ÍMPAR")
            print("-" * 40)
            print(f"Você {res}!")
            print("-=-" * 20)
            c = c + 1
    if res == "PERDEU":
        break
print(f"GAME OVER. Você venceu {c} vezes.")
