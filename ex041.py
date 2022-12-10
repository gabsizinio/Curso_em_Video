print("-=-" * 20)
print("           CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
print("-=-" * 20)
ano = int(input("Ano de nascimento: "))
idade = 2021 - ano
if idade <= 9:
    print("O atleta tem {} anos e sua categoria é MIRIM.".format(idade))
elif 9 < idade <= 14:
    print("O atleta tem {} anos e sua categoria é INFANTIL.".format(idade))
elif 14 < idade <= 19:
    print("O atleta tem {} anos e sua categoria é JUNIOR.".format(idade))
elif 20 <= idade <= 25:
    print("O atleta tem {} anos e sua categoria é SÊNIOR.".format(idade))
else:
    print("O atleta tem {} anos e sua categoria é MASTER.".format(idade))