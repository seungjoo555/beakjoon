import sys
input = sys.stdin.readline

t1, t2, t3 = map(int, input().split())
c1 = t2 + t3
c2 = t1 + t3
c3 = t1 + t2

if t1 >= c1:
    t1 = c1 - 1
elif t2 >= c2:
    t2 = c2 -1
elif t3 >= c3:
    t3 = c3 -1

print(t1+t2+t3)