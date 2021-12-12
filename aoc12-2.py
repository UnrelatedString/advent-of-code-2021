import sys
from stuff import *

ls = lines()#chunks()#nums()

cs = {}
for l in ls:
    a,b = l.split('-')
    if a not in cs: cs[a] = set()
    if b not in cs: cs[b] = set()
    cs[a].add(b)
    cs[b].add(a)

ps = {('start',)}
while True:
    nps = set()
    for v in ps:
        c = v[-1]
        if c == 'end':
            nps.add(v)
            continue
        for d in cs[c]:
            if (d not in v or all(v.count(x)==1 for x in v if x==x.lower()) or d.lower()!=d) and d != 'start':
                nps.add(v+(d,))
    if nps == ps:
        break
    ps = nps
for p in ps:print(p)
print(len(ps))
