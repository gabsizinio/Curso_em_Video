num = int(input("Digite um número que você queira saber a taboada:"))
c = 0
s = "s"
print("=" * 20)
while s == "s":
    print("{} x {} = {}".format(num, c, (num * c)))
    c = c + 1
    if c % 10 == 0:
        s = str(input("Quer continuar ? (s/n)"))
    if s != "s":
        print("Ah, ok")
print("=" * 20)
