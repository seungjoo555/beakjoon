import sys
input = map(int, sys.stdin.read().split())
T = next(input)
for _ in range(T):
    a = next(input)
    b = next(input)
    c = next(input)
    print(min([a,b,c]))