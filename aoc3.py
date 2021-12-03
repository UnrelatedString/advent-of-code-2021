ls = [l for l in iter(input,'')]

bs = zip(*ls)
g = []
for b in bs:
    g.append(sorted(b)[len(ls)//2]== '1')

e = [int(not b) for b in g]

def d(x):
    return eval(f'0b{"".join(str(int(b)) for b in x)}')

print(d(e)*d(g))
