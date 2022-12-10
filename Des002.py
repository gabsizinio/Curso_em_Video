dia = int(input("Dia do seu aniversário:"))
mes = str(input("Mês do seu aniversário:")).capitalize()
ano = int(input("Ano de seu nascimento:"))
resp = str(input("Você nasceu no dia {} de {} de {} correto ?".format(dia, mes, ano)))
if resp == "sim":
    print("ok")
else:
    print("Ah, desculpa!")
