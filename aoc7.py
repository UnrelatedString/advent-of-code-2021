import sys

ns = [n for n in eval(input())]

cs = [sum(abs(n-x) for n in ns) for x in range(max(ns))]
print(min(cs))
