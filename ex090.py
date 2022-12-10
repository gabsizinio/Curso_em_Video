alu = dict()
alu["Nome"] = str(input("Nome: "))
alu["Média"] = float(input(f"Média de {alu['Nome']}: "))
print("-=" * 40)
print(f"- Nome é igual a {alu['Nome']}.")
print(f"- Média é igual {alu['Média']}.")
if 5 <= alu["Média"] < 7:
    print("- Situação é igual a Recuperação.")
if alu["Média"] < 5:
    print("- Situação é igual a Reprovado.")
if alu["Média"] >= 7:
    print("- Situação é igual a Aprovado.")
