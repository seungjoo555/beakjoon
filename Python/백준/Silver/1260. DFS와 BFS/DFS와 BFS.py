import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    # 방문했다고 표시 -> 방문한 노드를 모아놓는 리스트 활용
    visited.append(node)
    # 할일 하기
    print(node, end = " ")
    for adj_node in sorted(graph[node]):
        if adj_node not in visited: dfs(adj_node)

def bfs(start):
    Queue.append(start)
    while Queue:
        node = Queue.popleft()
        visited.append(node)
        print(node, end = " ")
        for adj_node in sorted(graph[node]):
            if adj_node not in visited:
                if adj_node not in Queue:
                    Queue.append(adj_node)

Queue = deque()
visited =[]
dfs(V)
print()
visited.clear()
bfs(V)