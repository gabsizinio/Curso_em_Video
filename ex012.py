print("PARABÉNS, VOCÊ GANHOU UM DESCONTO DE 5% NA SUA COMPRA !")
pre = float(input("DIGITE O VALOR DA SUA COMPRA: (R$) "))
print("COM O DESCONTO, O VALOR DE SUA COMPRA DE {} R$ PASSA A SER {:.2f} R$.".format(
    pre, pre * 0.95))
