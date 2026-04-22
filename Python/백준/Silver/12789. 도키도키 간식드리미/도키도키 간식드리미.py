import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
nlist = deque(list(map(int, input().split())))
stack = []
check = 1
while nlist:
    if nlist[0] == check:
        nlist.popleft()
        check += 1
    elif stack and stack[-1] == check:
        stack.pop()
        check += 1
    else:
        stack.append(nlist.popleft())

while stack:
    n = stack.pop()
    if n != check:
        print("Sad")
        break
    else:
        check += 1

if not stack:
    print("Nice")