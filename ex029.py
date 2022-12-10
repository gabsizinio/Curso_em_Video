print("--------------------------")
print("          DETRAN")
print("--------------------------")
vel = float(input("DIGITE A VELOCIDADE DO CARRO: "))
if vel > 80:
    print("VOCÊ FOI MULTADO, POR EXCEDER O LIMITE DE 80KM/H !")
    print("SUA MULTA TEM O VALOR DE {} R$.".format((vel - 80) * 7))
    print("SEJA MAIS RESPONSÁVEL NO TRÂNSITO.")
else:
    print("VOCÊ NÃO FOI MULTADO.")
    print("PARABÉNS, CONTINUE ASSIM !")
