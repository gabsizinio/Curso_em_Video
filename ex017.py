from math import sqrt
co = float(input("Comprimento do cateto oposto: (cm) "))
ca = float(input("Comprimento do cateto adjascente: (cm) "))
hip = sqrt(co ** 2 + ca ** 2)
print("A hipotenusa vai medir {} cm.".format(hip))
