t1 = int(input("1° termo: "))
r = int(input("Razão: "))
c = 0
c1 = 0
t2 = 1
print("Os 10 primeiros termos da P.A:")
while c < 10:
    print(t1, "->", end=" ")
    t1 = t1 + r
    c = c + 1
print("PAUSA")
while t2 != 0:
    t2 = int(input("\nMais quantos termos ? [0] Para encerrar."))
    if t2 != 0:
        while c < 10 + t2:
            print(t1, "...", end=" ")
            t1 = t1 + r
            c = c + 1
        print("PAUSA")
    if t2 == 0:
        print("A progressão se encerra com {} termos !".format(c))
