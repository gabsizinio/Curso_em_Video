def leiaInt(a):
    print("-" * 30)
    while True:
        b = str(input(f"{a}"))
        if b.isdigit():
            return int(b)
        else:
            print("\033[0;31mERRO! Digite um número válido.\033[m  ")


num = leiaInt("Digite um número: ")
print(f"Você acbou de digutar o n° {num}.")


