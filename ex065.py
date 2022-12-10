c = 0
resp = "i"
s = 0
maior = 0
menor = 9999999999999999

while resp != "N":
    print("-=-" * 20)
    num = int(input("Digite um n°: "))
    s = s + num
    c = c + 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    resp = str(input("Quer continuar ? (S/N) ")).upper().strip()
print("A soma de todos os {} números é {}.".format(c, s))
print("A média dos números é {:.2F}.".format(s / c))
print("O maior valor é {}.".format(maior))
print("O menor valor é {}.".format(menor))
