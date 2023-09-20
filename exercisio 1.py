"""
Escreve um programa que tem 4 funcoes e recebe 2 numeros:
-somar
-subtrair
-dividir
-multiplicar
"""
a = 10
b = 15


def somar(num1, num2):
    result = num1 + num2
    return result


def subtrair(num1, num2):
    result = num1 - num2
    return result


def dividir(num1, num2):
    result = num1 / num2
    return result


def multiplicar(num1, num2):
    result = num1 * num2
    return result


print(f'{a} + {b} = {somar(a, b)}')
print(f'{a} - {b} = {subtrair(a, b)}')
print(f'{a} / {b} = {dividir(a, b)}')
print(f'{a} * {b} = {multiplicar(a, b)}')

