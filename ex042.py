s1 = float(input("1° segmento: "))
s2 = float(input("2° segmento: "))
s3 = float(input("3° segmento: "))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        print("Os segmentos formam um triângulo EQUILÁTERO.")
    if s1 == s2 != s3 or s1 == s3 != s2 or s2 == s3 != s1:
        print("Os segmentos formam um triângulo ISÓCELES.")
    if s1 != s2 and s1 != s3 and s2 != s3:
        print("Os segmentos formam um triângulo ESCALENO.")
else:
    print("Os segmentos não formam triângulo.")
