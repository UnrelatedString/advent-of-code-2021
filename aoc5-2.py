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
    if abs(a[0]-b[0]) == abs(a[1]-b[1]):
        for n in range(b[0]-a[0]+1):
            x = a[0] + n
            y = a[1] + n * (-1)**(b[1]<a[1])
            if (x,y) in g:
                r.add((x,y))
            g.add((x,y))

print(len(r))
