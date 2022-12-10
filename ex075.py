#v1 = int(input("Digite um número: "))
#v2 = int(input("Digite outro número: "))
#v3 = int(input("Digite mais um número: "))
#v4 = int(input("Digite o último número: "))
#num = (v1, v2, v3, v4)
num = (int(input("Digite um número: ")), int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")), int(input("Digite o último número: ")))

print(f"Você digitou os valores {num}.")
print(f"O 9 aparece {num.count(9)} vezes.")
if 3 in num:
    print(f"O 3 aparece primeiro na posição {num.index(3) + 1}.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
print("Os pares digitados foram", end=" ")
for n in num:
    if n % 2 == 0:
        print(n, end= " ")
