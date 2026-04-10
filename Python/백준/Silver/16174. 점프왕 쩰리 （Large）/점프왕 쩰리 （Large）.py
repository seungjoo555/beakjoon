import sys
from collections import deque
N = int(input())
gamepan = []
for _ in range(N):
    gamepan.append(list(map(int, sys.stdin.readline().split())))

check = [[0]*N for _ in range(N)]
def jump(x, y):
    Queue = deque()
    Queue.append([x, y])
    while Queue:
        x, y = Queue.popleft()
        n = gamepan[x][y]
        for x, y in ([[x+n,y],[x,y+n]]):
            if x < N and y < N and not check[x][y]:
                check[x][y] = 1
                if gamepan[x][y] == -1:
                    return "HaruHaru"
                Queue.append([x, y])
    return "Hing"
    
print(jump(0,0))


