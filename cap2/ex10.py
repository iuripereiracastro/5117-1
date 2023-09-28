x = (int(input(f'Escreva um numero inteiro\n')))
length = str(x)
zprint = ''

for y in range(len(length)):
    if int(length[y]) % 2:
        zprint = zprint + length[y]
print(f'Resultado: {zprint}')
