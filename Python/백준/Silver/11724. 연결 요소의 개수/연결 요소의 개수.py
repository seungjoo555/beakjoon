import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs2(start):
    Queue.append(start)
    while Queue:
        node = Queue.popleft()
        visited.append(node)
        for adj_node in graph[node]:
            if adj_node not in visited:
                if adj_node not in Queue:
                    Queue.append(adj_node)



visited =[]
count = 0
for i in range(1, n+1):
    if i not in visited:
        Queue = deque()
        bfs2(i)
        count += 1
print(count)