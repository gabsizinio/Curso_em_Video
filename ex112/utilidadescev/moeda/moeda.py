def metade(a, v):
    if v:
        b = f"{a / 2:.2f}"
        return str(b).replace(".", ",")
    else:
        return a / 2


def dobro(a, v):
    if v:
        b = f"{a * 2:.2f}"
        return str(b).replace(".", ",")
    else:
        return a * 2


def aumentar(a, p, v):
    if v:
        b = f"{a + (a * (p/ 100)):.2f}"
        return str(b).replace(".", ",")
    else:
        return a + (a * (p / 100))


def diminiur(a, p, v):
    if v:
        b = f"{a * ((100 - p) / 100):.2f}"
        return str(b).replace(".", ",")
    else:
        return a * ((100 - p) / 100)


def moeda(a):
    b = f"{a:.2f}"
    return str(b).replace(".", ",")


def resumo(a, b, c):
    print("-" * 40)
    print(f"{'RESUMO DO VALOR':^40}")
    print("-" * 40)
    print(f"Preço analisado:   R${moeda(a):^1}")
    print(f"Dobro do preço:    R${dobro(a, True):^1}")
    print(f"Metade do preço:   R${metade(a, True):^1}")
    print(f"{b}% de aumento:    R${aumentar(a, b, True):^1}")
    print(f"{c}% de redução:    R${diminiur(a, c, True):^1}")
    print("-" * 40)
