dis = int(input("Qual a distância da viagem ? (Km) "))
if dis <= 200:
    print("O preço da sua viagem é {} R$.".format(0.5 * dis))
else:
    print("O preço da viagem é {} R$.".format(0.45 * dis))
