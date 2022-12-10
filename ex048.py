cont = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = c + s
print("A soma de todos os {} solicitados é {}.".format(cont, s))
