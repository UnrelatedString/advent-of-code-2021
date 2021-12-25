import sys
from stuff import *

ls = lines()#chunks()#nums()

def ri(c):return'wxyz'.find(c)

def to26(n):
    while n:
        yield n % 26
        n //= 26

def run(prog, rs, ds = ()):
    for i, l in enumerate(prog):
        #print(i)
        if l.startswith('inp'):
            # for n in range(9,0,-1):
            #     rl = rs[:]
            #     rl[ri(l[4])] = n
            #     run(prog[i+1:], rl, ds+(n,))
            # break
            rs[ri('w')] = None
        else:
            o, a, b = l.split()
            if b in 'wxyz':
                b = rs[ri(b)]
            if b is None:
                x = rs[ri('x')]
                z = rs[ri('z')]
                rs[ri('w')] = int(input(f'x = {x}, z = {[*to26(z)][::-1]} ? '))
                b = rs[ri('w')]
            else:
                b = int(b)
            ai = ri(a)
            av = rs[ai]
            #print(o,av,b)
            rs[ai] = {
                'add': av+b,
                'mul': av*b,
                'div': av//b if b else None,
                'mod': av%b if b else None,
                'eql': int(av==b)
            }[o]
    else:
        # if rs[ri('z')] == 0:
        #     print(''.join(f'{d}' for d in ds))
        print(rs[ri('z')])

run(ls, [0,0,0,0])
