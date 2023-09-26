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
vendas = [0, 0, 0, 0, 0]

i = 0
checkSum = 0

for ilha in ilhas:
    while i < 5:
        vendas[i] = int(input(f'Insira as vendas para {ilhas[i]}:\n'))
        checkSum += vendas[i]
        i += 1

big = vendas[0]
bigIlha = ilhas[0]
small = vendas[0]
smallIlha = ilhas[0]
y = 0
for venda in vendas:
    #   Ilha com maior vendas
    if vendas[y] > big:
        big = vendas[y]
        bigIlha = ilhas[y]
    #   Ilha com menor vendas
    if vendas[y] < small:
        small = vendas[y]
        smallIlha = ilhas[y]
    y += 1

print(f'Total das vendas: {checkSum}')
medium = checkSum / len(vendas)
print(f'Media das vendas: {medium}')

print('----------------------------')
x = 0
for ilha in ilhas:
    if vendas[x] >= medium:
        print(f'{ilhas[x]} vendeu mais que a media')
    else:
        print(f'{ilhas[x]} vendeu menos que a media')
    x += 1

print('----------------------------')
print(f'{bigIlha} vendeu a maior quantidade ({big})')
print(f'{smallIlha} vendeu a menor quantidade ({small})')
