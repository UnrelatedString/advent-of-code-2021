l = input().lstrip('target area:').split(', ')

xr,yr = (sorted(int(n) for n in r[2:].split('..')) for r in l)

yv = -1-min(yr)
my = yv*(yv+1)//2
print(my)
