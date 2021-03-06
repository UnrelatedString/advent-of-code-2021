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

ps = [('start',())]
while True:
    nps = []
    for c,v in ps:
        if c == 'end':
            nps.append((c,v))
            continue
        for d in cs[c]:
            if d not in v or d.lower()!=d:
                nps.append((d,v+(c,)))
    if nps == ps:
        break
    ps = nps

print(len({*ps}))
