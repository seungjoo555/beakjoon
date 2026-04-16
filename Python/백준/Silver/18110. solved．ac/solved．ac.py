import sys
input = map(int, sys.stdin.read().split())
def real_round(val):
    return int(val + 0.5)
n = next(input)
d = real_round(n*0.15)

lev = list(input)
lev.sort()
if n == 0:
    print(0)
elif n < 4:
    print(real_round(sum(lev)/n))
else:
    print(real_round(sum(lev[d:-d])/(n-d*2)))
