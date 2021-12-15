import sys
from stuff import *

ls = lines()#chunks()#nums()

cs = {}
for y,l in enumerate(ls):
    for x,n in enumerate(l):
        n = eval(n)
        cs[complex(x,y)] = n
g = complex(x,y) #thank fuck for python's scoping being shit

def f(p):
    os = []
    if p == g:
        return 0
    for o in 1,1j:
        np = p + o
        if np in cs:
            os.append(f(np) + cs[np])
    return min(os)

print(f(0+0j))
