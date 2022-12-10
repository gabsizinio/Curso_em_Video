cid = str(input("Qual o nome de sua cidade ? ")).title().strip()
cid1 = cid.split()
print("O nome de sua cidade começa com Santo ? {}".format("Santo" in cid1[0]))


