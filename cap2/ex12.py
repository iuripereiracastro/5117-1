x = int(input(f'Qual o valor de x\n'))
n = int(input(f'Qual o valor de n\n'))

soma = 1
i = 1
factorial = 1
while i <= n:
    factorial = factorial * i
    soma += (x ** i) / factorial
    i += 1

print(f'O valor da soma é {soma}')
