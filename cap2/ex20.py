const = 8
res = ''
for x in range(1, 10):
    res += str(x)
    print(f'{res} * {const} + {x} = {(int(res) * const) + x}')
