"""
Escreve um programa que recebe 3 variaveis: a, b, definidor
Uma funçao aritmética (ari) recebe as 3 e dependendo da informação dada multiplica, soma, divide ou subtrai
Print
"""
while True:
    try:
        a = int(input(f'Insira o primeiro numero:'))
        break
    except ValueError:
        print(f'Insira um valor valido para o primeiro numero.')
        continue

while True:
    try:
        b = int(input(f'Insira o segundo numero:'))
        break
    except ValueError:
        print(f'Insira um valor valido para o segundo numero.')
        continue

definidor = input(f'Insira o tipo de operacao ( +, -, *, /):')

while definidor not in ('+', '-', '*', '/'):
    definidor = input(f'Insira um valor valido( +, -, *, /):')


def ari(num1, num2, operador):
    if operador == '+':
        var = num1 + num2
        print(f'Resultado: {var}')
    elif operador == '-':
        var = num1 - num2
        print(f'Resultado: {var}')
    elif operador == '*':
        var = num1 * num2
        print(f'Resultado: {var}')
    else:
        var = num1 / num2
        print(f'Resultado: {var}')


ari(a, b, definidor)

