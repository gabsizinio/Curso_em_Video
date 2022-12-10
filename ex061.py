t1 = int(input("1° termo da P.A: "))
r = int(input("Razão da P.A: "))
c = 0
print("Os 10 primeiros termos da P.A:")
while c < 10:
    print(t1, "->", end=" ")
    t1 = t1 + r
    c = c + 1
print("FIM")
