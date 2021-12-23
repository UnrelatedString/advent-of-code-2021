import sys
from stuff import *
import heapq as hq

ls = lines()#chunks()#nums()

ls[3:3] = '''  #D#C#B#A#
  #D#B#A#C#'''.split('\n')
# ls[3:3] = ['  #A#B#C#D#']*2

#thank fuck for this not being a maze
rs = tuple(r[::-1] for r in zip(*(l[3:10:2] for l in ls[2:6])))
#print(rs)
ss = ('',)*11 #11 over 7 for less special casing distance calculations

full_room = 4

def li(c):
    return 'ABCD'.find(c)

def r_s(x):
    return x*2+2

def s_r(x):
    return (x-3)//2

def between(ss, *cs):
    return ss[min(cs)+1:max(cs)]

empty_space = '' #thanks heapq

goal = ((('A','A','A','A'),('B','B','B','B'),('C','C','C','C'),('D','D','D','D')),(empty_space,)*11)

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
        if not all(b == a for b in gr):
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
        if not all(b == s for b in gr):
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
        if i == gi and all(b == a for b in r): #cannot believe i forgot to look at the second room
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
    #print(state)
    if state == goal:
        break
    visit(state)
else:
    print()

print(es[goal])
