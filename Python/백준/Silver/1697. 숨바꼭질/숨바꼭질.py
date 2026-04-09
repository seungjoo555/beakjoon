from collections import deque

N, K = map(int, input().split())

def time(st):
    Queue = deque()
    Queue.append(st)
    while Queue:
        node = Queue.popleft()
        if node == K:
            return
        for adj_node in (node-1,node+1,node*2):
            if  0 <= adj_node <= 100000  and not chek[adj_node]:
                chek[adj_node] = chek[node] +1
                Queue.append(adj_node)

chek = [0] * 100001
time(N)
print(chek[K])
