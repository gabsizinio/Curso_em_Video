def notas(*a, sit=False):
    """
    ⟶ Função para analisar notas e situações dos alunos-
    :param a: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    print("-" * 40)
    maior = 0
    menor = 9999999999
    p = 0
    s = 0
    dic = dict()
    for c in a:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
        s += c
        p += 1
    dic["total"] = p
    dic["maior"] = maior
    dic["menor"] = menor
    dic["média"] = s / p
    if sit:
        if dic["média"] < 6:
            sit = "Ruim"
        if dic["média"] >= 7:
            sit = "Boa"
        if 6 <= dic["média"] < 7:
            sit = "Razoável"
        dic["situação"] = sit
    return dic


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

