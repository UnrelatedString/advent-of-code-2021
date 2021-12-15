import re
import itertools as itr
import collections

dd = collections.defaultdict
cr = collections.Counter

def lines():
    return [*iter(input,'')]

def chunks(sentinel='e'):
    return [c.split('\n') for c in '\n'.join(iter(input,'')).rstrip('\n').split('\n\n')]

def nums():
    return eval(input())

moore = 1,1+1j,1j,-1+1j,-1,-1-1j,-1j,1-1j
von_neumann = 1,1j,-1,-1j

def c_t(z):
    return z.real, z.imag

def bidict(d):
    ret = {k:set() for k in itr.chain(d.keys(),d.values())}
    for k,v in d.items():
        ret[k].add(v)
        ret[v].add(k)

def slices(l,n):
    return [l[i:i+n] for i in range(len(ls)-n+1)]
