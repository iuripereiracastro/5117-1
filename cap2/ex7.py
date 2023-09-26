x = int(input(f'Insira o seu salario por hora: '))
y = int(input(f'Insira o numero de horas trabalhadas esta semana: '))

if y < 40:
    print(f'Ordenado: {x * y}')
else:
    print(f'Ordenado (horas extraordinarias): {(x * 40) + (x * (y - 40))}')
