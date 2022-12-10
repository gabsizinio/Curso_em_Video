sal = float(input("Digite o valor do seu salário: "))
if sal <= 1250:
    print("Você recebeu um aumento de 15%.")
    print("O seu salário de {} R$ passrá a ser {} R$.".format(sal, sal * 1.15))
else:
    print("Você recebeu um aumento de 10%.")
    print("O seu salário de {} R$ passará a ser {} R$.".format(sal, sal * 1.10))
