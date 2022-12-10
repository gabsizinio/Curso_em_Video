while True:
    print("-" * 40)
    val = int(input("Quer ver a tabuada de qual valor ? "))
    print("-" * 40)
    if "-" in str(val):
        break
    for c in range(1, 11):
        print(f"{val} x {c} = {val * c}")
print("PROGRAMA TABUADA ENCERRADO.")
