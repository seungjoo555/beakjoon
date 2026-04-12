import sys
from collections import deque
def queue():
    input = iter(sys.stdin.read().strip().split())
    Queue = deque()
    for _ in range(int(next(input))):
        ch = next(input)
        match ch:
            case 'push':
                Queue.append(int(next(input)))
            case 'pop':
                if Queue:
                    print(Queue.popleft())
                else:
                    print(-1)
            case 'size':
                print(len(Queue))
            case 'empty':
                if Queue:
                    print(0)
                else:
                    print(1)
            case 'front':
                if Queue:
                    print(Queue[0])
                else:
                    print(-1)
            case 'back':
                if Queue:
                    print(Queue[-1])
                else:
                    print(-1)
queue()