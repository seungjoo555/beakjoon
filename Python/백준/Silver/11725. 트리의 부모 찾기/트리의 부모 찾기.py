import sys
sys.setrecursionlimit(10**6)
input = map(int, sys.stdin.read().split())
N = next(input)
graph = [[] for _ in range(N+1)]
pr = [0] * (N-1)
for _ in range(N-1):
    a = next(input)
    b = next(input)
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = False
    for adj_node in graph[node]:
        if visited[adj_node]:
            pr[adj_node-2] = node
            dfs(adj_node)

visited =[True] * (N+1)
dfs(1)
print('\n'.join(map(str, pr)))