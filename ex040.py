nota1 = float(input("1° nota: "))
nota2 = float(input("2° nota: "))
media = (nota1 + nota2) / 2
print("Com notas {} e {},".format(nota1, nota2))
if media < 5:
    print("A sua média final foi {} e você está REPROVADO.".format(media))
elif 5 <= media < 7:
    print("A sua média final foi {} e você está de RECUPERAÇÃO.".format(media))
else:
    print("A sua média final foi {} e você está APROVADO.".format(media))
