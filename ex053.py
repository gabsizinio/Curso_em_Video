fra = str(input("Digite uma frase: "))
fra3 = fra[::-1]
fra2 = fra.replace(" ", "")[::-1]
print("O inverso de {} é {}.".format(fra, fra3))
if fra.replace(" ", "")[::-1] == fra2:
    print("Essa frase é um palíndromo.")
else:
    print("Essa frase não é um palíndromo.")
