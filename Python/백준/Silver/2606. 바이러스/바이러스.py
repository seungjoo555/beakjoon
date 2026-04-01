import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)





def dfs(node):
    visited.append(node)
    for adj_node in graph[node]:
        if adj_node not in visited: dfs(adj_node)

visited = []
dfs(1)
print(len(visited)-1)