import sys
from stuff import *
import heapq as hq

ls = lines()#chunks()#nums()

#thank fuck for this not being a maze
rs = tuple(r[::-1] for r in zip(*(l[3:10:2] for l in ls[2:4])))

states = [(0, rs, ('',)*11)] #11 over 7 for less special casing distance calculations

print(rs)

def li(c):
    return 'ABCD'.find(c)

def r_s(x):
    return x*2+3

def s_r(x):
    return (x-3)//2

def between(ss,*cs):
    return ss[min(cs)+1:max(cs)]


me = float('inf')

hq.heapify(states)

def push(state):
    rs,ss,e = state
    hq.heappush(states, (e,rs,ss))
    #print(e)

seen = set()

while states:
    e, rs, ss = hq.heappop(states)
    # if (rs,ss) in seen: # *presumably* if it's been seen it was cheaper if not the same cost... I guess that rests on the ultimate cheapest solution being reached first though... it's time to turn this into pathfinding
    #     continue
    seen.add((rs,ss))
    #print(e)
    if e > me:
        break
    if all(all(li(a) == i for a in r) and len(r)==2 for i,r in enumerate(rs)):
        print(e)
        me = min(e,me)
        continue
    for i,r in enumerate(rs):
        if not r: continue
        a = r[-1]
        if li(a) != i and len(rs[li(a)]) < 2 and rs[li(a)]==a and not any(between(ss, r_s(i), r_s(li(a)))):
            push((
                tuple(
                    r[:-1] if j==i else r+(a,) if j==li(a) else r for j,r in enumerate(rs)
                ),
                ss,
                e + (2*abs(i-li(a)) + 4 - len(r) - len(rs[li(a)])) * (10**li(a))
            ))
        # else: print(len(rs[li(a)]) < 2 , rs[li(a)]==a , not any(between(ss, r_s(i), r_s(li(a)))))
        else: #are these exclusive in an optimal solution? I sure hope so
            for j,s in enumerate(ss):
                if j not in (2,4,6,8) and s == '' and not any(between(ss, j, r_s(i))):
                    push((
                        tuple(
                            r[:-1] if k==i else r for k,r in enumerate(rs)
                        ),
                        tuple(
                            a if k==j else s for k,s in enumerate(ss)
                        ),
                        e + (abs(j-r_s(i)) + 2 - len(r)) * (10**li(a))
                    ))
                # else:
                #     print(j not in (2,4,6,8) , s is None , not any(between(ss, j, r_s(i))))
    for j,a in enumerate(ss):
        if a and len(rs[li(a)]) < 2 and not any(between(ss, j, r_s(li(a)))):
            push((
                tuple(
                    r+(a,) if i==j else r for i,r in enumerate(rs)
                ),
                tuple(
                    '' if i==j else s for i,s in enumerate(ss)
                ),
                e + (abs(j-r_s(li(a))) + 2 - len(rs[li(a)])) * (10**li(a))
            ))
        # elif a:
        #     print(a , len(rs[li(a)]) < 2 , not any(between(ss, j, r_s(li(a)))))
    #states = nss

print(me)
