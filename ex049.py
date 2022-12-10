n = int(input("Digite o número que você quer saber a tabuada: "))
n2 = int(input("Até onde você quer que a tabuada vá ? "))
for c in range(0, n2 + 1):
    print("{} x {} = {}".format(n, c, n * c))
