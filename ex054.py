s1 = 0
s2 = 0
for c in range(1, 8):
    ano = int(input("O ano de nascimento da {}° pessoa: ".format(c)))
    if ano > 2003:
        s1 = s1 + 1
    if ano <= 2003:
        s2 = s2 + 1
print("N° de maiores de idade: {}".format(s2))
print("N° de menores de idade: {}".format(s1))
