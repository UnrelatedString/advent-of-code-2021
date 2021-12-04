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
    for b in gs:
        for r in b:
            for j,v in enumerate(r):
                if v == n:
                    r[j] = 0
            if all(not v for v in r):
                 o(b,n)
        for c in zip(*b):
            if all(not v for v in c):
                o(b,n)
