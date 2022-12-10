resp = "O"
while resp != "M" and resp != "F":
    resp = str(input("Informe seu sexo: (M/F) ")).upper().strip()[0]
    if resp != "M" and resp != "F":
        print("Dados inválidos, tente novamente.")
        print("-=-" * 20)
print("Obrigado, sexo {} registrado com sucesso.".format(resp))

