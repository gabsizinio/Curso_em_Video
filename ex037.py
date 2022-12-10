print("-=-" * 20)
print("                   CONVERSOR NUMÉRICO")
print("-=-" * 20)
num = int(input("DIGITE UM NÚMERO INTEIRO:"))
base = int(input("(1) PARA BINÁRIO \n(2) PARA OCTAL \n(3) PARA HEXADECIMAL \nPARA QUE BASE VOCÊ QUER CONVERTER: "))
if base == 1:
    print("O número {} convertido para binário ficará {}.".format(num, bin(num)[2:]))
elif base == 2:
    print("O número {} convertido para base octal ficará {}.".format(num, oct(num)[2:]))
elif base == 3:
    print("O número {} convertido para base hexadecimal ficará {}.".format(num, hex(num)[2:]))
else:
    print("Você digitou um número inválido, tente novamente.")