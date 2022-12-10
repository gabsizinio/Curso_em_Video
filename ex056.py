s = 0
nm = 0
hv = "i"
maior = 0
for c in range(1, 5):
    print("----------- {}° ----------".format(c))
    nome = str(input("Nome: ")).capitalize().strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: (M/F) ")).upper().strip()
    s = s + idade
    if idade > maior:
        maior = idade
        hv = nome
    if idade < 21 and sexo == "F":
        nm = nm + 1
print("A média de idade do grupo é {} anos.".format(s / 4))
print("O homem mais velho é o {} e tem {} anos.".format(hv, maior))
print("O n° de mulheres com menos de 21 anos é {}.".format(nm))
