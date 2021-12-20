import sys
from stuff import *

a = lines()
a = ''.join(a) #damn it Eric

ls = lines()#chunks()#nums()

g = [[v == '#' for v in r] for r in ls]

# for it in range(2):
#     ng = []
#     p = 0
#     inv = (it%2) and a[0]=='#'
#     for _ in range(2):
#         for r in g:
#             r.append(p)
#             r.insert(p,0)
#         pr = [p for _ in g[0]]
#         g = [[*pr],*g,[*pr]]
#     ng = []
#     for r in slices(g,3):
#         nr = []
#         ng.append(nr)
#         for c in slices([*zip(*r)],3):
#             c = zip(*c)
#             n = 0
#             for rr in c:
#                 for v in rr:
#                     n <<= 1
#                     n += v^inv
#             nr.append((a[n]=='#')^inv)
#     g=ng
#     for _ in range(1):
#         for r in g:
#             r.append(p)
#             r.insert(p,0)
#         pr = [p for _ in g[0]]
#         g = [[*pr],*g,[*pr]]
#     #for r in g:print(''.join('.#'[v] for v in r))
#
# print(sum(sum( v for v in r) for r in g))

for it in range(50):
    ng = []
    p = (it)%2 and a[0] == '#'
    for _ in range(5):
        for r in g:
            r.append(p)
            r.insert(0,p) #..............................
        pr = [p for _ in g[0]]
        g = [[*pr],*g,[*pr]]
    ng = []
    for r in slices(g,3):
        nr = []
        ng.append(nr)
        for c in slices([*zip(*r)],3):
            c = zip(*c)
            n = 0
            for rr in c:
                for v in rr:
                    n <<= 1
                    n += v
            nr.append(a[n]=='#')
    g=ng
    #for r in g:print(''.join('.#'[v] for v in r))

print(sum(map(sum,g)))

# #why does my input start with a #??????????????
# g = {}
# for y,r in enumerate(ls):
#     for x,v in enumerate(r):
#         z = complex(x,y)
#         g[z] = v == '#'
#         for o in moore:
#             if z+o not in g:
#                 g[z+o] = 0
#
# for it in range(2):
#     p  =(it+1)%2 and a[0] == '#'
#     # ng = {}
#     # for z in g:
#     #     for o in moore:
#     #         if z+o not in g:
#     #             ng[z+o] = p
#     # g = ng
#     # ng = {}
#     # for z in g:
#     #     for o in moore:
#     #         if z+o not in g:
#     #             ng[z+o] = p
#     # g = ng
#     ng = {}
#     for z,v in g.items():
#         n = 0
#         for o in -1-1j,-1j,1-1j,-1,0,1,-1+1j,1j,1+1j:
#             n <<= 1
#             if z+o in g:
#                 n += g[z+o]
#             else:
#                 n += p
#         ng[z] = a[n] == '#'
#     g = ng
#
# print(sum(g.values()))
