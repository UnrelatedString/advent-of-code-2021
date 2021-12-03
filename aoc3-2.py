ls = [l for l in iter(input,'')]

def h(ls):
    bs = zip(*ls)
    g = []
    for b in bs:
        g.append(sorted(b)[::1][len(ls)//2]== '1')
    return g

def f(s,i,n):
    b = h(s)[i] ^ n
    k = {l for l in s if (l[i] == '1') == b}
    return k

c = set(ls)
o = set(ls)
for i in range(len(ls[0])):
    c &= (f(c,i,0) or c)
    o &= (f(o,i,1) or o)

print(eval(f'0b{c.pop()} * 0b{o.pop()}'))
