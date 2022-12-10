números = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in números:
        números.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado ! Não vou adicionar...")
    resp = str(input("Quer continuar ? [S/N] ")).upper().strip()
    if resp == "N":
        break
print("-=" * 20)
números.sort()
print(f"Você digitou os valores {números}.")
