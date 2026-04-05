from collections import deque
import sys

input = map(int, sys.stdin.read().split())
N = next(input)
Queue = deque()
while True:
    number = next(input)
    if number > 0 and len(Queue) != N:
            Queue.append(number)
    elif number == 0:
        Queue.popleft()
    elif number == -1:
        break
if Queue:
    print(' '.join(map(str, Queue)))
else:
    print("empty")