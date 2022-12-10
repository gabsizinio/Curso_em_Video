def leiaInt(a):
    print("-" * 30)
    while True:
        try:
            b = int(input(f"{a}"))
        except (ValueError, TypeError):
            print("\033[0;31mERRO por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[0;31mEntrada de dados interrompido pelo usuário.\033[0;31m")
            return 0
        else:
            return b


def leiaFloat(a):
    print("-" * 30)
    while True:
        try:
            b = float(input(f"{a}"))
        except (ValueError, TypeError):
            print("\033[0;31mERRO por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[0;31mEntrada de dados interrompido pelo usuário.\033[0;31m")
            return 0
        else:
            return b


num = leiaInt("Digite um Inteiro: ")
nom = leiaFloat("Digite um Real: ")
print(f"O valor inteiro digitado foi {num} e o real foi {nom}.")

