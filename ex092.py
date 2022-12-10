from datetime import datetime
dad = dict()
dad["Nome"] = str(input("Nome: "))
ano = int(input("Ano de nascimento: "))
dad["Idade"] = datetime.now().year - ano
dad["ctps"] = str(input("Carteira de Trabalho (0 não tem): "))
if dad["ctps"] != 0:
    dad["AC"] = int(input("Ano de contratação: "))
    dad["Salário"] = int(input("Salário: R$ "))
print("-=" * 30)
print(f"Nome tem valor de {dad['Nome']}.")
print(f"Idade tem valor de {dad['Idade']}.")
print(f"Ctps tem o valor de {dad['ctps']}.")
if dad["ctps"] != 0:
    print(f"Contratação tem o valor de {dad['AC']}.")
    print(f"Salário tem valor de {dad['Salário']}.")
ap = 2021 - dad["AC"]
if ap < 35:
    print(f"Aposentadoria aos {dad['Idade'] + (35 - ap)}.")
else:
    print("Você já pode se aposentar")
