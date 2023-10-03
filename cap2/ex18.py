num = int(input(f'Escreva um numero inteiro\n'))
n = []

for x in str(num):
    n.append(int(x))


#   9 8 0 0 7 6 4 0 0 0 3
#   - - 0 1 - - - 0 1 1 -
counter = 0
for idx in range(len(n) - 1):
    if n[idx] == 0:
        if n[idx + 1] == 0:
            counter += 1


print(f'O numero tem {counter} zeros seguidos')

