import sys
from stuff import *

ls = lines()#chunks()#nums()

def unwrap(t):
    if len(t) == 1:
        return t[0]
    else:
        return [unwrap(x) for x in t]

def reds(p, l, d):
    #print(p)
    if len(p) == 2:
        a, b = p
        if d > 3:
            #print(f'exploding {unwrap(p)}')
            if l:
                while len(l)==2:
                    l = l[1]
                l[0] += a[0]
            return [0],b[0]
        r = reds(a, l, d+1)
        if type(r) is tuple:
            v, c = r
            p[0] = v
            while len(b)==2:
                b = b[0]
            b[0] += c
            return p
        elif r is not None:
            p[0] = r
            return p
        r = reds(b, a, d+1)
        if type(r) is tuple:
            v, c = r
            p[1] = v
            return p, c
        elif r is not None:
            p[1] = r
            return p
    # else:
    #     if p[0] >= 10:
    #         print(f'splitting {unwrap(p)}')
    #         return [[p[0]//2],[(p[0]//2)+p[0]%2]]

def splis(p):
    if len(p) == 1:
        if p[0] >= 10:
            #print(f'splitting {unwrap(p)}')
            return [[p[0]//2],[(p[0]//2)+p[0]%2]]
    else:
        a, b = p
        r = splis(a)
        if r is not None:
            p[0] = r
            return p
        r = splis(b)
        if r is not None:
            p[1] = r
            return p

def wrap(t):
    if type(t) is list:
        return [*map(wrap,t)]
    else:
        return [t]

def mag(l):
    if len(l) == 2:
        a, b = l
        return 3*mag(a) + 2*mag(b)
    return l[0]

def add(a,b):
    s = [a,b]
    while True:
        if reds(s, [], 0) is None:
            if splis(s) is None:
                break
    return s

r = 0
for n in ls:
    for m in ls:
        if n == m: continue
        r = max(r, mag(add(wrap(eval(n)),wrap(eval(m)))))

print(r)
