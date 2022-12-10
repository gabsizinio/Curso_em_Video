from time import sleep
v1 = int(input("1° valor: "))
v2 = int(input("2° valor: "))
c = 0
while c != 5:
    print("-=-" * 20)
    c = int(input(
        "[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos valores \n[5] "
        "Sair do programa \nQual operação você deseja realizar ? "))
    if c == 1:
        print("A soma de {} e {} é {}.".format(v1, v2, v1 + v2))
    if c == 2:
        print("O produto de {} e {} é {}.".format(v1, v2, v1 * v2))
    if c == 3:
        if v1 > v2:
            print("O 1°valor, {}, é maior que o 2° valor, {}.".format(v1, v2))
        if v1 < v2:
            print("O 2°valor, {}, é maior que o 1° valor, {}.".format(v2, v1))
        if v1 == v2:
            print("Os valores são iguais.")
    if c == 4:
        print("-=-" * 20)
        v1 = int(input("1° valor: "))
        v2 = int(input("2° valor: "))
    if c == 5:
        print("Finalizando...")
        sleep(3)
        print("-=-" * 20)
        print("Programa Finalizado.")
        print("Obrigado !")
