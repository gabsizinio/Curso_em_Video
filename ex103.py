def ficha(a="<desconhecido>", b="0"):
    print("-" * 30)
    print(f"O jogador {a} fez {b} gol(s) no campeonato.")


print("-" * 30)
jog = str(input("Nome do jogador: ")).title()
if jog == "":
    jog = "<desconhecido>"
gol = str(input("Número de gols: "))
if not gol.isnumeric():
    gol = "0"
ficha(jog, gol)

