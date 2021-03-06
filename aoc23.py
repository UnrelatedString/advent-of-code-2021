import sys
from stuff import *
import heapq as hq

ls = lines()#chunks()#nums()

#thank fuck for this not being a maze
rs = tuple(r[::-1] for r in zip(*(l[3:10:2] for l in ls[2:4])))

ss = ('',)*11 #11 over 7 for less special casing distance calculations

full_room = 2 #since i know what part 2 is

def li(c):
    return 'ABCD'.find(c)

def r_s(x):
    return x*2+2

def s_r(x):
    return (x-3)//2

def between(ss, *cs):
    return ss[min(cs)+1:max(cs)]

empty_space = '' #thanks heapq

goal = ((('A','A'),('B','B'),('C','C'),('D','D')),(empty_space,)*11)

es = {(rs,ss): 0}
uv = [(0, (rs,ss))]

def update(state, cost):
    if state not in uv and state not in es:
        es[state] = cost
        hq.heappush(uv, (cost, state))
    else:
        es[state] = min(es[state], cost)

def roomd(r):
    return full_room - len(r)

def visit(state):
    rs, ss = state
    cost = es[state]
    # room to room
    for i,r in enumerate(rs):
        if not r:
            continue
        a = r[-1]
        gi = li(a)
        if i == gi:
            continue
        gr = rs[gi]
        if len(gr) == full_room:
            continue
        if any(between(ss, r_s(i), r_s(gi))):
            continue
        e = abs(r_s(i) - r_s(gi))
        e += roomd(r) + 1
        e += roomd(gr)
        e *= 10 ** gi
        rl = [*rs]
        rl[i] = r[:-1]
        rl[gi] = gr+(a,)
        update((tuple(rl), ss), cost + e)
    # space to room
    for i,s in enumerate(ss):
        if not s:
            continue
        gi = li(s)
        gr = rs[gi]
        if len(gr) == full_room:
            continue
        if any(between(ss, i, r_s(gi))):
            continue
        e = abs(i - r_s(gi))
        e += roomd(gr)
        e *= 10 ** gi
        rl = [*rs]
        sl = [*ss]
        sl[i] = empty_space
        rl[gi] = gr+(s,)
        update((tuple(rl), tuple(sl)), cost + e)
    # room to space
    for i,r in enumerate(rs):
        if not r:
            continue
        a = r[-1]
        gi = li(a)
        if i == gi:
            continue
        for j,s in enumerate(ss):
            if s:
                continue
            if j in (2,4,6,8):
                continue
            if any(between(ss, r_s(i), j)):
                continue
            e = abs(r_s(i) - j)
            e += roomd(r) + 1
            e *= 10 ** gi
            rl = [*rs]
            sl = [*ss]
            rl[i] = r[:-1]
            sl[j] = a
            update((tuple(rl), tuple(sl)), cost + e)

while uv:
    _, state = hq.heappop(uv)
    if state == goal:
        break
    visit(state)

print(es[goal])
