import sys
from stuff import *

ls = lines()#chunks()#nums()

ps = [int(l[-1]) for l in ls]

ss = {((0,0),tuple(ps)):1}

t = 1
ws = [0,0]
while ss:
    t ^= 1
    nss = dd(lambda:0)
    for (s,p),c in ss.items():
        for d1 in 1,2,3:
            for d2 in 1,2,3:
                for d3 in 1,2,3:
                    d=d1+d2+d3
                    ts = s[t]
                    tp = p[t]
                    tp += d
                    tp = tp%10 or 10
                    ts += tp
                    if ts >= 21:
                        ws[t] += c
                        continue
                    ks = (ts,s[t^1])[::(-1)**t]
                    kp = (tp,p[t^1])[::(-1)**t]
                    nss[ks,kp] += c
    ss = nss

print(max(ws))
