exp = str(input("Digite uma expressão: "))
npa = exp.count("(")
npf = exp.count(")")
if npf != npa:
    print("Sua expressão está errada!")
else:
    print("Sua expressão está válida!")
