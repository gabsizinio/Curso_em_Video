from math import radians, sin, cos, tan
ang = float(input("Digite o ângulo que você deseja em °: "))
ang1 = radians(ang)
print("O SENO de {}° é {:.2f}.".format(ang, sin(ang1)))
print("O COSSENO de {}° é {:.2f}.".format(ang, cos(ang1)))
print("A TANGENTE de {}° é {:.2f}.".format(ang, tan(ang1)))
