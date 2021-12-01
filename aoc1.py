ls = iter(input,'')

n = int(next(ls))
s=0
for l in ls:
    x = int(l)
    s += n < x
    n = x

print(s)
