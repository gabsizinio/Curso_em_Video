valn = []
valp = []
vali = []
resp = "S"
while True:
    num = int(input("Digite um número: "))
    valn.append(num)
    if num % 2 == 0:
        valp.append(num)
    else:
        vali.append(num)
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()
    if resp == "N":
        break
print("-=" * 20)
print(f"A lista completa é {valn}")
print(f"A lista de pares é {valp}")
print(f"A lista de ímpares {vali}")
