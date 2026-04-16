import sys

list = sys.stdin.read().splitlines()
t = len(list)
for i in range(t):
    a, b = map(int, list[i].split())
    print(a+b)