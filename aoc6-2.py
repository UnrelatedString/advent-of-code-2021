import sys

ns = [*eval(input())]

cs = [ns.count(n) for n in range(9)]
for _ in range(256):
    n = cs.pop(0)
    cs[6] += n
    cs.append(n)

print(sum(cs))
