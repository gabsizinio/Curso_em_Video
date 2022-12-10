maior = 0
menor = 99999999
for c in range(1, 6):
    peso = float(input("Digite o peso do {}° indivíduo: (Kg) ".format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print("O maior peso registrado foi de {} Kg.".format(maior))
print("O menor peso registrado foi de {} Kg.".format(menor))
