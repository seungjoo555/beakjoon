import sys
sys.setrecursionlimit(10**6)
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


def dfs(node):
    global count
    visited[node] = count
    for adj_node in sorted(graph[node]):
        if not visited[adj_node]:
            count += 1
            dfs(adj_node)

count = 1
visited = [0] * (n+1)
dfs(r)
sys.stdout.write('\n'.join(map(str, visited[1:])))