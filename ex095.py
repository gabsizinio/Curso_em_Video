dad = dict()
lis = list()
tot = 0
lis40 = list()
c = 0
while True:
    tot = 0
    dad["Nome"] = str(input("Nome do Jogador: ")).upper().strip()
    np = int(input(f"Quantas partidas {dad['Nome']} jogou. "))
    for c4 in range(0, np):
        gol = int(input(f"Quantos gols na partida {c4}? "))
        tot = tot + gol
        lis.append(gol)
        dad["Lista"] = lis[:]
    dad["Total"] = tot
    lis40.append(dad.copy())
    lis.clear()
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()
    if resp == "N":
        break
print("-=" * 22)
print("cod", end=" ")
for i in dad.keys():
    print(f'{i:<15}', end=" ")
print()
print("-" * 40)
for k, v in enumerate(lis40):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(lis40):
        print(f"ERRO! Não existe jogador com código {busca}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {lis40[busca]['Nome']}: ")
        for i, g in enumerate(lis40[busca]["Lista"]):
            print(f"    No jogo {i} fez {g} gols.")

    print("-" * 40)
print("<< VOLTE SEMPRE >>")

