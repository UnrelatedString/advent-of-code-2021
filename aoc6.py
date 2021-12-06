import sys

ns = [*eval(input())]

for _ in range(80):
    u = []
    for n in ns:
        if n == 0:
            u.append(6)
            u.append(8)
        else:
            u.append(n-1)
    ns = u

print(len(ns))
