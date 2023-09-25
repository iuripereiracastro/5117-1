"""
1. Cria uma lista com os nomes das ilhas do grupo central
2. Cria uma lista com 5 casas, inicializadas a zero
3. Pede ao utilizador para inserir vendas para cada ilha
4. Apresenta:
             - total de vendas
             - media
             - ilhas e montante(s) que venderam mais, menos, mais que a media, menos que a media
             - ordena de forma crescente e decrescente
"""
ilhas = ["São Jorge", "Pico", "Graciosa", "Faial", "Terceira"]
ilhasmaior = []
ilhasmenor = []
vendas = [0, 0, 0, 0, 0]
total = minimo = maximo = casa = 0
for ilha in ilhas:
    vendas[casa] = int(input(f'Insira as vendas para {ilhas[casa]}:\n'))
    total += vendas[casa]
    if casa == 0:
        minimo = vendas[casa]
        maximo = vendas[casa]
    else:
        if vendas[casa] < minimo:
            minimo = vendas[casa]
        if vendas[casa] > maximo:
            maximo = vendas[casa]
    casa += 1

print(f' vendas = {vendas} total = {total} minimo = {minimo} maximo = {maximo}')
print('--------------------------------------')

for casa in range(len(vendas)):
    if vendas[casa] == minimo:
        ilhasmenor.append(ilhas[casa])
        print(f'{ilhas[casa]} vendeu o menor: {vendas[casa]}')
    if vendas[casa] == maximo:
        ilhasmaior.append(ilhas[casa])
        print(f'{ilhas[casa]} vendeu o maior: {vendas[casa]}')

print(f' ilhas com menor venda = {ilhasmenor} menor valor = {minimo}')
print(f' ilhas com maior venda = {ilhasmaior} maior valor = {maximo}')
print('--------------------------------------')

def ordenar(lista, ordem = 1):
    troquei = True
    while troquei:
        troquei = False
        x = 0
        while x < len(lista) - 1:
            if lista[x] * ordem > lista[x + 1] * ordem:
                temp = lista[x]
                lista[x] = lista[x + 1]
                lista[x + 1] = temp
                troquei = True
            x += 1
    return lista

print(ordenar(vendas))
print(ordenar(vendas, -1))
print('--------------------------------------')
