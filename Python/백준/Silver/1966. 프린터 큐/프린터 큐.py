import sys
from collections import deque
input = map(int, sys.stdin.read().split())
N = next(input)
for _ in range(N):
    Queue = deque()
    check = deque()
    N = next(input)
    M = next(input)
    for _ in range(N):
        Queue.append(next(input))
    for i in range(len(Queue)):
        check.append(i)
    count = 0
    while True:
        f = 0
        for i in range(1, len(Queue)):
            if Queue[0] < Queue[i]:
                Queue.append(Queue.popleft())
                check.append(check.popleft())
                f = 1
                break
        if f == 1:
            continue
        Queue.popleft()
        count += 1
        if check.popleft() == M:
            break
        

    print(count)