x = 0
while x >= 0:
    if x > 0:
        print(f'O numero de dias correspondente é {((x / 60) / 60) / 24}')
    x = int(input('Escreva um número de segundos\n(um número negativo para terminar)\n'))
