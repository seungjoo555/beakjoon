import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bucket = [i+1 for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    for k in range((j-i+1)//2):
        bucket[i+(k-1)],bucket[j-(1+k)] = bucket[j-(1+k)], bucket[i+(k-1)]
for i in range(N):
    print(bucket[i], end=" ")