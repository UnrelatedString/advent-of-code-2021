import sys

ls = [l for l in iter(input,'')]#sys.stdin]
#ns = [n for n in eval(input())]#OPTIONS

s = []
c = dict(zip('{[(<','}])>'))
ss = {')':1,']':2,'}':3,'>':4}
for l in ls:
    bs = []
    for b in l:
        if b in c:
            bs.append(c[b])
        elif not bs:
            break
        elif bs.pop() != b:
            break
    else:
        s.append(int(''.join(str(ss[x]) for x in bs[::-1]),base=5))

print(sorted(s)[len(s)//2])
