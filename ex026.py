frase = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase {}.".format(frase.count("A"), frase))
print("A letra A aparece pela primeira vez no caractere {}.".format(frase.find("A") + 1))
var = frase[::-1]
print("A letra A aparece pela última vez no caractere {}.".format((len(frase)) - var.find("A")))
