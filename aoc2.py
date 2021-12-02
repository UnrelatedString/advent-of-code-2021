ls = [*iter(input,'')]

c = 0+0j
for l in ls:
    d,n = l.split()
    d = 1j**'fdbu'.find(d[0])
    c += d * int(n)

print(c.real*c.imag)
