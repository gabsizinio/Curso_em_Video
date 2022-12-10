c = 0
s = 0
cont = 0
while c != 999:
    print("[999 para encerrar].")
    c = int(input("Digite um n°: "))
    print("-=-" * 20)
    if c != 999:
        s = s + c
        cont = cont + 1
print("Você digitou {} números, que somados totalizam {}.".format(cont, s))
