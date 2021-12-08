import sys
from itertools import permutations

ls = [[x.split() for x in l.split(' | ')] for l in iter(input,'')]

ps = "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg".split()

def gl(ds,l,c=set()):
    for d in ds:
        d = {*d}
        if len(d)==l and d > c:
            return d

ss=0
for s,v in ls:
    m = {''.join(sorted(d)) for d in {*s,*v}}
    aa = {}
    da = {}
    da[1] = gl(m,2)
    da[7] = gl(m,3)
    da[4] = gl(m,4)
    da[8] = gl(m,7)
    da[9] = gl(m,6,da[4])
    da[3] = gl(m,5,da[7])
    m -= {''.join(sorted(d)) for d in da.values()}
    da[0] = gl(m,6,da[7])
    da[5] = gl(m,5,da[4]-da[3])
    m -= {''.join(sorted(d)) for d in da.values()}
    print(m)
    da[2] = gl(m,5)
    da[6] = gl(m,6)
    sm = {''.join(sorted(d)): x for x,d in da.items()}
    print(sm)
    o = 0
    for d in v:
        o *= 10
        o += sm[''.join(sorted(d))]
    ss += o
print(ss)
