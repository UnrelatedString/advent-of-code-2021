import sys
from stuff import *

ls = lines()#chunks()#nums()

rs = 0
def dd():
    global rs
    while True:
        for n in range(1,101):
            rs += 1
            yield n
            #print(n)
d = dd()

ps = [int(l[-1]) for l in ls]

ss = [0,0]

p = 1
while all(s < 1000 for s in ss):
    p ^= 1
    r = next(d)+next(d)+next(d)
    ps[p] += r
    ps[p] = ps[p]%10 or 10
    ss[p] += ps[p]
    #print(ss)

print(ss[p^1]*rs)
