import sys

ls = [[int(n) for n in l] for l in iter(input,'')]
#ns = [n for n in eval(input())]#OPTIONS

def lbi(n,x,y):
    if x >= 0 and y >= 0 and y < len(ls) and x < len(ls[0]):
        return ls[y][x] > n
    else:
        return True

s = 0
for y,r in enumerate(ls):
    for x,n in enumerate(r):
        if lbi(n,x,y+1) and lbi(n,x+1,y) and lbi(n,x,y-1) and lbi(n,x-1,y):
            s += 1 + n

print(s)
