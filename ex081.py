valores = []
c = 0
resp = "S"
while resp == "S":
    valores.append(int(input("Digite um número: ")))
    c = c + 1
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()
print("-=" * 20)
print(f"Você digitou {c} elementos.")
print(f"Os valores em ordem decrescente são", end=" ")
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 não foi encontrado na lista.")
