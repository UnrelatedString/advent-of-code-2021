import sys
from stuff import *

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
    if t == 4:
        i = 6
        while s[i]=='1':
            i += 5
        i += 5
        return i
    else:
        lt = s[6]=='1'
        i = 7
        if lt:
            l = bd(s[i:i+11])
            i += 11
            for _ in range(l):
                i += p(s[i:])
            return i
        else:
            l = bd(s[i:i+15])
            i += 15
            while l>0:
                x = p(s[i:])
                i += x
                l -= x
            return i

p(bs)
print(sv)
