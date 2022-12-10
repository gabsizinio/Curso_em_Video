val = float(input("Valor da Compra: (R$) "))
fp = int(input("(1) À vista (Cheque/Dinheiro)\n(2) À vista (Cartão)\n(3) Parcelado\nQual a forma de pagamento ? "))
if fp == 1:
    print("Parabéns, você ganhou um desconto de 10% !")
    print("Seu produto de R$ {} sairá por R$ {}.".format(val, val * 0.9))
if fp == 2:
    print("Parabéns, você ganhou um desconto de 5% !")
    print("Seu produto de R$ {} sairá por R$ {}.".format(val, val * 0.95))
if fp == 3:
    resp = int(input("Deseja parcelar em quantas vezes (2x a 12x) ? "))
    if resp == 2:
        print("Seu produto sairá por R$ {}, e cada parcela sairá no valor R$ {}.".format(val, val / 2))
    else:
        print("Seu produto sairá por R$ {}, com 20 % de juros, e cada parcela sairá no valor de R$ {}.".format(val * 1.2, val
                                                                                                         * 1.2 / resp))
else:
    print("Você digitou um n° inválido, tente novamente.")