nome = str(input("Digite o seu nome completo: ")).title().strip()
print("Seu nome só com letras maiúsculas: {}".format(nome.upper()))
print("Seu nome só com letras minúsculas: {}".format(nome.lower()))
nome1 = len(nome) - nome.count(" ")
print("Seu nome tem {} caracteres sem considerar os espaços.".format(nome1))
split = nome.split()
print("Seu 1° nome é {} e possui {} letras." .format(split[0], len(split[0])))

