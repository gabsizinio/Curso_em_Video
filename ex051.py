pt = int(input("1° termo da P.A: "))
r = int(input("Razão da P.A: "))
print("Os 10 primeiros termos dessa P.A:")
for c in range(1, 11,):
    print(pt, end = " -> ")
    pt = pt + r
