tab = ("Bragantino", "Athletico-PR", "Palmeiras", "Fortaleza", "Bahia", "Santos",
       "Atlético-GO", "Atlético-MG", "Fluminense", "Flamengo", "Corinthians", "Ceará",
       "Internacional", "Juventude", "Sport", "Cuiabá", "São Paulo", "Chapecoense", "América-MG",
       "Grêmio")
print("CAMPEONATO BRASILEIRO 2021 - RODADA 7")
print(f"A classificação atual é: {tab}.")
print("-=-" * 50)
print(f"Os 5 primeiros do campeonato são: {tab[0:5]}.")
print("-=-" * 50)
print(f"A zona de rebaixamento: {tab[16:]}.")
print("-=-" * 50)
print(f"Times em ordem alfabética: {sorted(tab)}.")
print("-=-" * 50)
print(f"A Chapecoense está em {tab.index('Chapecoense') + 1}°lugar.")
print("-=-" * 50)

