import json

faturaJson = open("dados.json")
dadosJson = json.load(faturaJson)
faturaJson.close()


def maxMonthlyValue(listaValores):
    dia = 0
    valor = 0
    
    for diaValor in listaValores:
        if diaValor["valor"] > valor:
            valor = diaValor["valor"]
            dia = diaValor["dia"]
    
    maiorValorMensal = "Dia %d || Valor = %.2f" % (dia, valor)
    return maiorValorMensal


def minMonthlyValue(listaValores):
    dia = listaValores[0]["dia"]
    valor = listaValores[0]["valor"]

    for diaValor in listaValores:
        if diaValor["valor"] < valor:
            valor = diaValor["valor"]
            dia = diaValor["dia"]
    
    menorValorMensal = "Dia %d || Valor = %.2f" % (dia, valor)
    return menorValorMensal


def daysAboveMonthlyValue(listaValores):
    diasAcima = []
    total = 0
    ignoreDia = 0
    mediaMensal = 0
    for valores in listaValores:
        mediaMensal += valores["valor"]
        if valores["valor"] == 0:
            ignoreDia += 1

    mediaMensal = mediaMensal / (len(listaValores) - ignoreDia)

    for diaValor in listaValores:
        if diaValor["valor"] > mediaMensal:
            total += 1
            diasAcima.append(diaValor["dia"])
    
    retornoDias = "Total de dias com valor acima da média: %d\n--> Dias: " % total

    for dia in diasAcima:
        retornoDias += "%d " % dia
    
    retornoDias = retornoDias.strip()

    return retornoDias


print("Menor valor mensal: " + minMonthlyValue(dadosJson))
print("Maior valor mensal: " + maxMonthlyValue(dadosJson))
print(daysAboveMonthlyValue(dadosJson))