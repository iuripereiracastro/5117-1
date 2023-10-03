length = []
inputo = int(input(f'Escreva um numero inteiro positivo\n'))

for x in str(inputo):
    length.append(x)

b = len(length) - 1
invertido = ''
while b > -1:
    invertido += length[b]
    b -= 1

print(f'O número invertido é {invertido}')
