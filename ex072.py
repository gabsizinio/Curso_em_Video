lista = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
         "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito"
         , "dezenove", "vinte")
num = 0
resp = "S"
while True:
    num = int(input("Digite um número de 0 a 20: "))
    while num > 20 or num < 0:
        num = int(input("Tente novamente. Digite um número de 0 a 20: "))
    print(f"Você digitou o número {lista[num]}.")
    print("-=-" * 20)
    resp = str(input("Você quer continuar: (S/N) ")).upper()
    print("-=-" * 20)
    if resp == "N":
        break
print("Ok, obrigado.")
