pre = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor",
       4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
print('''------------------------------------------
          LISTAGEM DE PREÇOS
------------------------------------------''')
for c in range(0, 17, 2):
    print(f"{pre[c]:.<30}R${pre[c + 1]:>7.2f}")
print("---------------------------------------")
