"""
Artimatico
"""


def aritmetica(op, n1, n2):
    if op == '+':
        resultado = n1 + n2
    elif op == '-':
        resultado = n1 - n2
    elif op == '*':
        resultado = n1 * n2
    elif op == '/':
        resultado = n1 / n2
    else:
        resultado = 'Operação inválida'
    return resultado


def contas(op, n1, n2):
    if op == '+':
        resultado = n1 + n2
    else:
        if op == '-':
            resultado = n1 - n2
        else:
            if op == '*':
                resultado = n1 * n2
            else:
                if op == '/':
                    resultado = n1 / n2
                else:
                    resultado = 'Operação inválida'
    return resultado


def continhas(op, n1, n2):
    resultado = 'Operação inválida'
    if op == '+':
        resultado = n1 + n2
    if op == '-':
        resultado = n1 - n2
    if op == '*':
        resultado = n1 * n2
    if op == '/':
        resultado = n1 / n2
    return resultado


print(contas('+', 20, 10))
print(contas('-', 20, 10))
print(contas('*', 20, 10))
print(contas('/', 20, 10))
print(contas('bla', 20, 10))
print('--------')
print(aritmetica('+', 30, 15))
print(aritmetica('-', 30, 15))
print(aritmetica('*', 30, 15))
print(aritmetica('/', 30, 15))
print(aritmetica('bla', 30, 15))
print('--------')
print(continhas('+', 10, 20))
print(continhas('-', 10, 20))
print(continhas('*', 10, 20))
print(continhas('/', 10, 20))
print(continhas('bla', 10, 20))
