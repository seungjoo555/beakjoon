import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dlist = []
for i in range(1, N+1):
    if N % i == 0:
        dlist.append(i)
if K > len(dlist):
    print(0)
else:
    print(dlist[K-1])