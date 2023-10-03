num = int(input(f'Escreva um numero\n'))
length = []

for x in str(num):
    length.append(int(x))


b = len(length) - 1
while b >= 0:
    length.append(length[b])
    b -= 1


capicua = ''
for n in length:
    capicua += str(n)


print(capicua)
