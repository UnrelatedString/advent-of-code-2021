import sys

ls = [[x.split() for x in l.split(' | ')] for l in iter(input,'')]

ps = "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg".split()

ss=0
for s,v in ls:
    aa = {a: {*"abcdefg"} for a in "abcdefg"}
    for d in s+v:
        for p in ps:
            if len(p) == len(d):
                for a in p:
                    aa[a] &= {*d}
    while not all(len(a) == 1 for a in aa.values()):
        if not any(len(a) >= 1 for a in aa.values()):
            print('fuck')
            break
        for k,a in aa.items():
            if len(a) == 1:
                for ok,oa in aa.items():
                    if k != ok:
                        oa -= a
    o = 0
    for d in v:
        t = sorted(next(iter(aa[a])) for a in d)
        o *= 10
        o += ps.index(''.join(t))
    ss += o
print(ss)
