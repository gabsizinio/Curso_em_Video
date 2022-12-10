pbar = "i"
bar = 999999999999999999
ppbar = p1000 = tot = 0
while True:
    nom = str(input("Nome do produto: ")).strip().title()
    pre = float(input("Preço R$: "))
    tot = tot + pre
    if pre > 1000:
        p1000 = p1000 + 1
    if pre < bar:
        pbar = nom
        ppbar = pre
    res = " "
    while res not in "SsNn":
        res = str(input("Quer continuar ? [S/N]")).strip().upper()
    if res == "N":
        break
print("-------- FIM DO PROGRAMA --------")
print(f"O total da compra foi R$ {tot}.")
print(f"Temos {p1000} produtos custando mais de R$ 1000.")
print(f"O produto mais barato foi {pbar} que custa R$ {ppbar}.")
