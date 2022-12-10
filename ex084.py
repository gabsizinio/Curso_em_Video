c = 0
pes = list()
dad = list()
maior = 0
menor = 5000
lismaior = list()
lismenor = list()
nomema = list()
nomeme = list()
while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    c = c + 1
    pes.append(nome)
    pes.append(peso)
    dad.append(pes[:])
    for p in dad:
        if p[1] >= maior:
            maior = p[1]
            lismaior.append(p[0])
            lismaior.append(p[1])
        if p[1] <= menor:
            menor = p[1]
            lismenor.append(p[0])
            lismenor.append(p[1])
    pes.clear()
    dad.clear()
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()
    if resp == "N":
        break
print("-=" * 30)
print(f"Ao todo, você cadastrou {c} pessoas.")
for m, n in enumerate(lismaior):
    if n == maior:
        nomema.append(lismaior[m - 1])
for p, o in enumerate(lismenor):
    if o == menor:
        nomeme.append(lismenor[p - 1])
print(f"O maior peso é de {maior} Kg, peso de {nomema}.")
print(f"O menor peso é de {menor} Kg, peso de {nomeme}.")
