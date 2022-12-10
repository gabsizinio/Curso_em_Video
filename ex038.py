num = int(input("1° valor: "))
num1 = int(input("2° valor: "))
if num > num1:
    print("O 1° valor, {}, é maior.".format(num))
    print("O 2° valor, {}, é menor .".format(num1))
if num < num1:
    print("O 2° valor, {}, é maior.".format(num1))
    print("O 1° valor, {}, é menor .".format(num))
if num == num1:
    print("Não existe maior valor, os dois são iguais.")
