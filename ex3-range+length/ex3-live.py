"""
Range e Length
"""

list = [60, 20, 40, 39, 10, 25, 40, 239, 10, 59, 28, 29, 200]

#1. Imprime o numero de casas na lista
print(len(list))
print('------')

#2. Imprime a sequencia de numeros entre 0 e o numero de casas na list - 1. Usa a variavel x
i = 0
for x in range(len(list)):
    print(f'Casa {i} = {list[x]}')
    i += 1

print('------')

#3. Imprime a sequencia de numeros entre numero de casas - 1 e 0. Usa variavel y
numero = len(list) - 1
for y in range(len(list)):
    print(numero)
    numero -= 1

print('------')

#4. Imprime a lista na ordem inversa
n = len(list) - 1
for z in range(len(list)):
    print(f'Casa {n} = {list[n]}')
    n -= 1

print('------')

#5. Imprimir os elementos da lista e dizer se é par ou impar
for num in range(len(list)):
    if list[num] % 2 == 0:
        print(f'O numero {list[num]} é par')
    else:
        print(f'O numero {list[num]} é impar')
