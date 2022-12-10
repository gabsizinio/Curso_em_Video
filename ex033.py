num1 = int(input("1° número: "))
num2 = int(input("2° número: "))
num3 = int(input("3° número: "))
if num1 > num2 > num3:
    print("{} é o maior n°.".format(num1))
    print("{} é o menor n°.".format(num3))
if num1 > num3 > num2:
    print("{} é o maior n°.".format(num1))
    print("{} é o menor n°.".format(num2))
if num1 > num2 == num3:
    print("{} é o maior n°.".format(num1))
    print("{} é o menor n°.".format(num2))
if num2 > num1 > num3:
    print("{} é o maior n°.".format(num2))
    print("{} é o menor n°.".format(num3))
if num2 > num3 > num1:
    print("{} é o maior n°.".format(num2))
    print("{} é o menor n°.".format(num1))
if num2 > num1 == num3:
    print("{} é o maior n°.".format(num1))
    print("{} é o menor n°.".format(num3))
if num3 > num1 > num2:
    print("{} é o maior n°.".format(num3))
    print("{} é o menor n°.".format(num2))
if num3 > num2 > num1:
    print("{} é o maior n°.".format(num3))
    print("{} é o menor n°.".format(num1))
if num3 > num2 == num1:
    print("{} é o maior n°.".format(num3))
    print("{} é o menor n°.".format(num1))
if num1 == num2 == num3:
    print("Os números são iguais")
