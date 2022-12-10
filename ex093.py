dad = dict()
lis = list()
tot = 0
dad["Nome"] = str(input("Nome do Jogador: ")).upper().strip()
np = int(input(f"Quantas partidas {dad['Nome']} jogou? "))
for c in range(0, np):
    gol = int(input(f"Quantos gols na partida {c}? "))
    tot = tot + gol
    lis.append(gol)
    dad["Lista"] = lis
dad["Total"] = tot
print("-=" * 30)
print(dad)
print("-=" * 30)
print(f"O campo nome tem o valor {dad['Nome']}.")
print(f"O campo gols tem o valor {dad['Lista']}.")
print(f"O campo total tem o valor {dad['Total']}.")
print("-=" * 30)
print(f"O jogador {dad['Nome']} jogou {np} partidas.")
for c2 in range(0, np):
    print(f"=> Na partida {c2}, fez {dad['Lista'][c2]} gols.")
print(f"Foi um total de {dad['Total']} gols.")

