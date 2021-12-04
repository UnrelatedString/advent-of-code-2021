ls = [l for l in iter(input,'e')]

bs = '\n'.join(ls).split('\n\n')

ns = eval(bs[0])
del bs[0]

gs = []
for b in bs:
    gs.append([])
    for r in b.split('\n'):
        gs[-1].append([])
        for c in r.split():
            gs[-1][-1].append(int(c))

def o(b,n):
    o = sum(sum(r) for r in b) * n
    if o:
        print(o, n)
        exit()

for i,n in enumerate(ns):
    n = int(n)
    for k,b in enumerate(gs):
        for r in b:
            for j,v in enumerate(r):
                if v == n:
                    r[j] = 0
            if all(not v for v in r):
                if len(gs) == 1:
                    o(gs[0],n)
                gs[k] = None
        for c in zip(*b):
            if all(not v for v in c):
                if len(gs) == 1:
                    o(gs[0],n)
                gs[k] = None
    gs = [g for g in gs if g]
