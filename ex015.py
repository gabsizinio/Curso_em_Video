km = float(input("Quantos Km rodados ? "))
dias = int(input("Quantos dias alugados ? "))
preco = (60 * dias) + (0.15 * km)
print("O total a pagar é R$ {:.2f}.".format(preco))
