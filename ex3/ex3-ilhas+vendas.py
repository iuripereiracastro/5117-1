"""
1. Cria uma lista com os nomes das ilhas do grupo central
2. Cria uma lista com 5 casas, inicializadas a zero
3. Pede ao utilizador para inserir vendas para cada ilha
4. Apresenta:
             - total de vendas
"""
ilhas = ["São Jorge", "Pico", "Graciosa", "Faial", "Terceira"]
vendas = [0, 0, 0, 0, 0]

i = 0
checkSum = 0

for currentVenda in range(len(vendas)):
    while i < 5:
        vendas[i] = int(input(f'Insira as vendas para {ilhas[i]}: '))
        checkSum += vendas[i]
        i += 1

print(f'Total de vendas: {checkSum}')
