val = []
num = int(input("Digite um valor: "))
val.append(num)
print("Adicionado ao final da lista...")
num = int(input("Digite um valor: "))
if len(val) == 1 and num >= val[0]:
    print("Adicionado ao final da lista...")
    val.insert(1, num)
if len(val) == 1 and num < val[0]:
    print("Adicionado na posição 0...")
    val.insert(0, num)
num = int(input("Digite um valor: "))
if len(val) == 2 and num >= val[1]:
    print("Adicionado ao final da lista...")
    val.insert(2, num)
if len(val) == 2 and val[0] <= num < val[1]:
    print("Adicionado na posição 1...")
    val.insert(1, num)
if len(val) == 2 and num < val[0]:
    print("Adicionado na posição 0...")
    val.insert(0, num)
num = int(input("Digite um valor: "))
if len(val) == 3 and num >= val[2]:
    print("Adicionado ao final da lista...")
    val.insert(3, num)
if len(val) == 3 and val[1] <= num < val[2]:
    print("Adicionado na posição 2...")
    val.insert(2, num)
if len(val) == 3 and val[0] <= num < val[1]:
    print("Adicionado na posição 1...")
    val.insert(1, num)
if len(val) == 3 and num < val[0]:
    print("Adicionado na posição 0...")
    val.insert(0, num)
num = int(input("Digite um valor: "))
if len(val) == 4 and num >= val[3]:
    print("Adicionado ao final da lista...")
    val.insert(4, num)
if len(val) == 4 and val[2] <= num < val[3]:
    print("Adicionado na posição 3...")
    val.insert(3, num)
if len(val) == 4 and val[1] <= num < val[2]:
    print("Adicionado na posição 2...")
    val.insert(2, num)
if len(val) == 4 and val[0] <= num < val[1]:
    print("Adicionado na posição 1...")
    val.insert(1, num)
if len(val) == 4 and num < val[0]:
    print("Adicionado na posição 0...")
    val.insert(0, num)
print("-=" * 20)
print(f"Os valores digitados em ordem foram {val}")
