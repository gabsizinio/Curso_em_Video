num = [[], []]
for c in range(1, 8):
    val = int(input(f"Digite o {c}° valor: "))
    if val % 2 == 0:
        num[0].append(val)
    else:
        num[1].append(val)
num[0].sort()
num[1].sort()
print("-=" * 30)
print(f"Os valores pares digitados foram: {num[0]}")
print(f"Os valores ímpares digitados foram: {num[1]}")
