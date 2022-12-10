num = int(input("Digite um número que você quer saber se é primo: "))
div = 0
s = 0
for div in range(1, num + 1):
    if num % div == 0:
        s = s + 1
if s == 2:
    print("O número {} possui {} divisores,logo é primo !".format(num, s))
else:
    print("O número {} possui {} divisores, logo não é primo !".format(num, s))
