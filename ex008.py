val = float(input("Digite um valor em metros:"))
print("O valor de {} metros equivale a:".format(val))
print("{} mm \n {} cm \n {} dm \n {} m \n {} dam \n {} hm \n {} km \n".format(val * 1000, val * 100, val * 10, val, val * 0.1, val * 0.01, val * 0.001))
