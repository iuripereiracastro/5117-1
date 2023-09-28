x = int(input(f'Escreva um numero inteiro\n'))
length = str(x)
i = 0

trocar = True
while trocar:
    trocar = False
    while i < len(length) - 1:
        temp = length[i]
        trocar = True
