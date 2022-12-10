def fatorial(a=0, show=False):
    """
    ⟶ Calcula o Fatorial de um número.
    :param a: número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n
    """
    f = 1
    print("-" * 20)
    for c in range(a, 0, -1):
        f = f * c
    if show:
        for d in range(a, 1, -1):
            print(f"{d} x", end=" ")
        print("1 =", end=" ")
    print(f)
    return f


a = (fatorial(5, show=True))



