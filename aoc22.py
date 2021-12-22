import sys
from stuff import *

ls = lines()#chunks()#nums()

cs = set()

for l in ls:
    s = l[1] == 'n'
    l = l[4-s:]
    xr,yr,zr = [sorted(int(b) for b in c[2:].split('..')) for c in l.split(',')]
    for x in range(xr[0],xr[1]+1):
        if x not in range(-50,51):continue
        for y in range(yr[0],yr[1]+1):
            if y not in range(-50,51):continue
            for z in range(zr[0],zr[1]+1):
                if z not in range(-50,51):continue
                c = x,y,z
                if s:
                    cs.add(c)
                else:
                    cs -= {c}

print(len(cs))
