import sys

ls = [l for l in iter(input,'')]#sys.stdin]
#ns = [n for n in eval(input())]#OPTIONS

os = {}

for y,r in enumerate(ls):
    for x,n in enumerate(r):
        os[complex(x,y)] = int(n)
fs = 0
for _ in range(100):
    for o in os:
        os[o] += 1
    fd = set()
    while True:
        for o in os:
            if os[o] > 9 and o not in fd:
                fs += 1
                fd.add(o)
                for s in 1,-1,1j,-1j,1+1j,1-1j,-1+1j,-1-1j:
                    if o+s in os:
                        os[o+s] += 1
                break
        else:
            break
    for o in os:
        if os[o] > 9:
            os[o] = 0

print(fs)
