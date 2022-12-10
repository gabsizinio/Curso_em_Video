valores = []
for c in range(0, 5):
    valores.append(int(input(f"Digite um número para a posição {c}: ")))
maior = 0
menor = 99999999999
posmaior = []
posmenor = []
for con, n in enumerate(valores):
    if n > maior:
        maior = n
    if n < menor:
        menor = n
for cont, c in enumerate(valores):
    if c == maior:
        posmaior.append(cont)
    if c == menor:
        posmenor.append(cont)
print("-=" * 20)
print(f"Você digitou os valores {valores}.")
print(f"O maior valor digitado foi {maior} nas posições {posmaior}.")
print(f"O menor valor digitado foi {menor} nas posições {posmenor}.")
