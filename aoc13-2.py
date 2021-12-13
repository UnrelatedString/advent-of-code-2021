import sys
from stuff import *

ls = lines()#chunks()#nums()

ps = {complex(*eval(l)) for l in ls}

fs = lines()

for f in fs: #lol
    f = f[11:]
    a = (-1j)**(f[0]=='y')
    n = int(f[2:])
    nps = set()
    for p in ps:
        p *= a
        if p.real > n:
            r,i = c_t(p)
            p = complex(n-(r-n),i)
        elif p.real == n:
            continue
        p /= a
        nps.add(p)
    ps = nps

mx,my = map(max,zip(*map(c_t,ps)))
for y in range(int(my)+1):
    for x in range(int(mx)+1):
        print(end='.#'[complex(x,y) in ps])
    print()

print(len(ps))
