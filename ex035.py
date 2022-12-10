s1 = float(input("Digite o comprimento do 1°segmento: (cm) "))
s2 = float(input("Digite o comprimento do 2°segmento: (cm) "))
s3 = float(input("Digite o comprimento do 3°segmento: (cm) "))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Os segmentos formam um triângulo.")
else:
    print("Os segmentos não formam um triângulo.")
