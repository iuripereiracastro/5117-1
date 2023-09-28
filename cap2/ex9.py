sequencia = []

x = 0
while x >= 0:
    x = (int(input(f'Escreva um digito\n(-1 para terminar)\n')))
    if x >= 0:
        sequencia.append(x)

temp = ''
for y in range(len(sequencia)):
    temp += str(sequencia[y])
print(f'O numero é: {temp}')
