
def calculoTotalFatura(listaValores):
    total = 0
    for valor in listaValores:
        total += valor["faturamento"]
    
    return total


#_________________________________________

faturamento_estado = [
    {"estado":"SP", "faturamento":67836.43},
    {"estado":"RJ", "faturamento":36678.66},
    {"estado":"MG", "faturamento":29229.88},
    {"estado":"ES", "faturamento":27165.48},
    {"estado":"Outros", "faturamento":19849.53}
]

total = calculoTotalFatura(faturamento_estado)

for valor in faturamento_estado:
    print(f'Estado: {valor["estado"]:^7} || Faturamento(%): {((valor["faturamento"]/total)*100):<5.2f}%')
