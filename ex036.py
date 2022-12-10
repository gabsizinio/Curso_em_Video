print("-=-" * 20)
print("                     BANCO VERDE")
print("-=-" * 20)
casa = float(input("Valor do imóvel: (R$) "))
sal = float(input("Valor do seu salário: (R$) "))
anos = int(input("Em quantos anos você pretende pagar o empréstimo: "))
pres = casa / (anos * 12)
if pres <= sal * 0.3:
    print("Seu empréstimo de R$ {} foi APROVADO.".format(casa))
    print("Você terá que pagar um valor de R$ {:.2F} mensalmente durante {} anos.".format(pres, anos))
else:
    print("Seu empréstimo de R$ {} foi NEGADO.".format(casa))
