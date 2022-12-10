l1 = [[], [], []]
l2 = [[], [], []]
l3 = [[], [], []]
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
