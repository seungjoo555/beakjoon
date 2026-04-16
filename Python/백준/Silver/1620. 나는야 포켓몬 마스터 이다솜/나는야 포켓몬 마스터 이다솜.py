import sys
input = sys.stdin.readline
N, M = map(int, input().split())
poke = {}
for i in range(1, N+1):
    s = input().strip()
    poke[str(i)] = s
    poke[s] = str(i)
for _ in range(M):
    ip = input().strip()
    print(poke[ip])