import sys
input = map(int, sys.stdin.read().split())
N = next(input)
s = [(a, b) for a, b in zip(input, input)]
s.sort(key=lambda x: (x[0], x[1]))
for i in s:
    print(*i)