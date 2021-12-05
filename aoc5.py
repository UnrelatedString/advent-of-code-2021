ls = [l.split(' -> ') for l in iter(input,'')]

g = set()
r = set()
for l in ls:
    a,b = sorted(map(eval,l))
    if a[0]==b[0] or a[1]==b[1]:
        for x in range(a[0],b[0]+1):
            for y in range(a[1],b[1]+1):
                if (x,y) in g:
                    r.add((x,y))
                g.add((x,y))
print(len(r))
