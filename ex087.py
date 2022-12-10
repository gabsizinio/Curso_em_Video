l1 = [[], [], []]
l2 = [[], [], []]
l3 = [[], [], []]
pares = list()
sompar = 0
maior = 0
for c in range(0, 3):
    l1[c].append(int(input(f"Digite um valor para [0, {c}]: ")))
for p in range(0, 3):
    l2[p].append(int(input(f"Digite um valor para [1, {p}]: ")))
for z in range(0, 3):
    l3[z].append(int(input(f"Digite um valor para [2. {z}]: ")))
print("-=" * 30)
for a in l1:
    for g in a:
        print(f"[  {g:^5}  ]", end="")
print("")
for b in l2:
    for c in b:
        print(f"[  {c:^5}  ]", end="")
print("")
for d in l3:
    for e in d:
        print(f"[  {e:^5}  ]", end="")
print("")
print("-=" * 30)
for c1 in l1:
    for c2 in c1:
        if c2 % 2 == 0:
            pares.append(c2)
for c3 in l2:
    for c4 in c3:
        if c4 % 2 == 0:
            pares.append(c4)
for c5 in l3:
    for c6 in c5:
        if c6 % 2 == 0:
            pares.append(c6)
for a1 in pares:
    sompar = sompar + a1
som3col = l1[2][0] + l2[2][0] + l3[2][0]
for a2 in l2:
    for a3 in a2:
        if a3 > maior:
            maior = a3
print(f"A soma dos valores pares é {sompar}.")
print(f"A soma dos valores da terceira coluna é {som3col}.")
print(f"O maior valor da segunda linha é {maior}.")
