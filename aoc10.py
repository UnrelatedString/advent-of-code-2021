import sys

ls = [l for l in iter(input,'')]#sys.stdin]
#ns = [n for n in eval(input())]#OPTIONS

s = 0
c = dict(zip('{[(<','}])>'))
ss = {')':3,']':57,'}':1197,'>':25137}
for l in ls:
    bs = []
    for b in l:
        if b in c:
            bs.append(c[b])
        elif not bs:
            break
        elif bs.pop() != b:
            s += ss[b]
            break

print(s)
