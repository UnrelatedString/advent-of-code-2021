import sys
from stuff import *

l = input().lstrip('target area:').split(', ')

xr,yr = (sorted(int(n) for n in r[2:].split('..')) for r in l)

c=  0
for yv in range(abs(min(yr))+2,min(yr)-2,-1):
    for xv in range(max(xr)+2):
#for yv in range(2000,-99,-1):
#    for xv in range(200):
        x,y = 0,0
        oy = yv
        my = 0
        while True:
            x += xv
            y += yv
            my = max(my,y)
            yv -= 1
            xv = xv and (xv - 1)
            if y < min(yr) or x > max(xr):
                break
            if x >= min(xr) and y <= max(yr):
                c += 1
                break
        yv = oy

print(c)
