import sys
from stuff import *
from functools import reduce

l = input()

#bs = bin(eval(f'0x{l}'))[2:]
bs = ''
for c in l:
    x = '0123456789ABCDEF'.index(c)
    bs += format(x,'04b')
def bd(b): return eval(f'0b{b}')

sv = 0
def p(s):
    global sv
    v = bd(s[:3])
    sv += v
    t = bd(s[3:6])
    i = 6
    if t == 4:
        v = 0
        while True:
            v <<= 4
            v += bd(s[i+1:i+5])
            if s[i]=='0':
                break
            i += 5
        i += 5
        return i,v
    else:
        lt = s[6]=='1'
        i += 1
        vs = []
        if lt:
            l = bd(s[i:i+11])
            i += 11
            for _ in range(l):
                x,v = p(s[i:])
                i += x
                vs.append(v)
        else:
            l = bd(s[i:i+15])
            i += 15
            while l>0:
                x,v = p(s[i:])
                i += x
                l -= x
                vs.append(v)
        os = [
            (lambda a,b:a+b),
            (lambda a,b:a*b),
            min,
            max,
            None,
            (lambda a,b:a>b),
            (lambda a,b:a<b),
            (lambda a,b:a==b)
        ]
        v = reduce(os[t],vs)
        return i,v

i,v=p(bs)
print(v)
