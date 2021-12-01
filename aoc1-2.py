ls = [*map(int,iter(input,''))]

ss = []
for i in range(len(ls)-2):
    ss.append(sum(ls[i:i+3]))

s = 0
n = ss[0]
for l in ss[1:]:
    x = int(l)
    s += n < x
    n = x

print(s)
