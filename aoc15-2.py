import sys
from stuff import *
import heapq as hq

ls = lines()#chunks()#nums()

cs = {}
d = {}
for y,l in enumerate(ls):
    for x,n in enumerate(l):
        n = eval(n)
        for Y in range(5):
            for X in range(5):
                c=complex(x+len(l)*X,y+len(ls)*Y)
                cs[c] = (n-1+X+Y)%9+1
                d[c] = float('inf')
                #u.add(complex(x,y))
g = c #thank fuck for python's scoping being shit


d[0] = 0
u = {*cs.keys()}
h = []
hq.heappush(h,(0,(0,0)))

while g in u:
    _,c = hq.heappop(h)#min(u,key=d.__getitem__)
    c = complex(*c)
    u.remove(c)
    for o in von_neumann:
        if c+o not in cs: continue
        if d[c+o] == float('inf'):
            hq.heappush(h,(d[c]+cs[c+o],c_t(c+o))) #uh?
        d[c+o] = min(d[c+o], d[c]+cs[c+o])

print(d[g])
