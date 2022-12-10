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

