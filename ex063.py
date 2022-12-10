print("SEQUÊNCIA DE FIBONACCI:")
t = int(input("Qunatos termos você deseja ver: "))
c = 0
pro = 0
ant = 0
while c < t:
    print(pro, "->", end=" ")
    pro = pro + ant
    ant = pro - ant
    c = c + 1
    if pro == 0:
        pro = pro + 1
print("FIM")
