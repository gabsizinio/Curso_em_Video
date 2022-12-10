num = c = s = 0
while True:
    num = int(input("Digite um valor: [999 para parar] "))
    if num == 999:
        break
    s = s + num
    c = c + 1
print(f"A soma dos {c} números é {s} !")

