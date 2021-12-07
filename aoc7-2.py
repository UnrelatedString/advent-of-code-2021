import sys

ns = [n for n in eval(input())]

cs = [sum(abs(n-x)*(abs(n-x)+1)//2 for n in ns) for x in range(max(ns))]
print(min(cs))
