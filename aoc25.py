ls = [l for l in iter(input,'')]

g = {}
w,h = len(ls[0]),len(ls)
for y,r in enumerate(ls):
    for x,v in enumerate(r):
        if v != '.':
            g[complex(x,y)] = v

t = 0
while True:
    t += 1
    moved = False
    ng = {}
    for z,v in g.items():
        x,y = z.real,z.imag
        if v == '>':
            nz = complex((x+1)%w,y)
            if nz in g:
                ng[z] = v
            else:
                ng[nz] = v
                moved = True
                #print(f'moved {z} {nz}')
        else:
            ng[z] = v
    g = ng
    ng = {}
    for z,v in g.items():
        x,y = z.real,z.imag
        if v == 'v':
            nz = complex(x,(y+1)%h)
            if nz in g:
                ng[z] = v
            else:
                ng[nz] = v
                moved = True
                #print(f'moved {z} {nz}')
        else:
            ng[z] = v
    g = ng
    if not moved:
        break

print(t)
