import sys
from stuff import *

p = input()
input()

ls = lines()#chunks()#nums()

t = {}
for l in ls:
    k,v = l.split(' -> ')
    t[k] = v

for _ in range(10):
    r = ''
    for a,b in zip(p,p[1:]):
        r += t[a+b]
    np = p[0]
    for a,b in zip(r,p[1:]):
        np += a + b
    p = np

cs = [p.count(e) for e in {*p}]
print(max(cs)-min(cs))
