from collections import deque

queue = deque()

N = int(input())

# 카드를 enqueue
for i in range(N):
    queue.append(i+1)

while len(queue) > 1:
    queue.popleft()
    item = queue.popleft()
    queue.append(item)

print(queue[0])