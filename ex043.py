print("-=-" * 20)
print("                 CALCULADORA DE IMC")
print("-=-" * 20)
alt = float(input("Digite sua altura: (m) "))
peso = float(input("Digite o seu peso: (Kg) "))
imc = peso / (alt ** 2)
if imc < 18.5:
    print("Seu IMC é de {:.2f} e você está ABAIXO DO PESO.".format(imc))
elif 18.5 <= imc < 25:
    print("Seu IMC é de {:.2f} e você está com o PESO IDEAL.".format(imc))
elif 25 <= imc < 30:
    print("Seu IMC é de {:.2f} e você está com SOBREPESO.".format(imc))
elif 30 <= imc < 40:
    print("Seu IMC é de {:.2f} e você está com OBESIDADE.".format(imc))
else:
    print("Seu IMC é de {:.2f} e você está com OBESIDADE MÓRBIDA.".format(imc))
