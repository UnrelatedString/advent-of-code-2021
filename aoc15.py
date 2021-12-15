import sys
from stuff import *

ls = lines()#chunks()#nums()

cs = {}
d = {}
for y,l in enumerate(ls):
    for x,n in enumerate(l):
        n = eval(n)
        cs[complex(x,y)] = n
        d[complex(x,y)] = float('inf')
        #u.add(complex(x,y))
g = complex(x,y) #thank fuck for python's scoping being shit


d[0] = 0
u = {*cs.keys()}

while u:
    c = min(u,key=d.__getitem__)
    u.remove(c)
    for o in von_neumann:
        if c+o not in cs: continue
        #if c+o not in d:
        #    u.add(c+o)
        #    d[c+o] = float('inf')
        d[c+o] = min(d[c+o], d[c]+cs[c+o])

print(d[g])
