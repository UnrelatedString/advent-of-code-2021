import sys
from stuff import *

ls = lines()#chunks()#nums()

cs = []

def ri(a,b):
    l = max(a[0],b[0])
    r = min(a[1],b[1])
    if r >= l:
        return r-l+1, (l,r)

t = 0

for l in ls:
    s = l[1] == 'n'
    l = l[4-s:]
    rs = tuple(sorted(int(b) for b in c[2:].split('..')) for c in l.split(','))
    xr,yr,zr=rs
    #print(rs, t)
    for c,p in cs[:]:
        ins = [ri(b,a) for a,b in zip(c,rs)]
        if all(ins):
            xi,yi,zi=[*zip(*ins)][0]
            #print(rs,c,xi*yi*zi)
            if p:
                t -= xi*yi*zi
            elif s:
                t += xi*yi*zi
            if not p:
                pass
            else:
                nrs = [*zip(*ins)][1]
                cs.append((nrs,False))
    if s:
        v=1
        for r in rs:
            v *= r[1]-r[0]+1
        t += v
        cs.append((rs,True))
    print(t,s)
    #print(t)

print(t)
