num = int(input("Digite o n° que você quer saber o fatorial: "))
c = num
f = 1
if num == 0:
    print("0! é igual a 1.")
else:
    while c > 0:
        f = f * c
        c = c - 1
    print("{}! é igual a {}.".format(num, f))
