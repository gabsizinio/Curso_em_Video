dad = dict()
lis = list()
c = 0
si = 0
lism = list()
while True:
    dad["Nome"] = str(input("Nome: ")).strip().capitalize()
    dad["Sexo"] = str(input("Sexo: [M/F] ")).upper().strip()
    while dad["Sexo"] not in "MF":
        print("Digite um códugo válido.")
        dad["Sexo"] = str(input("Sexo: [M/F] ")).upper().strip()
    dad["Idade"] = int(input("Idade: "))
    lis.append(dad.copy())
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()
    while resp not in "SN":
        print("Digite um código válido.")
        resp = str(input("Quer continuar? [S/N] ").upper().strip())
    c = c + 1
    if resp == "N":
        break
print("-=" * 40)
print(f"- O grupo tem {c} pessoas.")
for m in lis:
    si = si + m["Idade"]
print(f"- A média de idade é de {si / c:.2f} anos.")
for p in lis:
    if p["Sexo"] == "F":
        lism.append(p["Nome"])
print(f"- As mulheres cadastradas foram: {lism}")
print("- Lista de pessoas que estão acima da média:")
for g in lis:
    if g["Idade"] > si / c:
        print()
        print(f"O nome = {g['Nome']}; sexo = {g['Sexo']}; idade = {g['Idade']}.")
        print()
print("<< ENCERRADO >>")
