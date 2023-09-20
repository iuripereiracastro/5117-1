"""
Hello
"""
print("Howdy")
a = 10
print(a)
print(id(a))
height = 20
width = 10


def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado


area = multiplicar(height, width)

print(f'Area = {area}')
