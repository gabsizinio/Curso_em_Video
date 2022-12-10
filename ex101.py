def voto(a):
    res = 2021 - a
    vot = "Sim"
    if res < 16:
        return f"Com {res} anos: VOTO NEGADO"
    elif 16 <= res < 18 or res >= 65:
        return f"Com {res} anos: VOTO OPCIONAL"
    elif 18 <= res < 65:
        return f"Com {res} anos: VOTO ORIGATÓRIO"


print("-" * 30)
ano = int(input("Em qua ano você nasceu: "))
print(voto(ano))

