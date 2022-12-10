m20 = p18 = ho = 0
while True:
    print("-" * 50)
    print("            CADASTRE UMA PESSOA")
    print("-" * 50)
    ida = int(input("Idade: "))
    sex = " "
    while sex not in "MmFf":
        sex = str(input("Sexo: [M/F] ")).upper().strip()
    if ida > 18:
        p18 = p18 + 1
    if sex == "M":
        ho = ho + 1
    if sex == "F" and ida < 20:
        m20 = m20 + 1
    res = str(input("Quer continuar ? (S/N) ")).upper().strip()
    if res == "N":
        break
print("====== FIM DO PROGRAMA ======")
print(f"O n° de pessoas com mais de 18 anos é {p18}.")
print(f"O n° de homens cadastrados é {ho}.")
print(f"O n° de mulheres com menos de 20 anos cadastradas é {m20}.")
