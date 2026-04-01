import sys
from collections import deque
inp = map(int, sys.stdin.read().split())
n = next(inp)
m = next(inp)
r = next(inp)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a = next(inp)
    b = next(inp)
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    count = 1
    Queue.append(start)
    visited[start] = count
    while Queue:
        node = Queue.popleft()
        for adj_node in sorted(graph[node]):
            if not visited[adj_node]:
                count += 1
                Queue.append(adj_node)
                visited[adj_node] = count

Queue = deque()
visited =[0] *(n+1)
bfs(r)
# sys.stdout.write('\n'.join(map(str, visited[1:])))
print(*visited[1:], sep = '\n')