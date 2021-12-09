import sys

ls = [[int(n) for n in l] for l in iter(input,'')]
#ns = [n for n in eval(input())]#OPTIONS

def lbi(n,x,y):
    if x >= 0 and y >= 0 and y < len(ls) and x < len(ls[0]):
        return ls[y][x] > n
    else:
        return True

bs = []
fs = set()

for y,r in enumerate(ls):
    for x,n in enumerate(r):
        if lbi(n,x,y+1) and lbi(n,x+1,y) and lbi(n,x,y-1) and lbi(n,x-1,y):
            bs.append({complex(x,y)})
        elif n != 9:
            fs.add(complex(x,y))
#very naive lmao, thanks examples
for b in bs:
    while True:
        a = set()
        for o in 1,-1,1j,-1j:
            a |= fs & set(c+o for c in b)
        if not a:
            break
        b |= a
        fs -= a

sl = sorted(map(len,bs))[::-1]
a,b,c,*_ = sl

print(a*b*c)
