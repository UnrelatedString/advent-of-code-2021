ls = [*iter(input,'')]

c = 0+0j
a = 0
for l in ls:
    d,n = l.split()
    n = int(n)
    if d[0] == 'u':
        a -= n
    elif d[0] == 'd':
        a += n
    else:
        c += complex(1,a)*n

print(c.real*c.imag)
