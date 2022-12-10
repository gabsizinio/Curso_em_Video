bole = [[], [], [], []]
c1 = 0
c2 = 0
while True:
    nome = str(input("Nome: ")).capitalize().strip()
    bole[0].append(nome)
    n1 = float(input("Nota 1: "))
    bole[1].append(n1)
    n2 = float(input("Nota 2: "))
    bole[2].append(n2)
    c1 = c1 + 1
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()
    if resp == "N":
        break
print("-=" * 50)
print("No.", end="   ")
print("NOME", end="         ")
print("MÉDIA")
print("-" * 30)
for p in bole[0]:
    print(c2, end="    ")
    print(f"{p:<4}", end="     ")
    print(f"{(bole[1][c2] + bole[2][c2]) / 2:>8.1f}")
    c2 = c2 + 1
print("-" * 30)
while True:
    alu = int(input("Mostrar notas de qual aluno? {999 interrompe}: "))
    print(f"Notas de {bole[0][alu]} são {bole[1][alu], bole[2][alu]}")
    print("-" * 50)
    if alu == 999:
        break
print("<<< VOLTE SEMPRE >>>")
