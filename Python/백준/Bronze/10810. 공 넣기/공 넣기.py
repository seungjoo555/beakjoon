import sys

n, m = map(int, sys.stdin.readline().split())
bucket = [0 for _ in range(n)]
for a in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for b in range(i-1, j):
        bucket[b] = k
for c in range(len(bucket)):
    print(bucket[c], end = " ")