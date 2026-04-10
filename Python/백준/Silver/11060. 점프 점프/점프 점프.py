import sys
from collections import deque
N = int(input())
check = [0]*(N+1)
miro = list(map(int, sys.stdin.readline().split()))
def bsf(n):
    Queue = deque()
    Queue.append(n)
    while Queue:
        node = Queue.popleft()
        if node == N:
            return
        for adj_node in (i for i in range(node+1,node+1+miro[node-1])):
            if 0 < adj_node <= N and not check[adj_node]:
                check[adj_node] = check[node]+1
                Queue.append(adj_node)

if N == 1:
    print(0)
else:
    bsf(1)
    print(check[N] if check[N] else -1)
        
