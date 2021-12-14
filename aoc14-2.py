import sys
from stuff import *

p = input()
input()

ls = lines()#chunks()#nums()

t = {}
for l in ls:
    k,v = l.split(' -> ')
    t[k] = v

d = {x:p.count(x) for x in t}
tt = {}
for x in t:
    r = t[x]
    tt[x] = {x[0]+r,r+x[1]}

for _ in range(40):
    nd = {}
    for x in d:
        for r in tt[x]:
            if r not in nd:
                nd[r] = 0
            nd[r] += d[x]
    d = nd

cs = {}
for x in d:
    for c in x:
        if c not in cs:
            cs[c] = 0
        cs[c] += d[x]
print((max(cs.values())-min(cs.values()))//2)
