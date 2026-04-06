import sys
sys.setrecursionlimit(10**6)
input = map(int, sys.stdin.read().split())
N = next(input)
graph = [[] for _ in range(N+1)]
pr = [0] * (N)
for _ in range(N-1):
    a = next(input)
    b = next(input)
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    for adj_node in graph[node]:
        if pr[adj_node-1] == 0:
            pr[adj_node-1] = node
            dfs(adj_node)

dfs(1)
print('\n'.join(map(str, pr[1:])))