"""
Fazer uma tabuada
"""
import random

prim = []
seg = []
for z in range(10):
    prim.append(random.randint(1, 100))
    seg.append(random.randint(1, 100))

trocar = True
while trocar:
    trocar = False
    p = 0
    while p < len(prim) - 1:
        if prim[p] > prim[p + 1]:
            temp = prim[p]
            prim[p] = prim[p + 1]
            prim[p + 1] = temp
            trocar = True
        p += 1
    q = 0
    while q < len(seg) - 1:
        if seg[q] > seg[q + 1]:
            temp = seg[q]
            seg[q] = seg[q + 1]
            seg[q + 1] = temp
            trocar = True
        q += 1

x = 0
while x < len(prim):
    y = 0
    while y < len(seg):
        print(f'{prim[x]} * {seg[y]} =  {prim[x] * seg[y]}')
        y += 1
    x += 1
    print('--------------------')
