import re

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
