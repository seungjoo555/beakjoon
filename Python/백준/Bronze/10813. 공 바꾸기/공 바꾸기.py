import sys
input = sys.stdin.readline

N, M = map(int, input().split())

bucket = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]

for n in bucket:
    print(n, end = " ")