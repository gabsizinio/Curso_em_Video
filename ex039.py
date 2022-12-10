print("-=-" * 20)
print("            SERVIÇO DE ALISTAMENTO MILITAR")
print("-=-" * 20)
gen = str(input("Gênero: (M/F) "))
if gen == "F":
    print("Você não precisa se alistar.")
if gen == "M":
    ano = int(input("Ano de nascimento: "))
    idade = 2021 - ano
    if idade < 18:
        print("Você ainda não precisa se alistar, faltam {} anos.".format(18 - idade))
        print("Seu alistamento será em {}.".format(2021 + (18 - idade)))
    elif idade == 18:
        print("Você está na idade de se alistar, procure a junta militar mais próxima.")
    elif idade > 18:
        print("Você passou da idade de se alistar em {} anos, se você ainda não se alistou, procure a junta militar "
              "mais próxima.".format(idade - 18))
        print("O seu alistamento foi em {}.".format(2021 - (idade - 18)))
