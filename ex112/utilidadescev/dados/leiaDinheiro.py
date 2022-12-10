def leiadinheiro(a):
    b = str(input(f"{a} ")).strip()
    while True:
        if "," in b:
            b = b.replace(",", ".")
        if "." in b:
            b = b.replace(".", "1")
        if not b.isdigit():
            print(f"\033[0;31mERRO: '{b}' é um preço inválido!\033[m")
            b = str(input(a))
        else:
            b = b.replace("1", ".")
            break
    return float(b)
