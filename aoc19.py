import sys
from stuff import *
import re

ls = open('input19.txt').read().rstrip('\n').split('\n\n')#Chunks is fucking broken #chunks()#nums()

def at(a,b):
    return tuple(x+y for x,y in zip(a,b))

def st(a,b):
    return tuple(x-y for x,y in zip(a,b))

ss = {}
for c in ls:
    s = set()
    c = c.split('\n')
    ss[int(re.search(r'\d+',c[0])[0])] = s
    s |= {eval(t) for t in c[1:]}

def rotn(v, a, b):
    x, y, z = v
    for _ in range(a):
        x, y = -y, x
    return [
        (x, y, z),
        (-z, y, x),
        (x, -z, y),
        (x, -y, -z), # or should x be negative?
        (z, y, -x),
        (x, z, -y)
    ][b]

um = {*ss} - {0}
m = [ss[0]]

def l():
    for u in um:
        for a in range(4):
            for b in range(6):
                cs = [rotn(t, a, b) for t in ss[u]]
                for s in m:
                    for p in s:
                        for r in cs:
                            d = st(p, r)
                            o = {at(d, c) for c in cs}
                            i = o & s
                            if len(i) >= 12:
                                m.append(o)
                                um.remove(u)
                                return u

while um:
    r=l()
    if r:
        print(f'got {r}')
    else:
        print('what the fuck')

print(len(set.union(*m)))
